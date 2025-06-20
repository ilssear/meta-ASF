#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Project Structure Checker for SpecFirst Framework

This script validates that the essential files and directories required by the
SpecFirst framework exist at the project root. It is intended as a high-level
check to be run before more detailed validators like check_docs.py.
"""

import os
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any
import re

# This is the standard, robust way to import from a subdirectory (lib)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.spec_parser import SpecParser

# --- Configuration ---

# Files that MUST exist at the project root.
REQUIRED_FILES: List[str] = [
    "README.md",
    ".cursorrules",
    "SPECIFICATIONS.md",
]

# Directories that MUST exist at the project root.
# `check_empty`: if True, the script will fail if the directory is empty.
REQUIRED_DIRS: Dict[str, Dict[str, Any]] = {
    "docs": {"check_empty": True},
    "scripts": {"check_empty": True},
}

# --- Checker Class ---

class StructureChecker:
    """Checks for the presence of required files and directories."""

    def __init__(self, root_dir: str):
        """
        Initialize the checker.
        
        Args:
            root_dir: The root directory of the project to check.
        """
        self.root_dir = Path(root_dir).resolve()
        self.errors: List[str] = []
        self.successes: List[str] = []

    def run_checks(self) -> None:
        """Execute all configured file and directory checks."""
        print(f"🔍 Checking project structure at: {self.root_dir}\n")
        self._check_files()
        self._check_directories()
        self._check_doc_structure()

    def _check_files(self) -> None:
        """Check for the existence of all required files."""
        for file_name in REQUIRED_FILES:
            file_path = self.root_dir / file_name
            if file_path.is_file():
                self.successes.append(f"✅ Found required file: {file_name}")
            else:
                self.errors.append(f"❌ Missing required file: {file_name}")

    def _check_directories(self) -> None:
        """Check for the existence and content of all required directories."""
        for dir_name, config in REQUIRED_DIRS.items():
            dir_path = self.root_dir / dir_name
            if not dir_path.is_dir():
                self.errors.append(f"❌ Missing required directory: {dir_name}/")
                continue

            self.successes.append(f"✅ Found required directory: {dir_name}/")

            if config.get("check_empty", False):
                if not any(dir_path.iterdir()):
                    self.errors.append(f"    - ❌ Directory is empty: {dir_name}/")
                else:
                    self.successes.append(f"    - ✅ Directory is not empty: {dir_name}/")
    
    def get_required_doc_files(self) -> List[str]:
        """
        Parses SPECIFICATIONS.md to find all files marked as (REQUIRED).
        
        Returns:
            A list of required file paths relative to the project root.
        """
        spec_path = self.root_dir / "SPECIFICATIONS.md"
        if not spec_path.is_file():
            self.errors.append("❌ SPECIFICATIONS.md not found, cannot check doc structure.")
            return []

        try:
            spec_parser = SpecParser(self.root_dir)
            specified_files = spec_parser.parse_documentation_files()
            
            # Extract only required files
            required_files = [
                file_path for file_path, spec_file in specified_files.items()
                if spec_file.status.value == "REQUIRED"
            ]
            
            return required_files
        except Exception as e:
            self.errors.append(f"❌ Failed to parse SPECIFICATIONS.md: {e}")
            return []

    def _check_doc_structure(self):
        """
        Validates that the documentation structure defined in SPECIFICATIONS.md exists.
        """
        required_files = self.get_required_doc_files()
        if not required_files:
            return # Errors already logged by get_required_doc_files

        self.successes.append("\n📄 Checking documentation structure based on SPECIFICATIONS.md...")

        for doc_file_path in required_files:
            full_path = self.root_dir / doc_file_path
            if full_path.is_file():
                self.successes.append(f"    - ✅ Found required doc file: {doc_file_path}")
            else:
                self.errors.append(f"    - ❌ Missing required doc file: {doc_file_path}")

    def print_report(self) -> int:
        """
        Print a summary of the checks to the console.
        
        Returns:
            An exit code (0 for success, 1 for failure).
        """
        for msg in self.successes:
            print(msg)
        
        if self.errors:
            print("\n" + "-"*20 + "\n")
            print("🚨 Found errors:\n")
            for error in self.errors:
                print(error)
            print(f"\n🚫 Project structure is INVALID.")
            return 1
        
        print("\n🎉 Project structure is VALID.")
        return 0

# --- Main Execution ---

def main():
    """Main entry point for the structure checker script."""
    parser = argparse.ArgumentParser(
        description="Check for essential SpecFirst project files and directories.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "--root-dir", 
        default=".", 
        help="Root directory of the project to check (default: current directory)."
    )
    args = parser.parse_args()

    try:
        if not Path(args.root_dir).is_dir():
            raise FileNotFoundError(f"The specified root directory does not exist: {args.root_dir}")
        
        checker = StructureChecker(root_dir=args.root_dir)
        checker.run_checks()
        exit_code = checker.print_report()
        sys.exit(exit_code)

    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main() 