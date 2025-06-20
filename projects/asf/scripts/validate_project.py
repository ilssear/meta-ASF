#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Comprehensive Project Validator for the SpecFirst Framework.

This script analyzes a project's structure and content to determine its current
stage of development (e.g., "Ready to Generate", "In Progress", "Complete").
It consolidates checks for core file structure and documentation completeness
to provide a single, authoritative validation status.
"""

import sys
import argparse
import logging
from pathlib import Path
from typing import Set, List
import re

# This is the standard, robust way to import from a subdirectory (lib)
# It adds the script's own directory to the path, allowing the import.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.framework_validator import DocumentationChecker
from lib.spec_parser import SpecParser


# --- Main Project Validator ---
class ProjectValidator:
    """Orchestrates validation checks to determine project stage."""

    def __init__(self, root_dir: str, verbose: bool = False):
        self.root_dir = Path(root_dir).resolve()
        self.verbose = verbose
        
        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(level=log_level, format='%(message)s', stream=sys.stdout)
        self.logger = logging.getLogger(__name__)

        # Granular check results
        self.has_spec_txt = False
        self.has_spec_md = False
        self.readme_ok = False
        self.rules_ok = False
        self.docs_dir_ok = False
        self.scripts_dir_ok = False
        self.docs_complete = False
        self.unnecessary_docs: Set[str] = set()
        self.source_files_ok = False

    def run(self) -> None:
        """Run all validation checks and print a final report."""
        self.has_spec_txt = (self.root_dir / "specifications.txt").is_file()
        self.has_spec_md = (self.root_dir / "SPECIFICATIONS.md").is_file()

        if not self.has_spec_txt and not self.has_spec_md:
            self.logger.error("🚫 Not a SpecFirst project: Neither specifications.txt nor SPECIFICATIONS.md found.")
            sys.exit(1)

        self._check_core_structure()
        
        # Check source files if SPECIFICATIONS.md exists
        if self.has_spec_md:
            self.source_files_ok = self._check_source_files()

        if self.has_spec_md:
            doc_checker = DocumentationChecker(self.root_dir, self.logger)
            self.docs_complete = doc_checker.run_checks()
            self.unnecessary_docs = doc_checker.unnecessary_files
        
        self._print_report()

    def _check_source_files(self) -> bool:
        """Check that all required source files exist based on SPECIFICATIONS.md."""
        try:
            spec_parser = SpecParser(self.root_dir, self.logger)
            required_files = spec_parser.parse_source_files()
            if not required_files:
                self.logger.warning("Could not parse required source files from SPECIFICATIONS.md.")
                return False
        except Exception as e:
            self.logger.error(f"Failed to parse SPECIFICATIONS.md for source files: {e}")
            return False

        missing_files = []
        for file_path in required_files:
            full_path = self.root_dir / file_path
            if not full_path.is_file():
                missing_files.append(file_path)

        if missing_files:
            self.logger.warning(f"Missing required source files: {', '.join(missing_files)}")
            return False

        self.logger.debug("✅ All required source files exist.")
        return True

    def _check_core_structure(self) -> None:
        """Check for core files like README, .cursorrules, and docs/scripts directories."""
        self.logger.debug(f"--- Core Structure Check ---")
        self.logger.debug(f"Project Root: {self.root_dir}")

        # Files in the project root
        self.readme_ok = (self.root_dir / "README.md").is_file()
        self.logger.debug(f"Checking for README.md in project root: {'Found' if self.readme_ok else 'Missing'}")

        self.rules_ok = (self.root_dir / ".cursorrules").is_file()
        self.logger.debug(f"Checking for .cursorrules in project root: {'Found' if self.rules_ok else 'Missing'}")

        # Directories within the project root
        self.docs_dir_ok = (self.root_dir / "docs").is_dir()
        self.logger.debug(f"Checking for docs/ dir in project: {'Found' if self.docs_dir_ok else 'Missing'}")

        self.scripts_dir_ok = (self.root_dir / "scripts").is_dir()
        self.logger.debug(f"Checking for scripts/ dir in project: {'Found' if self.scripts_dir_ok else 'Missing'}")
        self.logger.debug(f"--------------------------")

    def _print_report(self) -> None:
        """Analyzes check results and prints a report on the project stage."""
        stage = "Unknown"
        messages = []

        # Stage 1: Initial idea, needs spec refinement
        if not self.has_spec_md and self.has_spec_txt:
            stage = "1. Ready for Refinement"
            messages.append("- Initial `specifications.txt` is present.")
            messages.append("- Next Step: Refine it into a formal `SPECIFICATIONS.md`.")
        
        # Stage 2: Spec exists, but basic dirs (docs/scripts) are missing
        elif self.has_spec_md and self.source_files_ok and not (self.docs_dir_ok and self.scripts_dir_ok):
            stage = "2. Ready to Generate"
            messages.append("- `SPECIFICATIONS.md` is present.")
            messages.append("- All required source files exist.")
            messages.append("- Core directories (`docs/`, `scripts/`) are missing.")
            messages.append("- Next Step: Generate the core project structure.")

        # Stage 2b: Spec exists but source files are missing
        elif self.has_spec_md and not self.source_files_ok:
            stage = "2. Incomplete Source Files"
            messages.append("- `SPECIFICATIONS.md` is present.")
            messages.append("- One or more required source files are missing.")
            messages.append("- Next Step: Create missing source files before generation.")

        # Stage 3: Core dirs exist, but docs are incomplete
        elif self.has_spec_md and not self.docs_complete:
            stage = "3. In Progress / Generating Required Docs"
            messages.append("- Core structure is in place.")
            messages.append("- One or more REQUIRED documentation files are missing from `docs/`.")
            messages.append("- Next Step: Run `check_docs.py` to get guidance on generating the missing files.")

        # Stage 4: Docs are complete, but final artifacts (README/rules) are missing
        elif self.has_spec_md and self.docs_complete and not (self.readme_ok and self.rules_ok):
            stage = "4. Ready for Finalization"
            messages.append("- All required documentation has been generated.")
            if not self.readme_ok:
                messages.append("- Workspace `README.md` is missing.")
            if not self.rules_ok:
                messages.append("- Workspace `.cursorrules` is missing.")
            messages.append("- Next Step: Generate the final project artifacts.")
        
        # Stage 5 & 6: Project is complete, possibly with warnings
        elif self.has_spec_md and self.docs_complete and self.readme_ok and self.rules_ok:
            if self.unnecessary_docs:
                stage = "5. Complete (with Warnings)"
                messages.append("- All required files and documentation are present.")
                messages.append(f"- Found {len(self.unnecessary_docs)} unnecessary files in `docs/`.")
                if self.verbose:
                    for f in sorted(list(self.unnecessary_docs)): messages.append(f"  - {f}")
            else:
                stage = "6. Complete and Valid"
                messages.append("- All structural and documentation requirements are met perfectly.")
        
        print("-" * 40)
        print(f"Project Stage: {stage}")
        print("-" * 40)
        for msg in messages:
            print(msg)
        print("-" * 40)

def main():
    parser = argparse.ArgumentParser(description="Validates the project's stage based on SpecFirst rules.")
    parser.add_argument("--root-dir", default=".", help="Project root directory.")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output.")
    args = parser.parse_args()

    try:
        validator = ProjectValidator(root_dir=args.root_dir, verbose=args.verbose)
        validator.run()
    except Exception as e:
        logging.getLogger(__name__).critical(f"An unexpected error occurred: {e}", exc_info=args.verbose)
        sys.exit(1)

if __name__ == "__main__":
    main() 