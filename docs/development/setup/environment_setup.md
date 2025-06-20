# Environment Setup Guide - Agile SpecFirst Framework

## Overview
This guide provides comprehensive instructions for setting up development environments for Agile SpecFirst Framework projects.

## System Requirements

### 1. Operating System
- Linux (Ubuntu 20.04+)
- macOS (10.15+)
- Windows 10/11 with WSL2

### 2. Hardware Requirements
- CPU: 4+ cores recommended
- RAM: 8GB minimum, 16GB recommended
- Storage: 20GB+ free space
- GPU: NVIDIA GPU with CUDA support (optional)

## Package Management

### 1. Mamba/Conda (Recommended)
```bash
# Install Mamba
curl -L -O "https://micro.mamba.pm/api/micromamba/linux-64/latest"
chmod +x micromamba
./micromamba shell init -s bash -p ~/micromamba
source ~/.bashrc

# Create environment
micromamba create -n myenv python=3.10
micromamba activate myenv
```

### 2. Conda
```bash
# Install Conda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

# Create environment
conda create -n myenv python=3.10
conda activate myenv
```

### 3. Pip (Fallback)
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
.\venv\Scripts\activate   # Windows
```

## Core Dependencies

### 1. Python Packages
```bash
# Install core packages
pip install -r requirements.txt

# Install development tools
pip install -r requirements-dev.txt
```

### 2. Development Tools
```bash
# Install pre-commit hooks
pre-commit install

# Install VS Code extensions
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance
```

## IDE Setup

### 1. Cursor IDE
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true,
    "editor.rulers": [88],
    "files.trimTrailingWhitespace": true
}
```

### 2. VS Code
```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

## Environment Verification

### 1. Python Setup
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Verify Python environment setup.
"""

import sys
import platform
from typing import Dict, Any

def verify_python() -> Dict[str, Any]:
    """Verify Python environment.
    
    Returns:
        Dict[str, Any]: Environment information.
    """
    return {
        "python_version": sys.version,
        "platform": platform.platform(),
        "executable": sys.executable
    }
```

### 2. GPU Support
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Verify GPU support.
"""

import torch
from typing import Dict, Any

def verify_gpu() -> Dict[str, Any]:
    """Verify GPU availability.
    
    Returns:
        Dict[str, Any]: GPU information.
    """
    return {
        "cuda_available": torch.cuda.is_available(),
        "device_count": torch.cuda.device_count(),
        "device_name": torch.cuda.get_device_name(0) if torch.cuda.is_available() else None
    }
```

### 3. Development Tools
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Verify development tools.
"""

import subprocess
from typing import Dict, Any

def verify_tools() -> Dict[str, Any]:
    """Verify development tools.
    
    Returns:
        Dict[str, Any]: Tools information.
    """
    tools = {}
    for tool in ["black", "flake8", "mypy", "pytest"]:
        try:
            version = subprocess.check_output([tool, "--version"]).decode().strip()
            tools[tool] = version
        except subprocess.CalledProcessError:
            tools[tool] = "Not installed"
    return tools
```

## Security Considerations

### 1. Environment Variables
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
Environment variable management.
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

def load_env() -> Dict[str, Any]:
    """Load environment variables.
    
    Returns:
        Dict[str, Any]: Environment variables.
    """
    load_dotenv()
    return {
        "api_key": os.getenv("API_KEY"),
        "environment": os.getenv("ENVIRONMENT", "development"),
        "debug": os.getenv("DEBUG", "false").lower() == "true"
    }
```

### 2. .env File
```bash
# .env
API_KEY=your_api_key_here
ENVIRONMENT=development
DEBUG=true
```

## Best Practices

### 1. Environment Isolation
- Use virtual environments
- Keep dependencies updated
- Document requirements
- Use dependency locks

### 2. Version Control
- Ignore virtual environments
- Ignore IDE settings
- Ignore environment files
- Track dependency files

### 3. Documentation
- Document setup steps
- Include verification
- List requirements
- Provide examples

## Version History

### v1.0.0 (2025-01-15)
- Initial environment setup
- Core dependencies
- Basic verification

### v1.1.0 (2025-01-20)
- Enhanced security
- Added GPU support
- Improved verification

## References
- [Project Setup Guide](./project_setup.md)
- [Best Practices Guide](../best_practices/README.md)
- [Style Guide](../style/python_style.md) 