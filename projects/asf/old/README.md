# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Development Framework

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](https://github.com/jmoraga/meta-ASF)
[![Status](https://img.shields.io/badge/status-Active-green.svg)](https://github.com/jmoraga/meta-ASF)
[![Last Updated](https://img.shields.io/badge/last%20updated-2025--06--20-orange.svg)](https://github.com/jmoraga/meta-ASF)

## 🚀 Quick Start

The SpecFirst Development Framework enables you to create complete, clear specifications before implementation, making complex development accessible to beginners while supporting experienced developers with best practices. The framework integrates **Test-Driven Development (TDD)** as a quality assurance tool and follows **PERA cycles** (Plan-Execute-Report/Review-Adjust) for continuous improvement.

### What is SpecFirst?

SpecFirst is a methodology that emphasizes:
- **Specification-first development**: All development starts with comprehensive specifications
- **Documentation-driven implementation**: Code is generated from validated specifications  
- **Iterative refinement**: Specifications evolve through continuous feedback and testing
- **User-centric validation**: All specifications are validated against user needs
- **Cross-platform compatibility**: Specifications are technology-agnostic
- **Beginner-friendly approach**: Accessible to non-technical users while powerful for experts
- **TDD as Quality Assurance**: Test-Driven Development ensures code quality and correctness
- **PERA Methodology**: Continuous improvement through Plan-Execute-Report/Review-Adjust cycles

### Target Users

- **Vibe Coders**: Creative individuals with great ideas but no coding experience
- **Software Development Teams**: Need structured approach to requirements gathering
- **Project Managers**: Need clear project scope definition and progress tracking
- **Individual Developers**: Need guidance on specification creation and implementation

## 📋 Prerequisites

- **Python 3.8+** with mamba/conda package management
- **Cursor IDE** for AI-assisted development
- **Git** for version control
- **WSL2/Ubuntu** (recommended for development)

## 🛠️ Installation

### Option 1: Quick Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/jmoraga/meta-ASF.git
cd meta-ASF/projects/asf

# Run the project validator to check your setup
python3 scripts/validate_project.py

# If you need to generate missing documentation
python3 scripts/check_docs.py --report
```

### Option 2: Manual Setup

```bash
# Create project directory
mkdir my-specfirst-project
cd my-specfirst-project

# Copy framework files
cp -r /path/to/meta-ASF/projects/asf/* .

# Initialize your project
python3 scripts/validate_project.py
```

### Option 3: Using Package Managers

#### With Conda/Mamba
```bash
# Create environment
mamba create -n specfirst python=3.11
mamba activate specfirst

# Install dependencies
pip install -r requirements.txt
```

#### With pip
```bash
# Install directly
pip install specfirst-framework
```

## 🎯 Usage

### 1. Project Initialization

```bash
# Start a new project
python3 scripts/validate_project.py --root-dir /path/to/your/project

# Check project status
python3 scripts/validate_project.py --verbose
```

### 2. Specification Creation

Create your project specification following the SpecFirst methodology:

```markdown
# SPECIFICATIONS.md

## Project Overview
- Purpose: [What your project does]
- Target users: [Who will use it]
- Key features: [Main functionality]
- Success criteria: [How you'll know it's working]

## Functional Requirements
- User stories: [What users need to do]
- Feature descriptions: [Detailed functionality]
- Input/output specifications: [Data flow]
- Data models: [Information structure]

## Behavioral Requirements
- User workflows: [Step-by-step processes]
- State transitions: [How the system changes]
- Error handling: [What happens when things go wrong]
- Edge cases: [Unusual situations]

## Visual Requirements
- UI/UX design: [How it looks and feels]
- Layout specifications: [Screen organization]
- Visual feedback: [User notifications]
- Responsive design: [Mobile/desktop compatibility]

## Performance Requirements
- Response times: [Speed expectations]
- Resource usage: [Memory/CPU requirements]
- Scalability: [Growth capacity]
- Load handling: [Concurrent users]

## Security Requirements
- Authentication: [User verification]
- Authorization: [Access control]
- Data protection: [Privacy measures]
- Input validation: [Data safety]
```

### 3. Documentation Generation

```bash
# Generate all required documentation
python3 scripts/check_docs.py

# Get detailed report
python3 scripts/check_docs.py --report

# Check for missing files
python3 scripts/check_docs.py --verbose
```

### 4. Implementation with TDD

The framework provides templates and guides for:

- **API Development**: RESTful endpoints, schemas, Swagger documentation
- **Security**: Authentication, authorization, data protection
- **Testing**: Unit tests, integration tests, end-to-end tests with TDD
- **Deployment**: Environment setup, configuration management
- **Documentation**: User guides, API documentation, troubleshooting

### 5. Validation and Testing

```bash
# Run project validation
python3 scripts/validate_project.py

# Check documentation completeness
python3 scripts/check_docs.py

# Run structure validation
python3 scripts/check_structure.py
```

### 6. PERA Cycle Implementation

Follow the PERA methodology for continuous improvement:

```bash
# Plan Phase: Review and plan improvements
python3 scripts/validate_project.py --verbose

# Execute Phase: Implement changes with TDD
# (Use TDD workflow for all code changes)

# Report/Review Phase: Validate results
python3 scripts/check_docs.py --report

# Adjust Phase: Refine based on feedback
# (Update specifications and repeat cycle)
```

## 📚 Documentation

### Core Methodology
- [AGILE_SPECFIRST.md](docs/framework/methodology/AGILE_SPECFIRST.md) - Core methodology documentation with TDD and PERA integration
- [VIBE_USER_GUIDE.md](docs/framework/methodology/VIBE_USER_GUIDE.md) - Beginner-friendly guide
- [CURSOR_INTEGRATION.md](docs/framework/methodology/CURSOR_INTEGRATION.md) - Cursor IDE integration
- [EXAMPLE_SPECIFICATIONS.md](docs/framework/methodology/EXAMPLE_SPECIFICATIONS.md) - Example specifications

### Development Guides
- [Development Workflow](docs/development/workflow/development_workflow.md) - Implementation process with TDD
- [Testing Workflow](docs/development/workflow/testing_workflow.md) - Testing strategies and TDD
- [Deployment Workflow](docs/development/workflow/deployment_workflow.md) - Deployment process
- [Unit Testing](docs/development/testing/unit_testing.md) - Unit testing guide with TDD
- [Integration Testing](docs/development/testing/integration_testing.md) - Integration testing
- [End-to-End Testing](docs/development/testing/e2e_testing.md) - E2E testing

### Best Practices
- [Best Practices Overview](docs/framework/best_practices/README.md) - General best practices
- [Patterns Overview](docs/framework/patterns/README.md) - Design patterns
- [Style Guide](docs/framework/style/README.md) - Code and documentation style

### Templates and Defaults
- [Copyright Templates](docs/defaults/templates/copyright/) - Copyright headers
- [Configuration Templates](docs/defaults/templates/config/) - Configuration files
- [Testing Templates](docs/defaults/templates/testing/) - Test templates with TDD
- [Security Templates](docs/defaults/templates/security/) - Security implementations
- [Framework Templates](docs/defaults/templates/framework/) - Framework guides

## 🔧 Configuration

### Environment Setup

The framework uses `defaults/environment.json` for environment-specific settings:

```json
{
  "development": {
    "python_version": "3.11",
    "package_manager": "mamba",
    "ide": "cursor",
    "platform": "wsl2"
  },
  "production": {
    "python_version": "3.11",
    "package_manager": "pip",
    "platform": "linux"
  }
}
```

### User Preferences

Customize your development experience:

- [User Preferences](docs/user/preferences/README.md) - Personal settings
- [Communication Guidelines](docs/user/communication/README.md) - Team communication
- [Configuration Guide](docs/user/config/) - Custom configurations
- [Custom Extensions](docs/user/custom/) - Framework extensions

## 🚨 Troubleshooting

### Common Issues

#### Project Validation Fails
```bash
# Check project structure
python3 scripts/validate_project.py --verbose

# Verify SPECIFICATIONS.md exists
ls -la SPECIFICATIONS.md

# Check for required directories
ls -la docs/ scripts/
```

#### Missing Documentation
```bash
# Get detailed report of missing files
python3 scripts/check_docs.py --report

# Generate missing documentation
python3 scripts/check_docs.py
```

#### Import Errors
```bash
# Check Python path
python3 -c "import sys; print(sys.path)"

# Verify script dependencies
python3 scripts/check_docs.py --verbose
```

#### Permission Issues
```bash
# Fix file permissions
chmod +x scripts/*.py

# Check directory permissions
ls -la scripts/
```

### Debug Mode

Enable verbose logging for detailed troubleshooting:

```bash
# Verbose project validation
python3 scripts/validate_project.py --verbose

# Verbose documentation checking
python3 scripts/check_docs.py --verbose

# Check script structure
python3 scripts/check_structure.py --verbose
```

### Getting Help

1. **Check the documentation**: Start with the [VIBE_USER_GUIDE.md](docs/framework/methodology/VIBE_USER_GUIDE.md)
2. **Run validation scripts**: Use `validate_project.py` and `check_docs.py`
3. **Review examples**: See [EXAMPLE_SPECIFICATIONS.md](docs/framework/methodology/EXAMPLE_SPECIFICATIONS.md)
4. **Check methodology**: Read [AGILE_SPECFIRST.md](docs/framework/methodology/AGILE_SPECFIRST.md)

## 🔄 Development Workflow

### 1. Specification Phase
- Define project requirements
- Create user stories
- Document constraints
- Validate specifications

### 2. Documentation Phase
- Generate required documentation
- Create templates
- Set up project structure
- Configure environment

### 3. Implementation Phase with TDD
- Write failing tests first
- Generate code from specifications
- Follow established patterns
- Apply best practices
- Test continuously

### 4. Validation Phase
- Run comprehensive tests
- Validate against specifications
- Check documentation completeness
- Get user feedback

### 5. PERA Cycle Phase
- Plan next improvements
- Execute changes with TDD
- Report/Review results
- Adjust based on feedback

### 6. Deployment Phase
- Package application
- Configure production environment
- Deploy and monitor
- Document deployment process

## 📊 Project Status

Current Status: **Stage 4 - Ready for Finalization**

- ✅ All required documentation generated (39/39 files)
- ✅ Core project structure in place
- ✅ Source methodology files complete with TDD and PERA integration
- ✅ Validation scripts functional
- 🔄 Final artifacts pending (README.md, .cursorrules)

## 🤝 Contributing

1. **Follow the SpecFirst methodology**: Start with specifications
2. **Use TDD for quality assurance**: Write tests before implementation
3. **Follow PERA cycles**: Plan-Execute-Report/Review-Adjust for continuous improvement
4. **Use the validation scripts**: Ensure quality and completeness
5. **Document your changes**: Update relevant documentation
6. **Test thoroughly**: Run all validation scripts
7. **Get feedback**: Share with the community

### Development Standards

- Follow [Python Style Guide](docs/framework/style/python_style.md)
- Use [Testing Patterns](docs/framework/patterns/testing_patterns.md) with TDD
- Apply [Security Patterns](docs/framework/patterns/security_patterns.md)
- Follow [API Patterns](docs/framework/patterns/api_patterns.md)
- Implement PERA cycles for continuous improvement

## 📄 License

Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

This project is licensed under the terms specified in the LICENSE file.

## 🙏 Acknowledgments

- Cursor IDE team for AI-assisted development capabilities
- The Python community for excellent tooling and documentation
- All contributors who help improve the SpecFirst methodology

## 📞 Support

For questions, issues, or contributions:

- **Documentation**: Check the [docs/](docs/) directory
- **Examples**: Review [EXAMPLE_SPECIFICATIONS.md](docs/framework/methodology/EXAMPLE_SPECIFICATIONS.md)
- **Methodology**: Read [AGILE_SPECFIRST.md](docs/framework/methodology/AGILE_SPECFIRST.md)
- **User Guide**: Start with [VIBE_USER_GUIDE.md](docs/framework/methodology/VIBE_USER_GUIDE.md)

---

**Version**: 1.0.1 | **Last Updated**: 2025-06-20 | **Status**: Active 