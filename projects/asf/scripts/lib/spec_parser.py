#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Shared SPECIFICATIONS.md Parser for SpecFirst Framework

This module provides common functionality for parsing SPECIFICATIONS.md
across all validation scripts, ensuring consistency and reducing duplication.
"""

import re
import logging
from pathlib import Path
from typing import List, Dict, Set, Optional
from dataclasses import dataclass
from enum import Enum

# --- Shared Data Classes ---

class FileStatus(Enum):
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    UNSPECIFIED = "UNSPECIFIED"

@dataclass
class SpecFile:
    """Represents a file specified in SPECIFICATIONS.md."""
    path: str
    status: FileStatus
    description: str = ""
    exists: bool = False

# --- Configuration Constants ---

SUPPORTED_EXTENSIONS = ('.md', '.py', '.yaml', '.json', '.template')

DIRECTORY_MAPPING = {
    "Default Configurations": "defaults",
    "Framework Documentation": "framework", 
    "Development Guides": "development",
    "User Preferences": "user",
}

# --- Main Parser Class ---

class SpecParser:
    """Parses SPECIFICATIONS.md to extract file requirements and structure."""
    
    def __init__(self, root_dir: Path, logger: Optional[logging.Logger] = None):
        self.root_dir = root_dir
        self.specs_file = root_dir / "SPECIFICATIONS.md"
        self.logger = logger or logging.getLogger(__name__)
        
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
    
    def parse_documentation_files(self) -> Dict[str, SpecFile]:
        """
        Parse SPECIFICATIONS.md to find documentation files in the docs/ directory.
        
        Returns:
            Dictionary mapping file paths to SpecFile objects.
        """
        if not self.specs_file.is_file():
            self.logger.warning("SPECIFICATIONS.md not found, cannot parse documentation files.")
            return {}
            
        content = self.specs_file.read_text(encoding='utf-8')
        doc_section = self._extract_doc_section(content)
        
        if not doc_section:
            self.logger.warning("Documentation Generation section not found in SPECIFICATIONS.md")
            return {}
            
        return self._parse_doc_section(doc_section)
    
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
    
    def _parse_doc_section(self, doc_section: List[str]) -> Dict[str, SpecFile]:
        """Parse the documentation section to extract file specifications."""
        specified_files = {}
        stack = []  # Each entry: (indent_level, dir_name)
        
        for line in doc_section:
            if not line.strip() or line.strip().startswith('#'):
                continue

            indent = len(line) - len(line.lstrip())
            level = indent // 2
            content_str = line.strip().lstrip('- ').lstrip('123456789. ')

            if content_str.startswith('*'):
                continue

            file_match = re.match(
                r'([^()]+\.(?:' + '|'.join(ext.lstrip('.') for ext in SUPPORTED_EXTENSIONS) + r'))\s*\((REQUIRED|OPTIONAL)\)', 
                content_str
            )
            if file_match:
                self._parse_file_entry(file_match, stack, specified_files)
            elif content_str.endswith('/') or not re.search(
                r'\.(?:' + '|'.join(ext.lstrip('.') for ext in SUPPORTED_EXTENSIONS) + r')($|\s)', 
                content_str
            ):
                self._update_directory_stack(content_str, level, stack)

        return specified_files
    
    def _parse_file_entry(self, match: re.Match, stack: List, specified_files: Dict[str, SpecFile]):
        """Parse a file line and add it to the specified_files dictionary."""
        file_name = match.group(1).strip()
        status = FileStatus(match.group(2))
        
        path_parts = [DIRECTORY_MAPPING.get(d, d) for _, d in stack]
        full_path = Path('docs', *path_parts, file_name).as_posix()
        
        specified_files[full_path] = SpecFile(path=full_path, status=status)
        self.logger.debug(f"Parsed file: {full_path} ({status.value})")

    def _update_directory_stack(self, content: str, level: int, stack: List):
        """Update the directory stack based on the current line's indentation."""
        while stack and stack[-1][0] >= level:
            stack.pop()
        
        dir_name = content.split('(')[0].strip().rstrip('/')
        stack.append((level, dir_name))
        self.logger.debug(f"Directory stack at level {level}: {[d for _, d in stack]}") 