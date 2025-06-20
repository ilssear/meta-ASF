# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst User Preferences Guide

## Overview

This guide outlines the user preferences and customization options available in the SpecFirst framework, allowing users to tailor the framework to their needs.

## User Preferences

### 1. Development Preferences
- Code Style
  - Indentation
  - Line length
  - Naming conventions
  - Comment style
  - Documentation format
- Editor Settings
  - Theme
  - Font
  - Key bindings
  - Extensions
  - Auto-completion

### 2. Framework Preferences
- Project Structure
  - Directory layout
  - File organization
  - Module structure
  - Configuration files
  - Documentation location
- Workflow Settings
  - Git workflow
  - Testing strategy
  - Documentation process
  - Review process
  - Deployment workflow

### 3. Documentation Preferences
- Format
  - Markdown style
  - Code blocks
  - Headers
  - Lists
  - Tables
- Content
  - Detail level
  - Example style
  - Language
  - Terminology
  - References

### 4. Testing Preferences
- Framework
  - Test runner
  - Assertion style
  - Mocking approach
  - Coverage requirements
  - Performance metrics
- Organization
  - Test structure
  - Naming conventions
  - Fixture usage
  - Test data
  - Reporting format

## Customization Options

### 1. Project Templates
```bash
# Create project template
python scripts/create_template.py --name my_template

# Use template
python scripts/create_project.py --template my_template
```

### 2. Configuration Files
```json
{
    "editor": {
        "theme": "dark",
        "font": "Fira Code",
        "line_length": 88,
        "indent_size": 4
    },
    "framework": {
        "project_structure": "standard",
        "documentation": "detailed",
        "testing": "comprehensive"
    },
    "documentation": {
        "format": "markdown",
        "style": "google",
        "language": "en"
    }
}
```

### 3. Style Customization
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Custom style configuration.
"""

from typing import Dict, Any

STYLE_CONFIG: Dict[str, Any] = {
    "python": {
        "indent_size": 4,
        "line_length": 88,
        "docstring_style": "google",
        "type_hints": True
    },
    "markdown": {
        "header_style": "atx",
        "list_style": "unordered",
        "code_style": "fenced"
    }
}
```

## Preference Management

### 1. Setting Preferences
```bash
# Set user preferences
python scripts/set_preferences.py --config preferences.json

# Update preferences
python scripts/update_preferences.py --key editor.theme --value dark

# Reset preferences
python scripts/reset_preferences.py
```

### 2. Preference Validation
```bash
# Validate preferences
python scripts/validate_preferences.py

# Check conflicts
python scripts/check_preference_conflicts.py

# Generate report
python scripts/generate_preference_report.py
```

### 3. Preference Migration
```bash
# Export preferences
python scripts/export_preferences.py --format json

# Import preferences
python scripts/import_preferences.py --file preferences.json

# Migrate preferences
python scripts/migrate_preferences.py --from v1 --to v2
```

## Best Practices

### 1. Preference Organization
- Use categories
- Maintain hierarchy
- Document changes
- Version control
- Regular review

### 2. Preference Updates
- Incremental changes
- Document rationale
- Test impact
- Validate changes
- Update documentation

### 3. Preference Sharing
- Use templates
- Document customizations
- Share configurations
- Version control
- Regular sync

### 4. Preference Maintenance
- Regular review
- Clean up unused
- Update defaults
- Document changes
- Validate settings

## Tools and Resources

### 1. Preference Tools
- Configuration editors
- Validators
- Migrators
- Exporters
- Importers

### 2. Documentation
- Preference guides
- Configuration docs
- Migration guides
- Best practices
- Examples

### 3. Templates
- Project templates
- Style templates
- Config templates
- Doc templates
- Test templates

### 4. Validation
- Config validators
- Style checkers
- Format validators
- Conflict checkers
- Report generators

## Common Scenarios

### 1. New Project Setup
1. Choose template
2. Set preferences
3. Customize settings
4. Validate config
5. Start development

### 2. Team Integration
1. Share preferences
2. Align settings
3. Document customizations
4. Validate consistency
5. Update documentation

### 3. Style Updates
1. Review current style
2. Plan changes
3. Update settings
4. Validate changes
5. Update docs

### 4. Migration
1. Export settings
2. Plan migration
3. Update preferences
4. Validate changes
5. Update docs

## Troubleshooting

### 1. Common Issues
- Invalid settings
- Conflicts
- Migration errors
- Validation failures
- Sync problems

### 2. Debug Steps
- Check config
- Verify settings
- Review logs
- Test changes
- Validate output

### 3. Recovery Steps
- Reset settings
- Restore backup
- Fix conflicts
- Update config
- Validate changes

## References

1. [Setup Guide](../setup/README.md)
2. [Workflow Guide](../workflow/README.md)
3. [Documentation Guide](../documentation/README.md)
4. [Best Practices](../best_practices/README.md)
5. [Style Guide](../style/README.md) 