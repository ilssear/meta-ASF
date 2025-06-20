# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Scripts Specification

## Overview
This document defines the functional requirements for all validation scripts in the SpecFirst framework. It ensures that scripts can be regenerated from clear specifications and maintain consistency across the framework.

## Purpose
The validation scripts serve as quality gates for the SpecFirst methodology, ensuring that projects meet specification requirements and maintain documentation standards.

## Core Scripts

### 1. validate_project.py

#### Purpose
Determines the overall project development stage and provides a clear status for CI/CD pipelines and quality assurance.

#### Functional Requirements
- **Input**: Project root directory containing SPECIFICATIONS.md
- **Output**: Project stage (1-6) with detailed status information
- **Processing**: Analyze project structure and documentation completeness

#### Project Stages
1. **No Specifications**: SPECIFICATIONS.md missing
2. **Incomplete Source Files**: SPECIFICATIONS.md present but required files missing
3. **Ready to Generate**: All source files present, core directories missing
4. **Documentation Incomplete**: Core structure present, documentation missing
5. **Implementation Ready**: Documentation complete, implementation needed
6. **Complete**: All requirements met, project ready for use

#### Validation Logic
- Check for SPECIFICATIONS.md existence
- Validate required source files from specifications
- Check core directory structure (docs/, scripts/)
- Verify documentation completeness
- Assess implementation status

#### Error Handling
- Clear error messages for missing files
- Detailed status information
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
Validates documentation completeness and identifies missing or inconsistent files.

#### Functional Requirements
- **Input**: Project root directory and SPECIFICATIONS.md
- **Output**: Detailed list of missing files and content requirements
- **Processing**: Parse specifications and compare with existing documentation

#### Validation Areas
- Required documentation files
- Template files
- Cross-references
- Content completeness
- File structure alignment

#### Content Analysis
- Parse SPECIFICATIONS.md for required files
- Check file existence and content
- Validate copyright headers
- Verify cross-references
- Assess content quality

#### Output Format
```
# LLM Task: Synchronize Documentation Files

## 📝 Plan: Create Missing Files
Based on `SPECIFICATIONS.md`, the following required files are missing...

### 📄 File to Create: [file_path]

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

### 3. check_structure.py

#### Purpose
Validates project structure integrity and ensures alignment with specifications.

#### Functional Requirements
- **Input**: Project root directory
- **Output**: Structure validation results with detailed error reporting
- **Processing**: Check directory structure and file organization

#### Structure Validation
- Required directories exist
- Required files present
- Directory hierarchy correct
- File naming conventions
- Path relationships

#### Validation Rules
- SPECIFICATIONS.md must exist in project root
- scripts/ directory must exist and contain validation scripts
- docs/ directory structure must match specifications
- All required files must be present
- Cross-references must be valid

#### Output Format
```
🔍 Checking project structure at: [path]

✅ Found required file: [file_name]
✅ Found required directory: [dir_name]
    - ✅ Directory is not empty: [dir_name]

📄 Checking documentation structure based on SPECIFICATIONS.md...

--------------------

🚨 Found errors:

❌ Missing required file: [file_name]
❌ Missing required directory: [dir_name]
    - ❌ Missing required doc file: [file_path]

🚫 Project structure is INVALID.
```

#### Error Handling
- Clear identification of missing components
- Specific file and directory paths
- Actionable error messages
- Validation status summary

## Script Dependencies

### Common Libraries
- `os`: File system operations
- `sys`: System-specific parameters
- `json`: JSON file processing
- `re`: Regular expressions for parsing
- `pathlib`: Path manipulation (Python 3.4+)

### Framework Dependencies
- `lib/framework_validator.py`: Core validation logic
- `lib/spec_parser.py`: Specification parsing utilities
- `defaults/environment.json`: Environment configuration
- `defaults/defaults.json`: Default settings

## Quality Standards

### Code Quality
- Comprehensive error handling
- Clear, descriptive variable names
- Proper documentation and comments
- Consistent code style (PEP 8)
- Type hints for function parameters

### Performance Requirements
- Fast execution (< 10 seconds for typical projects)
- Minimal memory usage
- Efficient file system operations
- Optimized parsing algorithms

### Reliability
- Graceful handling of missing files
- Robust error recovery
- Consistent output formats
- Cross-platform compatibility
- Version control friendly

## Integration Requirements

### CI/CD Integration
- Exit codes for automation
- Structured output for parsing
- Clear success/failure indicators
- Detailed logging capabilities
- Configuration file support

### IDE Integration
- Real-time validation feedback
- Quick status checks
- Error highlighting
- Actionable suggestions
- Progress indicators

## Maintenance

### Update Triggers
- Specification changes
- New validation requirements
- Framework updates
- User feedback
- Bug fixes

### Testing Requirements
- Unit tests for each script
- Integration tests for workflows
- Cross-platform testing
- Performance benchmarking
- Error scenario testing

### Documentation
- Clear usage instructions
- Example outputs
- Troubleshooting guides
- Configuration options
- Integration examples

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

## References
- [AGILE_SPECFIRST.md](AGILE_SPECFIRST.md)
- [SPECIFICATION_VALIDATION.md](SPECIFICATION_VALIDATION.md)
- [CURSOR_INTEGRATION.md](CURSOR_INTEGRATION.md)
- [EXAMPLE_SPECIFICATIONS.md](EXAMPLE_SPECIFICATIONS.md) 