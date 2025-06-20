# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Setup Guide

## Overview

This guide provides comprehensive instructions for setting up and configuring the SpecFirst framework in your development environment.

## Prerequisites

### 1. System Requirements
- Operating System
  - Linux (Ubuntu 20.04+)
  - macOS (10.15+)
  - Windows 10+ (WSL2 recommended)
- Hardware
  - CPU: 4+ cores recommended
  - RAM: 8GB+ recommended
  - Storage: 10GB+ free space
  - GPU: NVIDIA GPU with CUDA support (optional)

### 2. Required Software
- Python 3.8+
- Node.js 16+
- Git
- VS Code with Cursor extension
- Package Managers
  - mamba (recommended)
  - conda
  - pip

### 3. Development Tools
- Code Editor
  - VS Code
  - Cursor extension
  - Python extension
  - Git extension
- Version Control
  - Git
  - GitHub account
- Terminal
  - WSL2 (Windows)
  - iTerm2 (macOS)
  - Default terminal (Linux)

## Installation

### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/yourusername/SpecFirst.git
cd SpecFirst

# Create environment (mamba)
mamba create -n specfirst python=3.8
mamba activate specfirst

# Create environment (conda)
conda create -n specfirst python=3.8
conda activate specfirst

# Create environment (pip)
python -m venv specfirst
source specfirst/bin/activate  # Linux/macOS
.\specfirst\Scripts\activate   # Windows
```

### 2. Dependencies Installation
```bash
# Install dependencies (mamba)
mamba install -c conda-forge -c pytorch -c nvidia \
    pytorch torchvision torchaudio pytorch-cuda=11.8 \
    -y

# Install dependencies (conda)
conda install -c conda-forge -c pytorch -c nvidia \
    pytorch torchvision torchaudio pytorch-cuda=11.8 \
    -y

# Install dependencies (pip)
pip install -r requirements.txt
```

### 3. Configuration
```bash
# Create config directory
mkdir -p config

# Create config template
cp config/config.json.template config/config.json

# Edit configuration
nano config/config.json
```

## Verification

### 1. Environment Check
```bash
# Check Python version
python --version

# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"

# Check installed packages
pip list
```

### 2. Framework Check
```bash
# Run verification script
python scripts/verify_setup.py

# Check documentation
python scripts/generate_docs.py
```

### 3. Test Run
```bash
# Run example project
python examples/hello_world.py

# Run tests
pytest tests/
```

## Troubleshooting

### 1. Common Issues
- CUDA Installation
  - Check NVIDIA drivers
  - Verify CUDA toolkit
  - Check PyTorch installation
- Environment Issues
  - Check Python version
  - Verify package installation
  - Check path configuration
- Configuration Issues
  - Verify config file
  - Check permissions
  - Validate settings

### 2. Debug Commands
```bash
# Check system info
python scripts/system_info.py

# Verify dependencies
python scripts/check_dependencies.py

# Test GPU
python scripts/test_gpu.py
```

### 3. Recovery Steps
- Environment Reset
  - Remove environment
  - Clear cache
  - Reinstall dependencies
- Configuration Reset
  - Backup config
  - Reset to defaults
  - Restore settings
- System Reset
  - Clear temporary files
  - Reset permissions
  - Reinstall tools

## Best Practices

### 1. Environment Management
- Use virtual environments
- Keep dependencies updated
- Document environment changes
- Use version control
- Regular maintenance

### 2. Configuration Management
- Use templates
- Document changes
- Version control
- Regular backups
- Security checks

### 3. Development Workflow
- Follow style guide
- Use linting tools
- Regular testing
- Documentation updates
- Code review

## References

1. [Environment Guide](environment.md)
2. [Configuration Guide](configuration.md)
3. [Troubleshooting Guide](troubleshooting.md)
4. [Best Practices](../best_practices/README.md)
5. [Style Guide](../style/README.md) 