# Scripts Directory

## Overview
This directory contains validation and utility scripts for the SpecFirst framework. These scripts ensure project compliance with the framework's specifications and provide guidance for project development.

## Semantic Parsing (2025+)
All scripts now use a robust, semantic parser (`lib/semantic_parser.py`) that:
- Understands the hierarchical, path-hinted structure of SPECIFICATIONS.md
- Handles any numbering (including zero-padded and multi-digit)
- Properly manages directory stacks and indentation
- Ignores description lines and invalid sections
- Does not rely on hard-coded mappings
- Only processes files/directories within valid sections
- Supports all file types including `.py`, `.md`, `.json`, `.yaml`, `.template`, etc.

## Professional Logging Standards
All scripts now use professional, standards-compliant logging:
- **Standard levels**: `ERROR`, `WARNING`, `DEBUG`, `INFO`
- **Text-based status indicators**: `[EXISTS]`, `[MISSING]`, `[OPTIONAL]`, `[FAILED]`, `[SUCCESS]`
- **No emojis in logs** - clean, professional output suitable for CI/CD
- **User-friendly reports** available with `--report` flag when needed

## Quick LLM/Cursor Usage Examples

- **Validate project stage:**
  ```bash
  python projects/asf/scripts/validate_project.py --root-dir projects/asf
  ```
- **Check documentation:**
  ```bash
  python projects/asf/scripts/check_docs.py --root-dir projects/asf
  ```
- **Human-readable docs report:**
  ```bash
  python projects/asf/scripts/check_docs.py --root-dir projects/asf --report
  ```
- **Verbose/debugging output:**
  ```bash
  python projects/asf/scripts/validate_project.py --root-dir projects/asf -v
  python projects/asf/scripts/check_docs.py --root-dir projects/asf -v
  ```
- **Create deployment package:**
  ```bash
  python projects/asf/scripts/deploy_package.py --root-dir projects/asf
  ```

## Script Descriptions

### validate_project.py
Determines the overall project development stage and provides a clear status for CI/CD pipelines and quality assurance.

### check_docs.py
Validates documentation completeness and identifies missing or inconsistent files using the semantic parser.

### check_structure.py
Validates project structure integrity and ensures alignment with specifications.

### deploy_package.py
**Purpose**: Packages only generated files for deployment. See above for details.

## Library Modules

### lib/semantic_parser.py
**Purpose**: Semantic parsing of SPECIFICATIONS.md for all scripts.
- Supports all file extensions: `.md`, `.py`, `.json`, `.yaml`, `.yml`, `.txt`, `.template`
- Robust error handling and validation
- See docstring in the file for details.

### lib/framework_validator.py
**Purpose**: Core validation logic for the framework.
- Uses the semantic parser for all file and structure checks
- Properly updates file existence status
- Professional logging and error handling

## Testing Framework

### Test Structure
- **Unit tests**: `tests/unit/` - Individual component testing
- **Integration tests**: `tests/integration/` - Script workflow testing  
- **End-to-end tests**: `tests/e2e/` - Complete workflow validation
- **Configuration**: `pytest.ini` - Test configuration with coverage reporting
- **Fixtures**: `tests/conftest.py` - Shared test fixtures and marker registration

### Test Coverage
- **100% test pass rate** (34/34 tests)
- **Zero warnings** - All pytest configuration issues resolved
- **Professional logging** - No emoji-based output in tests
- **Comprehensive validation** - All scripts and parser functionality tested

### Running Tests
```bash
# Run all tests
python -m pytest scripts/tests/ -v

# Run specific test types
python -m pytest scripts/tests/unit/ -v
python -m pytest scripts/tests/integration/ -v
python -m pytest scripts/tests/e2e/ -v

# Run with coverage
python -m pytest scripts/tests/ -v --cov=lib --cov=validate_project --cov=check_docs --cov=check_structure
```

## TDD and SpecFirst
- All scripts and the parser are tested using unit tests (see `test_semantic_parser.py`)
- The parser is designed for reusability and extensibility for future SpecFirst projects
- Tests follow TDD principles with comprehensive coverage

## Error Handling
- All scripts provide clear error messages and exit codes
- Professional logging standards throughout
- Use `-v` for debugging output if needed
- Graceful handling of malformed specifications

## Integration
- All validation and documentation scripts now use the semantic parser for robust, future-proof compliance checking
- Professional output suitable for CI/CD pipelines
- Consistent error handling and status reporting

## Scripts

### 1. validate_project.py
**Purpose**: Determines the overall project development stage and provides a clear status for CI/CD pipelines and quality assurance.

**Usage**:
```bash
# Validate current directory (defaults to current directory)
python scripts/validate_project.py

# Validate specific directory
python scripts/validate_project.py --root-dir /path/to/project

# Verbose output
python scripts/validate_project.py --verbose
```

**Project Stages**:
1. **Stage 1**: Ready for Refinement (specifications.txt exists, needs SPECIFICATIONS.md)
2. **Stage 2**: Ready to Generate (SPECIFICATIONS.md exists, core directories missing)
3. **Stage 3**: In Progress / Generating Required Docs (core structure exists, docs incomplete)
4. **Stage 4**: Ready for Finalization (docs complete, final artifacts missing)
5. **Stage 5**: Complete (with warnings about unnecessary files)
6. **Stage 6**: Complete and Valid (all requirements met perfectly)

**Key Features**:
- Checks for SPECIFICATIONS.md and specifications.txt
- Validates core directory structure (docs/, scripts/)
- Analyzes documentation completeness using semantic parser
- Provides actionable next steps
- Supports verbose debugging output
- Professional logging standards

### 2. check_docs.py
**Purpose**: Validates documentation completeness and identifies missing or inconsistent files.

**Usage**:
```bash
# Check documentation in current directory
python scripts/check_docs.py

# Check documentation in specific directory
python scripts/check_docs.py --root-dir /path/to/project

# Generate detailed report
python scripts/check_docs.py --report

# Verbose output for debugging
python scripts/check_docs.py --verbose
```

**Key Features**:
- Parses SPECIFICATIONS.md for required documentation files using semantic parser
- Scans docs/ directory for existing files (supports all extensions)
- Identifies missing required files
- Flags unnecessary files not in specifications
- Generates LLM-consumable guidance for fixing issues
- Provides detailed human-readable reports
- Professional logging and status indicators

**Output Formats**:
- **Default**: LLM guidance for fixing documentation issues
- **--report**: Detailed human-readable analysis report with `[EXISTS]`/`[MISSING]` status
- **--verbose**: Debug information about parsing and file discovery

### 3. check_structure.py
**Purpose**: Validates project structure integrity and ensures alignment with specifications.

**Usage**:
```bash
# Check structure in current directory
python scripts/check_structure.py

# Check structure in specific directory
python scripts/check_structure.py --root-dir /path/to/project
```

**Key Features**:
- Validates required files exist (README.md, .cursorrules, SPECIFICATIONS.md)
- Checks required directories exist and are not empty (docs/, scripts/)
- Validates documentation structure against SPECIFICATIONS.md using semantic parser
- Provides clear error reporting with professional status indicators
- Returns appropriate exit codes for automation

### 4. deploy_package.py
**Purpose**: Packages only generated files for deployment. See above for details.

## Common Usage Patterns

### 1. Project Status Check
```bash
# Quick status check
python scripts/validate_project.py

# If Stage 3 or below, check what's missing
python scripts/check_docs.py
```

### 2. Documentation Validation
```bash
# Get LLM guidance for missing files
python scripts/check_docs.py

# Get detailed report with professional status indicators
python scripts/check_docs.py --report
```

### 3. Structure Validation
```bash
# Validate project structure
python scripts/check_structure.py
```

### 4. CI/CD Integration
```bash
# Use in CI/CD pipeline
python scripts/validate_project.py --root-dir /path/to/project
if [ $? -eq 0 ]; then
    echo "Project validation passed"
else
    echo "Project validation failed"
    exit 1
fi
```

## Script Dependencies

### Required Files
- `SPECIFICATIONS.md`: Must exist in project root
- `docs/` directory: Must exist for documentation validation
- `scripts/` directory: Must exist and contain validation scripts

### Python Dependencies
- `pathlib`: Path manipulation (Python 3.4+)
- `argparse`: Command-line argument parsing
- `logging`: Professional logging and debugging output
- `re`: Regular expressions for parsing
- `sys`: System-specific parameters
- `os`: File system operations

### Import Structure
All scripts use the following pattern to import from the lib directory:
```python
import sys
from pathlib import Path

# Add script directory to path for lib imports
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib.framework_validator import DocumentationChecker
from lib.semantic_parser import SemanticSpecParser
```

## Best Practices

### Running Scripts
- Always run from project root directory
- Use `--root-dir` for non-standard locations
- Use `--verbose` for debugging issues
- Check exit codes for automation

### Interpreting Results
- **Stage 1-2**: Focus on specification refinement
- **Stage 3**: Focus on documentation generation
- **Stage 4**: Focus on final artifacts
- **Stage 5-6**: Focus on cleanup and optimization

### Automation
- Use in CI/CD pipelines
- Check exit codes for pass/fail
- Parse output for specific issues
- Integrate with development workflow

### Use deploy_package.py to create deployment packages for release
Only generated files (docs/, README.md, .cursorrules, LICENSE) are included in the deployment package.

## Troubleshooting

### Common Issues
1. **Import errors**: Ensure lib/ directory exists and contains required modules
2. **Path issues**: Use absolute paths or ensure correct working directory
3. **Permission errors**: Check file and directory permissions
4. **Parsing errors**: Validate SPECIFICATIONS.md format

### Debugging
- Use `--verbose` flag for detailed output
- Check script logs for specific error messages
- Validate SPECIFICATIONS.md manually
- Test with minimal project structure

## References
- [SPECIFICATIONS.md](../SPECIFICATIONS.md) - Project specifications
- [SCRIPTS_SPECS.md](../docs/framework/methodology/SCRIPTS_SPECS.md) - Script specifications
- [AGILE_SPECFIRST.md](../docs/framework/methodology/AGILE_SPECFIRST.md) - Core methodology 

## Deployment Packaging

### deploy_package.py
**Purpose**: Creates a deployment package (zip file) containing only generated files from the project, suitable for distribution or deployment. It includes:
- docs/ (all generated documentation)
- README.md (project interface)
- .cursorrules (AI/implementation guide)
- LICENSE (GPL 3.0, copied from defaults/gpl-3.0.txt if needed)

**Usage**:
```bash
# Create deployment package from current directory
python scripts/deploy_package.py

# Specify project root
python scripts/deploy_package.py --root-dir /path/to/project

# Custom package name
python scripts/deploy_package.py --package-name my_deployment

# Verbose output (shows logging)
python scripts/deploy_package.py --verbose
```

**Features**:
- Only includes generated files (no source/spec files)
- Uses professional logging (INFO, ERROR, etc.)
- Fully tested (unit/integration)
- Fails if required files are missing
- Suitable for CI/CD and manual use 