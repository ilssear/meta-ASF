#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Shared validation library for the SpecFirst Framework.

This module contains common classes and functions used by various validator
scripts to parse SPECIFICATIONS.md and check for documentation completeness.
"""

import os
import logging
from pathlib import Path
from typing import Dict, List, Set

from .spec_parser import SpecParser, SpecFile, FileStatus

# --- Documentation Completeness Checker ---
class DocumentationChecker:
    """Parses SPECIFICATIONS.md and checks for documentation file completeness."""
    def __init__(self, root_dir: Path, logger: logging.Logger):
        self.root_dir = root_dir
        self.specs_file = root_dir / "SPECIFICATIONS.md"
        self.docs_dir = root_dir / "docs"
        self.logger = logger
        self.specified_files: Dict[str, SpecFile] = {}
        self.existing_files: Set[str] = set()
        self.missing_required_files: Set[str] = set()
        self.unnecessary_files: Set[str] = set()

    def run_checks(self) -> bool:
        """Runs all documentation checks and returns True if all required docs exist."""
        if not self.docs_dir.is_dir():
            self.logger.debug("Docs directory not found, skipping documentation completeness check.")
            return True # Not a failure of this component

        if not self.specs_file.is_file():
            self.logger.warning("SPECIFICATIONS.md not found, cannot check documentation completeness.")
            return False

        # First check the robustness of the specifications by validating source files
        if not self._check_specification_robustness():
            return False

        self.parse_specifications()
        self.scan_existing_files()
        self.analyze_documentation()
        return not self.missing_required_files

    def _check_specification_robustness(self) -> bool:
        """
        Check the robustness of the specifications by validating that source methodology files exist.
        
        Returns:
            True if all source files exist and are valid, False otherwise.
        """
        methodology_dir = self.root_dir / "methodology"
        if not methodology_dir.is_dir():
            self.logger.warning("methodology/ directory not found - specifications may be incomplete.")
            return False

        # Get required source files from SPECIFICATIONS.md
        try:
            spec_parser = SpecParser(self.root_dir, self.logger)
            required_source_files = spec_parser.parse_source_files()
            if not required_source_files:
                self.logger.warning("Could not parse any methodology source files from SPECIFICATIONS.md.")
                return False
        except Exception as e:
            self.logger.error(f"Failed to parse SPECIFICATIONS.md for source files: {e}")
            return False

        missing_source_files = []
        empty_source_files = []

        for file_path in required_source_files:
            full_path = self.root_dir / file_path
            if not full_path.is_file():
                missing_source_files.append(file_path)
            elif full_path.stat().st_size == 0:
                empty_source_files.append(file_path)

        if missing_source_files:
            self.logger.warning(f"Missing source methodology files: {', '.join(missing_source_files)}")
            return False

        if empty_source_files:
            self.logger.warning(f"Empty source methodology files: {', '.join(empty_source_files)}")
            return False

        self.logger.debug("✅ All source methodology files exist and are non-empty.")
        return True

    def parse_specifications(self) -> None:
        """Parse SPECIFICATIONS.md to identify required documentation files."""
        try:
            spec_parser = SpecParser(self.root_dir, self.logger)
            self.specified_files = spec_parser.parse_documentation_files()
        except Exception as e:
            self.logger.error(f"Failed to parse SPECIFICATIONS.md: {e}")
            self.specified_files = {}

    def scan_existing_files(self) -> None:
        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(('.md', '.py', '.yaml', '.json', '.template')):
                    rel_path = Path(root, file).relative_to(self.root_dir).as_posix()
                    self.existing_files.add(rel_path)

    def analyze_documentation(self) -> None:
        specified_paths = set(self.specified_files.keys())
        required_paths = {p for p, df in self.specified_files.items() if df.status == FileStatus.REQUIRED}
        
        self.logger.debug(f"--- Documentation Analysis ---")
        self.logger.debug(f"{len(required_paths)} required files specified:")
        for p in sorted(list(required_paths)):
            self.logger.debug(f"  - {p}")
        
        self.logger.debug(f"{len(self.existing_files)} existing files found in docs/:")
        for p in sorted(list(self.existing_files)):
            self.logger.debug(f"  - {p}")

        self.missing_required_files = required_paths - self.existing_files
        self.unnecessary_files = self.existing_files - specified_paths

        self.logger.debug(f"{len(self.missing_required_files)} missing required files calculated.")
        self.logger.debug(f"-----------------------------") 