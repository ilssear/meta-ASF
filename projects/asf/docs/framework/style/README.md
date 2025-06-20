# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Style Guide

## Overview
This guide provides comprehensive style guidelines and best practices for projects following the SpecFirst framework methodology.

## Code Style

### 1. Python Style
- Follow PEP 8
- Use type hints
- Write docstrings
- Handle errors
- Use consistent naming

### 2. Documentation Style
- Use Markdown
- Follow templates
- Include examples
- Add diagrams
- Cross-reference

### 3. Configuration Style
- Use YAML/JSON
- Follow templates
- Document options
- Validate configs
- Version control

### 4. Testing Style
- Follow patterns
- Write clear tests
- Document cases
- Handle errors
- Use fixtures

## Documentation Standards

### 1. Markdown Format
- Use headers
- Add lists
- Include code
- Add links
- Use tables

### 2. Code Documentation
- Write docstrings
- Add comments
- Document types
- Explain logic
- Include examples

### 3. API Documentation
- Document endpoints
- Add examples
- Include errors
- Show responses
- Add diagrams

### 4. User Documentation
- Write clearly
- Add examples
- Include screenshots
- Add tutorials
- Provide troubleshooting

## Naming Conventions

### 1. Variables
- Use snake_case
- Be descriptive
- Avoid abbreviations
- Use consistent terms
- Follow patterns

### 2. Functions
- Use snake_case
- Be descriptive
- Use verbs
- Follow patterns
- Document parameters

### 3. Classes
- Use PascalCase
- Be descriptive
- Use nouns
- Follow patterns
- Document methods

### 4. Files
- Use snake_case
- Be descriptive
- Use extensions
- Follow patterns
- Group related files

## Code Organization

### 1. File Structure
- Follow layout
- Group related code
- Use clear names
- Follow patterns
- Document structure

### 2. Module Organization
- Group by feature
- Use clear names
- Follow patterns
- Document modules
- Include tests

### 3. Class Organization
- Single responsibility
- Clear interfaces
- Document methods
- Follow patterns
- Include tests

### 4. Function Organization
- Single purpose
- Clear parameters
- Document behavior
- Follow patterns
- Include tests

## Best Practices

### 1. Code Quality
- Write clean code
- Follow standards
- Document code
- Handle errors
- Write tests

### 2. Documentation
- Keep updated
- Use templates
- Add examples
- Include diagrams
- Cross-reference

### 3. Testing
- Write tests
- Document cases
- Handle errors
- Use fixtures
- Follow patterns

### 4. Configuration
- Use templates
- Document options
- Validate configs
- Version control
- Follow patterns

## Style Examples

### 1. Good Style
```python
# Clear, well-documented function
def process_user_data(user_data: Dict[str, Any]) -> Result:
    """
    Process user data according to specifications.
    
    Args:
        user_data: Dictionary containing user data
        
    Returns:
        Result object containing processed data
        
    Raises:
        ValidationError: If user data is invalid
        ProcessingError: If processing fails
    """
    try:
        # Validate input
        validate_user_data(user_data)
        
        # Process data
        result = process_data(user_data)
        
        # Log success
        logger.info("Successfully processed user data")
        
        return result
        
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise
        
    except Exception as e:
        logger.error(f"Processing error: {e}")
        raise ProcessingError(f"Failed to process user data: {e}")
```

### 2. Poor Style
```python
# Unclear, poorly documented function
def process(data):
    # Do stuff
    x = data.get('stuff')
    if x:
        return x
    return None
```

## Common Pitfalls

### 1. Code Style
- Inconsistent style
- Poor documentation
- Unclear names
- Missing types
- Poor organization

### 2. Documentation
- Outdated docs
- Missing examples
- Poor organization
- Inconsistent style
- Missing references

### 3. Testing
- Missing tests
- Poor documentation
- Unclear cases
- Missing fixtures
- Poor organization

### 4. Configuration
- Missing docs
- Poor validation
- Inconsistent style
- Missing versioning
- Poor organization

## References
- [Specification Guide](../best_practices/specification_guide.md)
- [Implementation Guide](../best_practices/implementation_guide.md)
- [Deployment Guide](../best_practices/deployment_guide.md)
- [Security Guide](../security/README.md)
- [Agile SpecFirst Methodology](../methodology/AGILE_SPECFIRST.md) 