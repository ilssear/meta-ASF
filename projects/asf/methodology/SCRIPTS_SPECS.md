# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Scripts Specification

## Overview
This document defines the functional requirements for all validation scripts in the SpecFirst framework. It ensures that scripts can be regenerated from clear specifications and maintain consistency across the framework.

## Purpose
The validation scripts serve as quality gates for the SpecFirst methodology, ensuring that projects meet specification requirements and maintain documentation standards.

## Semantic Parser (2025+)
All scripts now use a robust, semantic parser (`lib/semantic_parser.py`) that:
- Understands the hierarchical, path-hinted structure of SPECIFICATIONS.md
- Handles any numbering (including zero-padded and multi-digit)
- Properly manages directory stacks and indentation
- Ignores description lines and invalid sections
- Does not rely on hard-coded mappings
- Only processes files/directories within valid sections
- Supports all file extensions: `.md`, `.py`, `.json`, `.yaml`, `.yml`, `.txt`, `.template`

## Professional Logging Standards
All scripts implement professional, standards-compliant logging:
- **Standard levels**: `ERROR`, `WARNING`, `DEBUG`, `INFO`
- **Text-based status indicators**: `[EXISTS]`, `[MISSING]`, `[OPTIONAL]`, `[FAILED]`, `[SUCCESS]`
- **No emojis in logs** - clean, professional output suitable for CI/CD pipelines
- **User-friendly reports** available with `--report` flag when needed
- **Consistent error handling** across all scripts

## Testing Framework
Comprehensive testing infrastructure ensures reliability:
- **Unit tests**: `tests/unit/` - Individual component testing
- **Integration tests**: `tests/integration/` - Script workflow testing  
- **End-to-end tests**: `tests/e2e/` - Complete workflow validation
- **Configuration**: `pytest.ini` - Test configuration with coverage reporting
- **Fixtures**: `tests/conftest.py` - Shared test fixtures and marker registration
- **100% test pass rate** (34/34 tests) with zero warnings

## Core Scripts

### 1. validate_project.py

#### Purpose
Determines the overall project development stage and provides a clear status for CI/CD pipelines and quality assurance.

#### LLM/Cursor Usage
```bash
# From the workspace root:
python projects/asf/scripts/validate_project.py --root-dir projects/asf

# For verbose/debugging output:
python projects/asf/scripts/validate_project.py --root-dir projects/asf -v
```

#### Functional Requirements
- **Input**: Project root directory containing SPECIFICATIONS.md
- **Output**: Project stage (1-6) with detailed status information
- **Processing**: Analyze project structure and documentation completeness using semantic parser
- **Logging**: Professional standards-compliant output

#### Project Stages
1. **Stage 1**: Ready for Refinement (specifications.txt exists, needs SPECIFICATIONS.md)
2. **Stage 2**: Ready to Generate (SPECIFICATIONS.md exists, core directories missing)
3. **Stage 3**: In Progress / Generating Required Docs (core structure exists, docs incomplete)
4. **Stage 4**: Ready for Finalization (docs complete, final artifacts missing)
5. **Stage 5**: Complete (with warnings about unnecessary files)
6. **Stage 6**: Complete and Valid (all requirements met perfectly)

#### Validation Logic
- Check for SPECIFICATIONS.md existence
- Validate required source files from specifications using semantic parser
- Check core directory structure (docs/, scripts/)
- Verify documentation completeness
- Assess implementation status

#### Error Handling
- Clear error messages for missing files
- Detailed status information with professional indicators
- Actionable next steps
- Graceful handling of malformed specifications

#### Output Format
```
----------------------------------------
Project Stage: [Stage Number]. [Stage Name]
----------------------------------------
- [Status message 1]
- [Status message 2]
- [Status message 3]
- Next Step: [Actionable next step]
----------------------------------------
```

### 2. check_docs.py

#### Purpose
Validates documentation completeness and identifies missing or inconsistent files using semantic parsing.

#### LLM/Cursor Usage
```bash
# From the workspace root:
python projects/asf/scripts/check_docs.py --root-dir projects/asf

# For a detailed human-readable report:
python projects/asf/scripts/check_docs.py --root-dir projects/asf --report

# For verbose/debugging output:
python projects/asf/scripts/check_docs.py --root-dir projects/asf -v
```

#### Functional Requirements
- **Input**: Project root directory and SPECIFICATIONS.md
- **Output**: Detailed list of missing files and content requirements
- **Processing**: Parse specifications using semantic parser and compare with existing documentation
- **File Support**: All extensions including `.py`, `.md`, `.json`, `.yaml`, `.template`

#### Validation Areas
- Required documentation files (parsed semantically)
- Template files with proper extension support
- Cross-references
- Content completeness
- File structure alignment

#### Content Analysis
- Parse SPECIFICATIONS.md for required files using semantic parser
- Check file existence and content with proper extension support
- Validate copyright headers
- Verify cross-references
- Assess content quality

#### Output Format
```
# LLM Task: Synchronize Documentation Files

## Plan: Create Missing Files
Based on `SPECIFICATIONS.md`, the following required files are missing...

### File to Create: [file_path]

**Content Specification:**
- [Content details from specifications]

**Required Content:**
- Copyright header (if applicable)
- Brief introduction
- Content addressing specification points
```

#### Error Handling
- Identify missing files with specific paths
- Provide content requirements for each file
- Suggest generation strategies
- Handle malformed specifications gracefully
- Professional status indicators in reports

### 3. check_structure.py

#### Purpose
Validates project structure integrity and ensures alignment with specifications using semantic parsing.

#### LLM/Cursor Usage
```bash
# From the workspace root:
python projects/asf/scripts/check_structure.py --root-dir projects/asf
```

#### Functional Requirements
- **Input**: Project root directory
- **Output**: Structure validation results with detailed error reporting
- **Processing**: Check directory structure and file organization using semantic parser
- **Logging**: Professional standards-compliant output

#### Structure Validation
- Required directories exist
- Required files present (parsed from semantic structure)
- Directory hierarchy correct
- File naming conventions
- Path relationships

#### Validation Rules
- SPECIFICATIONS.md must exist in project root
- scripts/ directory must exist and contain validation scripts
- docs/ directory structure must match semantic specifications
- All required files must be present
- Cross-references must be valid

#### Output Format
```
Checking project structure at: [path]

[EXISTS] Found required file: [file_name]
[EXISTS] Found required directory: [dir_name]
    - [EXISTS] Directory is not empty: [dir_name]

[INFO] Checking documentation structure based on SPECIFICATIONS.md...

--------------------

[ERROR] Found errors:

[MISSING] Missing required file: [file_name]
[MISSING] Missing required directory: [dir_name]
    - [MISSING] Missing required doc file: [file_path]

[FAILED] Project structure is INVALID.
```

#### Error Handling
- Clear identification of missing components
- Specific file and directory paths
- Actionable error messages with professional indicators
- Validation status summary

### 4. deploy_package.py

#### Purpose
Creates a deployment package (zip file) containing only generated files from the project, suitable for distribution or deployment. It includes:
- docs/ (all generated documentation)
- README.md (project interface)
- .cursorrules (AI/implementation guide)
- LICENSE (GPL 3.0, copied from defaults/gpl-3.0.txt if needed)

#### LLM/Cursor Usage
```bash
# From the workspace root:
python projects/asf/scripts/deploy_package.py --root-dir projects/asf

# For verbose/debugging output:
python projects/asf/scripts/deploy_package.py --root-dir projects/asf -v
```

#### Functional Requirements
- **Input**: Project root directory containing generated files
- **Output**: Zip file containing only generated files
- **Processing**: Validate existence of all required generated files, copy to temp dir, zip, and clean up
- **Logging**: Professional standards-compliant output
- **Testing**: Fully covered by unit and integration tests

#### Error Handling
- Fails if any required file is missing
- Logs errors and exits with non-zero code
- Provides actionable error messages

#### Output Format
- Zip file named <project>_deployment.zip (or custom name)
- Logs progress and errors using professional logging

## Script Dependencies

### Common Libraries
- `os`: File system operations
- `sys`: System-specific parameters
- `json`: JSON file processing
- `re`: Regular expressions for parsing
- `pathlib`: Path manipulation (Python 3.4+)
- `logging`: Professional logging and debugging output

### Framework Dependencies
- `lib/framework_validator.py`: Core validation logic using semantic parser
- `lib/semantic_parser.py`: Semantic specification parsing utilities
- `defaults/environment.json`: Environment configuration
- `defaults/defaults.json`: Default settings

## Semantic Parser Implementation

### Core Classes
- `SemanticSpecParser`: Main parser class for semantic understanding
- `FileSpec`: Data structure for file specifications with status
- `FileStatus`: Enum for file status (REQUIRED, OPTIONAL)
- `Section`: Data structure for documentation sections

### Parsing Features
- Section header parsing: `N. Section Name (path_hint)`
- Directory stack management with indentation
- File entry parsing: `- filename.ext (STATUS)`
- Description line filtering: `* description`
- Path hint resolution for proper file location
- Comprehensive file extension support

### Supported Extensions
- `.md` (Markdown files)
- `.py` (Python files)
- `.json` (JSON files)
- `.yaml`, `.yml` (YAML files)
- `.txt` (Text files)
- `.template` (Template files)
- `.html` (HTML files)
- `.css` (CSS files)
- `.js` (JavaScript files)
- `.rst` (reStructuredText files)

## Quality Standards

### Code Quality
- Comprehensive error handling
- Clear, descriptive variable names
- Proper documentation and comments
- Consistent code style (PEP 8)
- Type hints for function parameters
- TDD approach with unit tests
- Professional logging standards

### Performance Requirements
- Fast execution (< 10 seconds for typical projects)
- Minimal memory usage
- Efficient file system operations
- Optimized semantic parsing algorithms

### Reliability
- Graceful handling of missing files
- Robust error recovery
- Consistent output formats
- Cross-platform compatibility
- Version control friendly
- Semantic understanding of specification structure
- Professional logging throughout

## Integration Requirements

### CI/CD Integration
- Exit codes for automation
- Structured output for parsing
- Clear success/failure indicators
- Detailed logging capabilities
- Configuration file support
- Professional output standards

### IDE Integration
- Real-time validation feedback
- Quick status checks
- Error highlighting
- Actionable suggestions
- Progress indicators

### LLM/Cursor Integration
- Clear usage examples in docstrings
- Standardized command patterns
- Verbose output for debugging
- Human-readable reports
- Consistent error messages
- Professional logging standards

## Testing Requirements

### Test Structure
- **Unit tests**: Individual component testing with comprehensive coverage
- **Integration tests**: Script workflow testing with realistic scenarios
- **End-to-end tests**: Complete workflow validation
- **Test configuration**: `pytest.ini` with coverage reporting
- **Test fixtures**: Shared fixtures in `conftest.py`

### Test Coverage
- **100% test pass rate** (34/34 tests)
- **Zero warnings** - All pytest configuration issues resolved
- **Professional logging** - No emoji-based output in tests
- **Comprehensive validation** - All scripts and parser functionality tested

### Test Execution
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

## Maintenance

### Update Triggers
- Specification changes
- New validation requirements
- Framework updates
- User feedback
- Bug fixes
- Semantic parser improvements
- Professional logging enhancements

### Testing Requirements
- Unit tests for each script
- Integration tests for workflows
- Cross-platform testing
- Performance benchmarking
- Error scenario testing
- Semantic parser test coverage
- Professional logging validation

### Documentation
- Clear usage instructions with LLM/Cursor examples
- Example outputs with professional formatting
- Troubleshooting guides
- Configuration options
- Integration examples
- Semantic parser documentation
- Professional logging standards

## Security Considerations

### Input Validation
- Sanitize file paths
- Validate specification format
- Check for malicious content
- Limit file access scope
- Secure error messages

### Output Security
- No sensitive information in output
- Sanitized error messages
- Secure logging practices
- Access control validation
- Audit trail maintenance
- Professional error reporting

## References
- [AGILE_SPECFIRST.md](AGILE_SPECFIRST.md)
- [SPECIFICATION_VALIDATION.md](SPECIFICATION_VALIDATION.md)
- [CURSOR_INTEGRATION.md](CURSOR_INTEGRATION.md)
- [EXAMPLE_SPECIFICATIONS.md](EXAMPLE_SPECIFICATIONS.md) 