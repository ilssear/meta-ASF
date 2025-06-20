# Project Setup Guide - Agile SpecFirst Framework

## Overview
This guide provides comprehensive instructions for setting up new projects using the Agile SpecFirst Framework.

## Project Initialization

### 1. Create Basic Structure
```bash
# Create project directory
mkdir myproject
cd myproject

# Create essential directories
mkdir -p src tests docs config

# Create essential files
touch README.md SPECIFICATIONS.md
touch src/__init__.py tests/__init__.py
```

### 2. Initialize Git
```bash
# Initialize git repository
git init

# Create .gitignore
cat > .gitignore << EOL
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Environment
.env
.env.*

# Build
*.pyc
*.pyo
*.pyd
.Python
*.so

# Distribution
dist/
build/
*.egg-info/

# Logs
*.log
logs/
EOL
```

## Configuration Setup

### 1. Create Configuration Template
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Configuration template for the project.
"""

from typing import Dict, Any
import json
import os

def load_config() -> Dict[str, Any]:
    """Load configuration from file.
    
    Returns:
        Dict[str, Any]: Configuration dictionary.
        
    Raises:
        FileNotFoundError: If config file doesn't exist.
        json.JSONDecodeError: If config file is invalid.
    """
    config_path = os.path.join("config", "config.json")
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, "r") as f:
        return json.load(f)
```

### 2. Python Environment Setup
```bash
# Create requirements.txt
cat > requirements.txt << EOL
# Core dependencies
flask>=2.0.0
pydantic>=1.8.0
pytest>=6.0.0

# Development tools
black>=21.0.0
flake8>=3.9.0
mypy>=0.910
EOL

# Create setup.py
cat > setup.py << EOL
# Copyright (c) [Year], [Full Name] ([Email Address])

from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask>=2.0.0",
        "pydantic>=1.8.0",
        "pytest>=6.0.0",
    ],
    extras_require={
        "dev": [
            "black>=21.0.0",
            "flake8>=3.9.0",
            "mypy>=0.910",
        ],
    },
)
EOL
```

## Documentation Setup

### 1. Create README.md
```markdown
# Project Name

## Overview
Brief description of the project.

## Setup
1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Configure environment

## Usage
Basic usage instructions.

## Development
Development setup and guidelines.

## License
MIT License
```

### 2. Initialize SPECIFICATIONS.md
```markdown
# Project Specifications

## Overview
Project purpose and goals.

## Core Requirements
1. Requirement 1
2. Requirement 2

## Success Criteria
- Criterion 1
- Criterion 2
```

## Development Tools Setup

### 1. Code Quality Tools
```yaml
# .pre-commit-config.yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files

-   repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
    -   id: black

-   repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
    -   id: flake8
```

### 2. Testing Framework
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Test configuration and fixtures.
"""

import pytest
from typing import Generator

@pytest.fixture
def test_config() -> Generator[dict, None, None]:
    """Provide test configuration.
    
    Yields:
        dict: Test configuration.
    """
    config = {
        "test_key": "test_value",
        "debug": True,
    }
    yield config
```

## Best Practices

### 1. Code Organization
- Follow PEP 8
- Use type hints
- Write docstrings
- Keep functions small

### 2. Documentation
- Keep README updated
- Document APIs
- Include examples
- Write clear comments

### 3. Version Control
- Write clear commits
- Use feature branches
- Review code changes
- Keep history clean

### 4. Testing
- Write tests first
- Test edge cases
- Mock dependencies
- Measure coverage

## Version History

### v1.0.0 (2025-01-15)
- Initial project setup
- Basic structure
- Core configuration

### v1.1.0 (2025-01-20)
- Enhanced documentation
- Development tools
- Best practices

## References
- [Agile SpecFirst Framework](../methodology/AGILE_SPECFIRST.md)
- [Environment Setup](./environment_setup.md)
- [Best Practices Guide](../best_practices/README.md) 