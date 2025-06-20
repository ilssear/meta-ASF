#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Documentation Checker for SpecFirst Framework

This script validates the documentation structure against SPECIFICATIONS.md,
ensuring all required files exist and are properly formatted.
"""

import os
import re
import sys
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class FileStatus(Enum):
    REQUIRED = "REQUIRED"
    OPTIONAL = "OPTIONAL"
    UNSPECIFIED = "UNSPECIFIED"

@dataclass
class DocFile:
    path: str
    status: FileStatus
    description: str = ""
    exists: bool = False

class DocumentationChecker:
    def __init__(self, root_dir: str = ".", verbose: bool = False):
        """Initialize the documentation checker.
        
        Args:
            root_dir: Root directory of the project (directory containing SPECIFICATIONS.md)
            verbose: Enable verbose logging
        """
        self.root_dir = Path(root_dir)
        self.specs_file = self.root_dir / "SPECIFICATIONS.md"
        if not self.specs_file.exists():
            raise FileNotFoundError(f"SPECIFICATIONS.md not found in {root_dir}. This directory must contain SPECIFICATIONS.md to be considered a project root.")
        self.docs_dir = self.root_dir / "docs"
        self.required_files: Set[str] = set()
        self.optional_files: Set[str] = set()
        self.existing_files: Set[str] = set()
        self.missing_files: Set[str] = set()
        self.unnecessary_files: Set[str] = set()
        self.file_descriptions: Dict[str, str] = {}
        
        # Configure logging
        log_level = logging.DEBUG if verbose else logging.ERROR
        logging.basicConfig(
            level=log_level,
            format='%(levelname)s: %(message)s',
            handlers=[
                logging.StreamHandler(sys.stderr)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def parse_specifications(self) -> None:
        """Parse SPECIFICATIONS.md to extract required and optional files."""
        try:
            content = self.specs_file.read_text(encoding='utf-8')
        except FileNotFoundError:
            self.logger.error(f"{self.specs_file} not found")
            sys.exit(1)
        except Exception as e:
            self.logger.error(f"Error reading {self.specs_file}: {e}")
            sys.exit(1)

        # Find the Documentation Generation section (nested under Implementation Requirements)
        doc_section = None
        in_doc_section = False
        for line in content.splitlines():
            if line.strip().startswith('### Documentation Generation'):
                in_doc_section = True
                doc_section = []
                continue
            if in_doc_section:
                # Stop at the next section header
                if line.strip().startswith('###') or line.strip().startswith('## '):
                    break
                doc_section.append(line)
        if not doc_section:
            self.logger.error("Documentation Generation section not found in SPECIFICATIONS.md")
            sys.exit(1)

        # DEBUG: Print the raw lines from the Documentation Generation section
        self.logger.debug("Raw lines from Documentation Generation section:")
        for raw_line in doc_section:
            self.logger.debug(f"  {repr(raw_line)}")

        # Parse the hierarchical bullet list using a stack for directory context
        stack = []  # Each entry: (indent_level, dir_name)
        for line in doc_section:
            # Skip empty lines and section headers
            if not line.strip() or line.strip().startswith('#'):
                continue

            # Calculate indentation level (2 spaces per level)
            indent = len(line) - len(line.lstrip())
            level = indent // 2

            # Remove bullet, number, and leading/trailing spaces
            content = line.strip()
            if content.startswith('-'):
                content = content[1:].strip()
            elif re.match(r'^\d+\.', content):
                content = re.sub(r'^\d+\.\s*', '', content)

            # Skip description lines (start with *)
            if content.startswith('*'):
                continue

            # 1. Check for file: has a file extension and (REQUIRED) or (OPTIONAL)
            file_match = re.match(r'([^()]+\.(md|py|yaml|json|template))\s*\((REQUIRED|OPTIONAL)\)', content)
            if file_match:
                file_name = file_match.group(1).strip()
                status = file_match.group(3)
                # Build full path from stack, using the actual directory names
                path_parts = [d for _, d in stack]
                # Replace category names with actual directory names
                path_parts = [p.replace('Default Configurations', 'defaults').replace('Framework Documentation', 'framework').replace('Development Guides', 'development').replace('User Preferences', 'user') for p in path_parts]
                full_path = os.path.join('docs', *path_parts, file_name).replace('\\', '/')
                self.logger.debug(f"Parsed file: {full_path} ({status})")
                if status == 'REQUIRED':
                    self.required_files.add(full_path)
                elif status == 'OPTIONAL':
                    self.optional_files.add(full_path)
                continue

            # 2. Directory: ends with '/' or has no file extension
            if content.endswith('/') or not re.search(r'\.(md|py|yaml|json|template)($|\s)', content):
                # Update stack to current level
                if len(stack) > level:
                    stack = stack[:level]
                # Extract directory name (before '(' if present)
                dir_name = content.split('(')[0].strip().rstrip('/')
                stack.append((level, dir_name))
                self.logger.debug(f"Directory stack at level {level}: {[d for _, d in stack]}")
                continue

        # DEBUG: Print parsed files
        self.logger.debug("Parsed Required Files:")
        for f in sorted(self.required_files):
            self.logger.debug(f"  - {f}")
        self.logger.debug("Parsed Optional Files:")
        for f in sorted(self.optional_files):
            self.logger.debug(f"  - {f}")

    def debug_print_parsed_files(self):
        """Print parsed files in debug mode."""
        self.logger.debug("Parsed Required Files:")
        for f in sorted(self.required_files):
            self.logger.debug(f"  - {f}")
        self.logger.debug("Parsed Optional Files:")
        for f in sorted(self.optional_files):
            self.logger.debug(f"  - {f}")

    def scan_existing_files(self) -> None:
        """Scan the docs directory for existing files."""
        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(('.md', '.py', '.yaml', '.json', '.template')):
                    # Get path relative to root_dir
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, self.root_dir)
                    rel_path = rel_path.replace('\\', '/')
                    self.existing_files.add(rel_path)
                    self.logger.debug(f"Found existing file: {rel_path}")

    def analyze_documentation(self) -> None:
        """Analyze documentation completeness and identify issues."""
        # Find missing required files
        self.missing_files = self.required_files - self.existing_files
        for file in self.missing_files:
            self.logger.error(f"Missing required file: {file}")
        
        # Find unnecessary files (exist but not in specs)
        all_specified_files = self.required_files | self.optional_files
        self.unnecessary_files = self.existing_files - all_specified_files
        for file in self.unnecessary_files:
            self.logger.warning(f"Unnecessary file found: {file}")

    def generate_report(self) -> str:
        """Generate a comprehensive report of the documentation status."""
        report = []
        report.append("# Documentation Analysis Report\n")

        # Summary statistics
        report.append("## Summary Statistics")
        report.append(f"- Required Files: {len(self.required_files)}")
        report.append(f"- Optional Files: {len(self.optional_files)}")
        report.append(f"- Existing Files: {len(self.existing_files)}")
        report.append(f"- Missing Files: {len(self.missing_files)}")
        report.append(f"- Unnecessary Files: {len(self.unnecessary_files)}\n")

        # Directory structure
        report.append("## Directory Structure")
        for dir_path in sorted(set(os.path.dirname(f) for f in self.required_files | self.optional_files)):
            # Check if directory exists
            full_dir_path = os.path.join(self.root_dir, dir_path)
            dir_exists = os.path.exists(full_dir_path)
            status = "✅" if dir_exists else "❌"
            report.append(f"{status} {dir_path}/")
            for file in sorted(f for f in self.required_files | self.optional_files if os.path.dirname(f) == dir_path):
                full_file_path = os.path.join(self.root_dir, file)
                exists = os.path.exists(full_file_path)
                if file in self.optional_files:
                    file_status = "✅" if exists else "⚪"
                else:
                    file_status = "✅" if exists else "❌"
                report.append(f"  {file_status} {os.path.basename(file)}")
        report.append("")

        # Missing required files
        if self.missing_files:
            report.append("## Missing Required Files")
            for file in sorted(self.missing_files):
                report.append(f"- {file}")
                report.append(f"  * Purpose: No description available")
                report.append(f"  * Status: Required")
                report.append(f"  * Action: Create this file")
            report.append("")

        # Missing optional files
        missing_optional = [f for f in self.optional_files if not os.path.exists(os.path.join(self.root_dir, f))]
        if missing_optional:
            report.append("## Missing Optional Files")
            for file in sorted(missing_optional):
                report.append(f"- {file}")
                if self.logger.level == logging.DEBUG:
                    report.append(f"  * Purpose: No description available")
            report.append("")

        # Unnecessary files
        if self.unnecessary_files:
            report.append("## Unnecessary Files")
            report.append("These files exist but are not specified in SPECIFICATIONS.md:")
            for file in sorted(self.unnecessary_files):
                report.append(f"- {file}")
                report.append(f"  * Action: Either remove this file or update SPECIFICATIONS.md")
            report.append("")

        # LLM guidance
        report.append("## LLM Guidance\n")
        report.append("### Files to Generate")
        for file in sorted(self.missing_files):
            report.append(f"- {file}")
            report.append(f"  * Purpose: No description available")
            report.append(f"  * Required Content:")
            report.append(f"    - Copyright header")
            report.append(f"    - Version information")
            report.append(f"    - Content matching description")
            report.append(f"    - Proper cross-references")

        return "\n".join(report)

def main():
    """Main entry point for the documentation checker."""
    parser = argparse.ArgumentParser(description="Check documentation against specifications.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
    parser.add_argument("--root-dir", default=".", help="Root directory of the project")
    args = parser.parse_args()
    
    checker = DocumentationChecker(root_dir=args.root_dir, verbose=args.verbose)
    
    # Parse specifications and analyze documentation
    checker.parse_specifications()
    checker.scan_existing_files()
    checker.analyze_documentation()
    
    # Generate and print report
    report = checker.generate_report()
    print(report)
    
    # Exit with error if required files are missing
    if checker.missing_files:
        sys.exit(1)

if __name__ == "__main__":
    main() 