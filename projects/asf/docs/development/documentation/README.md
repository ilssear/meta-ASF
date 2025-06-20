# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Development Documentation Guide

# Documentation Guide

## Overview
This guide provides comprehensive documentation instructions and best practices.

## Documentation Types

### 1. Project Documentation
- README files
- Project structure
- Setup guides
- Contributing guides

### 2. Code Documentation
- Function documentation
- Class documentation
- Module documentation
- Package documentation

### 3. API Documentation
- API endpoints
- Request/response formats
- Authentication
- Error handling

### 4. User Documentation
- User guides
- Tutorials
- Examples
- Troubleshooting

## Documentation Tools

### 1. Documentation Generators
- Sphinx
- MkDocs
- Docusaurus
- Jekyll

### 2. Code Documentation
- Docstrings
- Type hints
- Comments
- Examples

### 3. API Documentation
- OpenAPI/Swagger
- Postman
- API Blueprint
- RAML

### 4. User Documentation
- Markdown
- HTML
- PDF
- Interactive guides

## Documentation Process

### 1. Documentation Planning
- Content structure
- Style guide
- Review process
- Maintenance plan

### 2. Documentation Writing
- Clear language
- Proper formatting
- Code examples
- Visual aids

### 3. Documentation Review
- Technical review
- Editorial review
- User testing
- Feedback incorporation

### 4. Documentation Maintenance
- Regular updates
- Version control
- Change tracking
- Quality checks

## Best Practices

### 1. Documentation Organization
- Clear structure
- Logical grouping
- Easy navigation
- Consistent style

### 2. Documentation Writing
- Clear language
- Proper formatting
- Code examples
- Visual aids

### 3. Documentation Review
- Technical review
- Editorial review
- User testing
- Feedback incorporation

### 4. Documentation Maintenance
- Regular updates
- Version control
- Change tracking
- Quality checks

## Examples

### 1. Good Documentation
```python
def calculate_total(items: List[Item], tax_rate: float) -> float:
    """Calculate total price including tax.
    
    Args:
        items: List of items to calculate total for
        tax_rate: Tax rate as decimal (e.g., 0.1 for 10%)
        
    Returns:
        Total price including tax
        
    Raises:
        ValueError: If tax_rate is negative
        
    Example:
        >>> items = [Item(price=10.0), Item(price=20.0)]
        >>> calculate_total(items, 0.1)
        33.0
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
        
    subtotal = sum(item.price for item in items)
    tax = subtotal * tax_rate
    return subtotal + tax
```

### 2. Poor Documentation
```python
def calc(items, tax):
    return sum(i.price for i in items) * (1 + tax)
```

## Common Pitfalls

### 1. Documentation Organization
- Missing structure
- Poor grouping
- Hard navigation
- Inconsistent style

### 2. Documentation Writing
- Unclear language
- Bad formatting
- Missing examples
- No visual aids

### 3. Documentation Review
- No technical review
- No editorial review
- No user testing
- No feedback

### 4. Documentation Maintenance
- No updates
- No version control
- No change tracking
- No quality checks

## References
- [Google Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Sphinx Documentation](https://www.sphinx-doc.org/)
- [MkDocs Guide](https://www.mkdocs.org/)
- [Documentation Best Practices](https://www.writethedocs.org/guide/) 