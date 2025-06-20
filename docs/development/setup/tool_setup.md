# Tool Setup Guide

## Overview
This guide provides instructions for setting up the development tools required for the SpecFirst framework.

## Required Tools

### Version Control
1. Install Git
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install git

   # macOS
   brew install git
   ```

2. Configure Git
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### Python Environment
1. Install Mamba
   ```bash
   # Install Miniconda first
   wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
   bash Miniconda3-latest-Linux-x86_64.sh

   # Install Mamba
   conda install mamba -n base -c conda-forge
   ```

2. Create Environment
   ```bash
   mamba create -n specfirst python=3.8
   mamba activate specfirst
   ```

### Development Tools
1. Install Code Quality Tools
   ```bash
   pip install black flake8 mypy pytest
   ```

2. Install Documentation Tools
   ```bash
   pip install sphinx sphinx-rtd-theme
   ```

## Optional Tools

### Node.js Development
1. Install Node.js
   ```bash
   # Using nvm
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   nvm install 16
   ```

2. Install Development Tools
   ```bash
   npm install -g typescript eslint prettier
   ```

### Docker
1. Install Docker
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install docker.io

   # macOS
   brew install docker
   ```

2. Install Docker Compose
   ```bash
   # Ubuntu/Debian
   sudo apt-get install docker-compose

   # macOS
   brew install docker-compose
   ```

## IDE Setup

### VS Code
1. Install VS Code
   ```bash
   # Ubuntu/Debian
   sudo snap install code --classic

   # macOS
   brew install --cask visual-studio-code
   ```

2. Install Extensions
   - Python
   - GitLens
   - Markdown All in One
   - Docker
   - ESLint
   - Prettier

### PyCharm
1. Install PyCharm
   ```bash
   # Ubuntu/Debian
   sudo snap install pycharm-professional --classic

   # macOS
   brew install --cask pycharm
   ```

2. Configure Settings
   - Enable Git integration
   - Configure Python interpreter
   - Set up code style
   - Configure testing

## Best Practices
- Keep tools updated
- Use consistent versions
- Document configurations
- Regular maintenance
- Security reviews

## Troubleshooting
- Check tool versions
- Verify configurations
- Review error logs
- Check dependencies
- Update documentation

## Related Documentation
- See `docs/defaults/settings/tool_settings.md` for tool configurations
- See `docs/development/setup/environment_setup.md` for environment setup
- See `docs/framework/best_practices/implementation_guide.md` for implementation details 