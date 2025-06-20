# Copyright Templates

## Overview
This directory contains copyright templates for different types of files in the project. These templates ensure consistent copyright headers across all project files.

## Templates

### 1. Code Files (code_example.py)
- Used for Python source files
- Includes copyright notice, license, and version information
- Follows PEP 8 style guidelines

### 2. Documentation Files (documentation.md)
- Used for Markdown documentation files
- Includes copyright notice and version information
- Follows project documentation standards

### 3. Project Level (project_level.py)
- Used for project-level Python files
- Includes comprehensive copyright and license information
- Follows project coding standards

## Usage

1. Copy the appropriate template for your file type
2. Replace placeholders with actual values:
   - `{{YEAR}}` - Current year
   - `{{AUTHOR}}` - Author name
   - `{{PROJECT}}` - Project name
   - `{{VERSION}}` - File version
   - `{{DESCRIPTION}}` - File description

## Example

```python
# Copyright (c) {{YEAR}} {{AUTHOR}}
# All rights reserved.
#
# This file is part of {{PROJECT}}.
# Version: {{VERSION}}
#
# {{DESCRIPTION}}
```

## References
- [Python Style Guide](../framework/style/python_style.md)
- [Documentation Guide](../../development/documentation/README.md)
- [Implementation Guide](../framework/best_practices/implementation_guide.md) 