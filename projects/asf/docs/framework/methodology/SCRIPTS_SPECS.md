# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Specifications for Framework Scripts

This document defines the functional and operational requirements for the validation and maintenance scripts located in the `scripts/` directory. These scripts are essential for enforcing the standards of the Agile SpecFirst Development Framework.

## 1. Core Principles
- **Source of Truth**: All validation logic MUST be derived from `SPECIFICATIONS.md`. The scripts should parse the specifications to determine required files, not have them hard-coded (unless the script's purpose is to check for `SPECIFICATIONS.md` itself).
- **Clear Output**: Scripts MUST produce clear, human-readable output that indicates the project's status and provides actionable guidance for fixing errors.
- **CI/CD Integration**: Scripts MUST be runnable from the command line and use exit codes to signal success (0) or failure (non-zero), making them suitable for use in CI/CD pipelines.

## 2. Script Definitions

### 2.1. `validate_project.py` - Primary Project Validator
This script acts as the main quality gate for the project. It consolidates information from other checks to provide a holistic view of the project's development stage.

**Functional Requirements:**
- **Entry Point**: Serves as the primary, high-level validation script.
- **Stage Analysis**: Determines and reports the project's current development stage (e.g., "1. Ready for Refinement", "3. In Progress", "6. Complete and Valid").
- **Core File Check**: Verifies the presence of `SPECIFICATIONS.md` and/or `specifications.txt` to confirm it's a SpecFirst project.
- **Documentation Check**: Integrates the logic from `lib/framework_validator.py` to determine if all `(REQUIRED)` documentation files are present.
- **Final Artifacts Check**: Verifies the presence of the final generated artifacts in the project root: `README.md` and `.cursorrules`.
- **Command-Line Interface**: MUST accept a `--root-dir` argument to specify the project root and a `--verbose` flag for detailed logging.

### 2.2. `check_docs.py` - Detailed Documentation Checker
This script provides a granular analysis of the `docs/` directory against the requirements in `SPECIFICATIONS.md`.

**Functional Requirements:**
- **Specification Parsing**: MUST parse the "Documentation Generation" section of `SPECIFICATIONS.md` to build a list of all required and optional files.
- **File Validation**:
    - Reports a list of all `(REQUIRED)` files that are missing.
    - Reports a list of any files found in the `docs/` directory that are not specified in the documentation plan (unnecessary files).
- **Guidance Generation**: Includes logic to generate LLM-ready guidance for creating the content of missing files.
- **Command-Line Interface**: MUST accept a `--root-dir` argument.

### 2.3. `check_structure.py` - Basic Structure Checker
This script performs a quick, high-level check for the most essential files and directories at the project root.

**Functional Requirements:**
- **File Check**: Verifies the existence of `README.md`, `.cursorrules`, and `SPECIFICATIONS.md`.
- **Directory Check**: Verifies the existence of the `docs/` and `scripts/` directories and ensures they are not empty.
- **Simple Output**: Provides a clean, pass/fail report on the basic structure.
- **Command-Line Interface**: MUST accept a `--root-dir` argument.

### 2.4. `lib/framework_validator.py` - Shared Validation Library
This is not a standalone script, but a Python module containing reusable validation logic to be used by the other scripts.

**Functional Requirements:**
- **Modularity**: Contains classes and functions that encapsulate common validation tasks.
- **`DocumentationChecker` Class**:
    - **Initialization**: Takes a project root path and a logger instance.
    - **Specification Parsing**: Contains the logic to read `SPECIFICATIONS.md` and extract the file requirements.
    - **File Checking**: Implements the core logic for comparing the required file list against the actual files on disk.
    - **Results**: Makes the lists of missing and unnecessary files available for other scripts to use.
- **Single Source of Logic**: Prevents duplication of the specification parsing logic across multiple scripts. 