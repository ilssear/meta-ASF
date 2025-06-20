#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Semantic SPECIFICATIONS.md Parser for SpecFirst Framework

This module provides robust, semantic parsing of SPECIFICATIONS.md for all validation and documentation scripts.

Features:
- Understands hierarchical, path-hinted structure (e.g., 0. Section Name (/docs/))
- Handles any numbering (including zero-padded and multi-digit)
- Properly manages directory stacks and indentation
- Ignores description lines and invalid sections
- No hard-coded mappings; all paths are built from the spec structure
- Only processes files/directories within valid sections

Usage Example (LLM/Cursor):

    from pathlib import Path
    from lib.semantic_parser import SemanticSpecParser
    parser = SemanticSpecParser(Path("/path/to/project"))
    files = parser.parse_documentation_files()
    for path, spec in files.items():
        print(path, spec.status)

See the scripts/README.md for more details and integration examples.
"""

import re
import logging
from pathlib import Path
from typing import List, Dict, Set, Optional
from dataclasses import dataclass
from enum import Enum

# --- Constants ---

SUPPORTED_EXTENSIONS = ('.md', '.txt', '.rst', '.html', '.css', '.js', '.json', '.yaml', '.yml', '.py', '.template')

# --- Shared Data Classes ---

class FileStatus(Enum):
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    UNSPECIFIED = "UNSPECIFIED"

@dataclass
class FileSpec:
    """Represents a file specification with semantic information."""
    path: str
    status: FileStatus
    description: str = ""
    exists: bool = False

@dataclass
class Section:
    """Represents a documentation section."""
    number: str
    name: str
    path_hint: str
    level: int

# --- Main Parser Class ---

class SemanticSpecParser:
    """Semantic parser that understands SPECIFICATIONS.md structure."""
    
    def __init__(self, root_dir: Path, logger: Optional[logging.Logger] = None):
        self.root_dir = root_dir
        self.specs_file = root_dir / "SPECIFICATIONS.md"
        self.logger = logger or logging.getLogger(__name__)
        
    def parse_documentation_files(self) -> Dict[str, FileSpec]:
        """
        Parse SPECIFICATIONS.md to find documentation files using semantic understanding.
        
        Returns:
            Dictionary mapping file paths to FileSpec objects.
        """
        if not self.specs_file.is_file():
            self.logger.warning("SPECIFICATIONS.md not found, cannot parse documentation files.")
            return {}
            
        content = self.specs_file.read_text(encoding='utf-8')
        doc_section = self._extract_doc_section(content)
        
        if not doc_section:
            self.logger.warning("Documentation Generation section not found in SPECIFICATIONS.md")
            return {}
            
        return self._parse_doc_section_semantically(doc_section)
    
    def _extract_doc_section(self, content: str) -> List[str]:
        """Extract the Documentation Generation section from SPECIFICATIONS.md."""
        lines = content.splitlines()
        try:
            start_index = next(i for i, line in enumerate(lines) 
                             if line.strip().startswith('### Documentation Generation'))
        except StopIteration:
            return []
        
        doc_section = []
        for line in lines[start_index + 1:]:
            if line.strip().startswith(('###', '## ')):
                break
            doc_section.append(line)
        return doc_section
    
    def _parse_doc_section_semantically(self, doc_section: List[str]) -> Dict[str, FileSpec]:
        """Parse the documentation section using semantic understanding."""
        specified_files = {}
        current_section = None
        dir_stack = []  # Each entry: (indent_level, dir_name)
        section_path = []

        for line in doc_section:
            if not line.strip() or line.strip().startswith('#'):
                continue

            indent = len(line) - len(line.lstrip())
            level = indent // 2
            content = line.strip()

            # Section header: reset stack to section path
            section_match = re.match(r'^(\d+\.)\s+(.+?)\s+\(([^)]+)\)$', content)
            if section_match:
                number = section_match.group(1)
                name = section_match.group(2).strip()
                path_hint = section_match.group(3).strip()
                current_section = Section(number=number, name=name, path_hint=path_hint, level=level)
                section_path = self._resolve_path_from_hint(path_hint)
                dir_stack = []  # Reset stack for new section
                continue
            # If at root level and not a section header, reset current_section
            if level == 0:
                current_section = None
                continue

            # Only process if inside a valid section
            if not current_section:
                continue

            # Directory: adjust stack to correct level, then append
            dir_match = re.match(r'^-\s+(.+?)/$', content)
            if dir_match:
                dir_name = dir_match.group(1).strip()
                # Pop stack to current level, then append
                while dir_stack and dir_stack[-1][0] >= level:
                    dir_stack.pop()
                dir_stack.append((level, dir_name))
                continue

            # File: adjust stack to correct level, then build path
            file_match = re.match(r'^-\s+(.+?)\s+\((REQUIRED|OPTIONAL)\)$', content)
            if file_match:
                file_name = file_match.group(1).strip()
                status = FileStatus(file_match.group(2))
                # Pop stack to current level (file is always a leaf)
                while dir_stack and dir_stack[-1][0] >= level:
                    dir_stack.pop()
                # Build path: section_path + dirs in stack + file
                path_parts = ['docs'] + section_path + [d for _, d in dir_stack] + [file_name]
                full_path = Path(*path_parts).as_posix()
                specified_files[full_path] = FileSpec(path=full_path, status=status)
                continue

            # Description: ignore
            if content.startswith('*'):
                continue

            # If line doesn't match any pattern, skip
            continue

        return specified_files
    
    def _resolve_path_from_hint(self, path_hint: str) -> List[str]:
        """
        Resolve the actual path from a path hint like '/docs/' or '/docs/framework/'.
        
        Args:
            path_hint: Path hint from the specification
            
        Returns:
            List of path components (excluding 'docs' which is added later)
        """
        # Remove leading/trailing slashes and split
        clean_path = path_hint.strip('/')
        if clean_path == 'docs':
            return []  # Root docs directory
        elif clean_path.startswith('docs/'):
            # Remove 'docs/' prefix and split remaining path
            remaining = clean_path[5:]  # Remove 'docs/'
            return remaining.split('/') if remaining else []
        else:
            # If path hint doesn't start with docs/, assume it's relative to docs
            return clean_path.split('/') if clean_path else []
    
    def parse_source_files(self) -> List[str]:
        """
        Parse SPECIFICATIONS.md to find required source files (methodology/*, defaults/*, scripts/*).
        
        Returns:
            List of required source file paths relative to project root.
        """
        if not self.specs_file.is_file():
            self.logger.warning("SPECIFICATIONS.md not found, cannot parse source files.")
            return []
            
        content = self.specs_file.read_text(encoding='utf-8')
        lines = content.splitlines()
        
        required_files = []
        
        # Parse methodology files from Documentation Synchronization Paths
        in_sync_section = False
        for line in lines:
            if "#### Documentation Synchronization Paths" in line:
                in_sync_section = True
                continue
            
            if in_sync_section:
                if line.strip().startswith(('##', '### ')):
                    break
                
                # Look for methodology source files (only complete file paths)
                match = re.search(r"-\s+(methodology/[^\s]+\.md)", line)
                if match:
                    source_path = match.group(1).strip()
                    required_files.append(source_path)

        # Parse defaults files from Implementation Requirements
        in_impl_section = False
        for line in lines:
            if "## Implementation Requirements" in line:
                in_impl_section = True
                continue
            
            if in_impl_section and line.strip().startswith(('##', '### ')):
                break
            
            # Look for defaults files (only complete file paths)
            if "defaults/" in line and line.strip().startswith("-"):
                match = re.search(r"defaults/[^\s]+\.(?:json|py|md)", line)
                if match:
                    source_path = match.group(0).strip()
                    required_files.append(source_path)

        # Parse scripts files from Framework Scripts section
        in_scripts_section = False
        for line in lines:
            if "### Framework Scripts" in line:
                in_scripts_section = True
                continue
            
            if in_scripts_section and line.strip().startswith(('##', '### ')):
                break
            
            # Look for scripts files (only complete file paths)
            if "scripts/" in line and line.strip().startswith("-"):
                match = re.search(r"scripts/[^\s]+\.py", line)
                if match:
                    source_path = match.group(0).strip()
                    required_files.append(source_path)

        return required_files 