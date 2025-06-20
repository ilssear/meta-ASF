#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Documentation Checker for SpecFirst Framework

This script validates the documentation structure against SPECIFICATIONS.md,
ensuring all required files exist and are properly formatted.
"""

import os
import sys
import logging
import argparse
from pathlib import Path
from typing import Dict, List, Set

# This is the standard, robust way to import from a subdirectory (lib)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.spec_parser import SpecParser, SpecFile, FileStatus, SUPPORTED_EXTENSIONS

# --- Main Application Class ---

class DocumentationChecker:
    def __init__(self, root_dir: str = "."):
        """Initialize the documentation checker.
        
        Args:
            root_dir: Root directory of the project (must contain SPECIFICATIONS.md).
        """
        self.root_dir = Path(root_dir)
        self.specs_file = self.root_dir / "SPECIFICATIONS.md"
        if not self.specs_file.exists():
            raise FileNotFoundError(f"SPECIFICATIONS.md not found in {root_dir}. This directory must contain SPECIFICATIONS.md.")
        
        self.docs_dir = self.root_dir / "docs"
        self.logger = logging.getLogger(__name__)

        # Data stores
        self.specified_files: Dict[str, SpecFile] = {}
        self.existing_files: Set[str] = set()
        self.missing_files: Set[str] = set()
        self.unnecessary_files: Set[str] = set()

    def parse_specifications(self) -> None:
        """Parse SPECIFICATIONS.md to extract all specified documentation files."""
        try:
            spec_parser = SpecParser(self.root_dir, self.logger)
            self.specified_files = spec_parser.parse_documentation_files()
        except Exception as e:
            self.logger.error(f"Error parsing SPECIFICATIONS.md: {e}")
            sys.exit(1)

        self.logger.debug("Parsed Files:")
        for f in sorted(self.specified_files.keys()):
            self.logger.debug(f"  - {f} ({self.specified_files[f].status.value})")

    def scan_existing_files(self) -> None:
        """Scan the docs directory for existing files with supported extensions."""
        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(SUPPORTED_EXTENSIONS):
                    rel_path = Path(root, file).relative_to(self.root_dir).as_posix()
                    self.existing_files.add(rel_path)
                    self.logger.debug(f"Found existing file: {rel_path}")

    def analyze_documentation(self) -> None:
        """Analyze documentation completeness and identify issues."""
        specified_paths = set(self.specified_files.keys())
        required_paths = {
            path for path, docfile in self.specified_files.items() 
            if docfile.status == FileStatus.REQUIRED
        }

        self.missing_files = required_paths - self.existing_files
        for file in self.missing_files:
            self.logger.error(f"Missing required file: {file}")
        
        self.unnecessary_files = self.existing_files - specified_paths
        for file in self.unnecessary_files:
            self.logger.warning(f"Unnecessary file found: {file}")

        # Update the 'exists' status for each specified file
        for path, docfile in self.specified_files.items():
            docfile.exists = path in self.existing_files

    def generate_report(self) -> str:
        """Generate a comprehensive report of the documentation status."""
        report = []
        all_specified_paths = set(self.specified_files.keys())
        optional_paths = all_specified_paths - {
            p for p, df in self.specified_files.items() if df.status == FileStatus.REQUIRED
        }

        report.append("# Documentation Analysis Report\n")
        report.append("## Summary Statistics")
        report.append(f"- Required Files: {len(all_specified_paths) - len(optional_paths)}")
        report.append(f"- Optional Files: {len(optional_paths)}")
        report.append(f"- Existing Files: {len(self.existing_files)}")
        report.append(f"- Missing Required Files: {len(self.missing_files)}")
        report.append(f"- Unnecessary Files: {len(self.unnecessary_files)}\n")

        report.append("## Directory Structure")
        all_dirs = sorted({Path(p).parent.as_posix() for p in all_specified_paths})
        for dir_path in all_dirs:
            dir_exists = (self.root_dir / dir_path).exists()
            status = "✅" if dir_exists else "❌"
            report.append(f"{status} {dir_path}/")

            files_in_dir = sorted(p for p in all_specified_paths if Path(p).parent.as_posix() == dir_path)
            for file_path in files_in_dir:
                docfile = self.specified_files[file_path]
                if docfile.status == FileStatus.OPTIONAL:
                    file_status = "✅" if docfile.exists else "⚪"
                else:
                    file_status = "✅" if docfile.exists else "❌"
                report.append(f"  {file_status} {Path(file_path).name}")
        report.append("")

        if self.missing_files:
            report.append("## Missing Required Files")
            for file in sorted(self.missing_files):
                report.append(f"- {file}")
            report.append("")

        missing_optional = sorted(p for p, df in self.specified_files.items() if df.status == FileStatus.OPTIONAL and not df.exists)
        if missing_optional:
            report.append("## Missing Optional Files")
            for file in missing_optional:
                report.append(f"- {file}")
            report.append("")

        if self.unnecessary_files:
            report.append("## Unnecessary Files")
            report.append("These files exist but are not specified in SPECIFICATIONS.md:")
            for file in sorted(self.unnecessary_files):
                report.append(f"- {file}")
            report.append("")
        
        if self.missing_files or self.unnecessary_files:
            report.append("## LLM Guidance")
            report.append(self.generate_llm_guidance())
            report.append("")

        return "\n".join(report)

    def generate_llm_guidance(self) -> str:
        """Generate a detailed content-generation prompt for an LLM."""
        if not self.missing_files and not self.unnecessary_files:
            return "**Result: All documentation files are in sync with `SPECIFICATIONS.md`. No actions required.**"

        guidance = ["# LLM Task: Synchronize Documentation Files\n"]
        
        if self.missing_files:
            guidance.append("## 📝 Plan: Create Missing Files")
            guidance.append("Based on `SPECIFICATIONS.md`, the following required files are missing. Your task is to generate the content for each file based on its specified purpose.\n")
            
            for file_path in sorted(list(self.missing_files)):
                docfile = self.specified_files.get(file_path)
                guidance.append(f"### 📄 File to Create: `{file_path}`")
                
                guidance.append("\n**Content Specification:**")
                guidance.append("- Follow instructions from `SPECIFICATIONS.md` and linked files.")
                guidance.append("\n---\n")

        if self.unnecessary_files:
            guidance.append("## 🗑️ Plan: Remove Unnecessary Files")
            guidance.append("The following files exist in the `docs/` directory but are not mentioned in `SPECIFICATIONS.md`. They should be removed.\n")
            guidance.append("```sh")
            for file in sorted(list(self.unnecessary_files)):
                guidance.append(f"rm {file}")
            guidance.append("```")

        return "\n".join(guidance)

def main():
    """Main entry point for the documentation checker."""
    parser = argparse.ArgumentParser(
        description="Check documentation against SPECIFICATIONS.md.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  # Get LLM-consumable commands to fix documentation
  python3 scripts/check_docs.py

  # Get a detailed human-readable report
  python3 scripts/check_docs.py --report

  # See verbose parsing output (for debugging)
  python3 scripts/check_docs.py --verbose
"""
    )
    parser.add_argument(
        "-v", "--verbose", 
        action="store_true", 
        help="Enable verbose logging for debugging the script itself."
    )
    parser.add_argument(
        "--report", 
        action="store_true", 
        help="Generate a detailed, human-readable report instead of LLM commands."
    )
    parser.add_argument(
        "--root-dir", 
        default=".", 
        help="Root directory of the project (default: current directory)."
    )
    args = parser.parse_args()
    
    # Configure logging based on verbosity
    log_level = logging.DEBUG if args.verbose else logging.CRITICAL + 1
    if args.report:
        log_level = logging.WARNING

    logging.basicConfig(
        level=log_level,
        format='%(levelname)s: %(message)s',
        stream=sys.stderr
    )

    try:
        checker = DocumentationChecker(root_dir=args.root_dir)
        checker.parse_specifications()
        checker.scan_existing_files()
        checker.analyze_documentation()
        
        if args.report:
            print(checker.generate_report())
        else:
            print(checker.generate_llm_guidance())
        
        if checker.missing_files and not (args.report or args.verbose):
            sys.exit(1)
        else:
            sys.exit(0)

    except FileNotFoundError as e:
        logging.getLogger(__name__).critical(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        logging.getLogger(__name__).critical(f"An unexpected error occurred: {e}", exc_info=args.verbose)
        sys.exit(1)

if __name__ == "__main__":
    main() 