# Scripts Directory

## Overview
This directory contains validation and utility scripts for the SpecFirst framework. These scripts ensure project compliance with the framework's specifications and provide guidance for project development.

## Scripts

### 1. validate_project.py
**Purpose**: Determines the overall project development stage and provides a clear status for CI/CD pipelines and quality assurance.

**Usage**:
```bash
# Validate current directory
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
- Analyzes documentation completeness
- Provides actionable next steps
- Supports verbose debugging output

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
- Parses SPECIFICATIONS.md for required documentation files
- Scans docs/ directory for existing files
- Identifies missing required files
- Flags unnecessary files not in specifications
- Generates LLM-consumable guidance for fixing issues
- Provides detailed human-readable reports

**Output Formats**:
- **Default**: LLM guidance for fixing documentation issues
- **--report**: Detailed human-readable analysis report
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
- Validates documentation structure against SPECIFICATIONS.md
- Provides clear error reporting
- Returns appropriate exit codes for automation

## Library Modules

### lib/framework_validator.py
**Purpose**: Core validation logic for the framework.

**Key Components**:
- `DocumentationChecker`: Main class for documentation validation
- File existence and content validation
- Cross-reference validation
- Quality assessment functions

### lib/spec_parser.py
**Purpose**: Parses SPECIFICATIONS.md to extract file requirements and structure.

**Key Components**:
- `SpecParser`: Main parsing class
- `SpecFile`: Data structure for file specifications
- `FileStatus`: Enum for file status (REQUIRED, OPTIONAL)
- Documentation file parsing
- Source file parsing
- Cross-reference validation

**Supported Extensions**:
- `.md` (Markdown files)
- `.py` (Python files)
- `.json` (JSON files)
- `.yaml`, `.yml` (YAML files)
- `.txt` (Text files)

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

# Get detailed report
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
- `logging`: Logging and debugging output
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
from lib.spec_parser import SpecParser
```

## Error Handling

### Common Error Scenarios
1. **Missing SPECIFICATIONS.md**: Scripts will exit with error if not found
2. **Malformed SPECIFICATIONS.md**: Parsing errors will be reported
3. **Missing directories**: Required directories must exist
4. **Empty directories**: Required directories must not be empty
5. **File permission issues**: Scripts will report access errors

### Exit Codes
- **0**: Success (all checks passed)
- **1**: Error (validation failed or script error)
- **2**: Usage error (invalid arguments)

## Integration with Framework

### Validation Workflow
1. **validate_project.py**: Determine overall project stage
2. **check_docs.py**: Identify specific documentation issues
3. **check_structure.py**: Validate structural requirements
4. **Manual fixes**: Address identified issues
5. **Re-run validation**: Confirm fixes resolved issues

### Framework Compliance
- Scripts enforce framework specifications
- Ensure documentation completeness
- Validate project structure
- Provide guidance for compliance
- Support automated validation

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