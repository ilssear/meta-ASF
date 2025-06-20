# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Development Setup Guide

# Development Setup

## Overview
This guide provides comprehensive setup instructions for development environments.

## Environment Setup

### 1. System Requirements
- Python 3.8+
- Git
- Docker (optional)
- Node.js (optional)
- PostgreSQL (optional)

### 2. Development Tools
- VS Code
- PyCharm
- Git
- Docker Desktop
- Postman

### 3. Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

### 4. Database Setup
```bash
# Start PostgreSQL
docker run -d \
    --name postgres \
    -e POSTGRES_PASSWORD=postgres \
    -e POSTGRES_USER=postgres \
    -e POSTGRES_DB=app \
    -p 5432:5432 \
    postgres:13
```

## Project Setup

### 1. Clone Repository
```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
```

### 2. Install Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

### 3. Configuration
```bash
# Copy configuration template
cp config.json.template config.json

# Edit configuration
nano config.json
```

### 4. Database Migration
```bash
# Run migrations
python manage.py migrate
```

## Development Tools

### 1. Code Quality
- Black for formatting
- Flake8 for linting
- MyPy for type checking
- Pytest for testing

### 2. Git Hooks
- pre-commit
- pre-push
- commit-msg

### 3. IDE Setup
- VS Code extensions
- PyCharm plugins
- Editor config

### 4. Debugging Tools
- Python debugger
- Logging
- Profiling
- Testing

## Best Practices

### 1. Environment Management
- Use virtual environments
- Pin dependencies
- Document requirements
- Version control

### 2. Configuration
- Use environment variables
- Secure secrets
- Version control
- Documentation

### 3. Development Workflow
- Git workflow
- Code review
- Testing
- Documentation

### 4. Security
- Secure credentials
- Access control
- Data protection
- Audit logging

## Troubleshooting

### 1. Common Issues
- Environment setup
- Dependencies
- Configuration
- Database

### 2. Debug Steps
- Check logs
- Verify config
- Test connections
- Check permissions

### 3. Recovery Steps
- Reset environment
- Reinstall dependencies
- Restore database
- Fix configuration

## References
- [Python Setup Guide](https://docs.python.org/3/tutorial/venv.html)
- [Docker Documentation](https://docs.docker.com/)
- [PostgreSQL Guide](https://www.postgresql.org/docs/)
- [VS Code Setup](https://code.visualstudio.com/docs)
- [Git Workflow](https://git-scm.com/doc) 