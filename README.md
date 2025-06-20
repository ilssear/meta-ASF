# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Framework

## Overview
SpecFirst is a specification-driven development framework that emphasizes **Test-Driven Development (TDD)**, **incremental changes**, and **rapid user feedback**. This project is organized into four main documentation domains:

- **Framework documentation**: Core methodology, patterns, and best practices (technology-agnostic)
- **Development documentation**: Project implementation, workflows, and stack-specific guides (technology-specific)
- **Defaults**: Templates and default settings for quick project setup
- **User**: User-specific documentation, including communication, preferences, and customizations

## Key Features

### 🧪 Test-Driven Development (TDD)
- **Red-Green-Refactor cycle** with concrete examples
- **Test-first approach** for all new features
- **Comprehensive testing guidelines** with edge case coverage
- **Automated validation** scripts for project integrity

### 🔄 Incremental Development
- **Small, focused changes** (15 min - 2 hours)
- **Phase-based implementation** with clear checkpoints
- **Change size guidelines** to prevent scope creep
- **Validation checklists** for each change

### 📋 Rapid Feedback Loops
- **User feedback integration** at every stage
- **Specification validation** against requirements
- **Continuous validation** with automated scripts
- **Error prevention** guidelines to avoid common mistakes

### 🛠️ Validation & Quality Assurance
- **Project validation scripts** (`validate_project.py`, `check_docs.py`)
- **Specification-driven validation** (no hardcoded assumptions)
- **Comprehensive checklists** for change validation
- **Regression testing** to prevent breaking changes

## Getting Started

### Prerequisites
- Cursor IDE
- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SpecFirst.git
cd SpecFirst
```

2. Set up the development environment:
```bash
# Using mamba (recommended)
mamba create -n specfirst python=3.8
mamba activate specfirst

# Or using pip
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure your environment:
```bash
cp config/config.json.template config/config.json
# Edit config.json with your settings
```

## Usage

### For Vibe Coders

1. Start with the Vibe Coder's Guide:
```bash
# Open in Cursor IDE
cursor docs/framework/methodology/VIBE_USER_GUIDE.md
```

2. Create your first project:
```bash
# Follow the guide to create specifications.txt
# Then let Cursor help you implement it
```

### For Developers

1. Review the methodology:
```bash
cursor docs/framework/methodology/AGILE_SPECFIRST.md
```

2. Learn TDD and incremental development:
```bash
cursor docs/development/testing/unit_testing.md
cursor docs/development/workflow/development_workflow.md
```

3. Set up a new project:
```bash
# Create project structure
mkdir my_project
cd my_project

# Initialize with SpecFirst
cp ../docs/defaults/templates/SPECIFICATIONS.md.template SPECIFICATIONS.md
# Edit SPECIFICATIONS.md with your project details
```

4. Follow TDD workflow:
```bash
# Write failing test first
# Implement minimal code to pass test
# Refactor while keeping tests green
# Repeat for each feature
```

## Project Structure

```
project_root/
├── docs/
│   ├── framework/      # Core methodology, patterns, best practices
│   ├── development/    # Project implementation, workflows, stack
│   ├── defaults/       # Templates and default settings
│   └── user/           # User-specific documentation
└── projects/           # User-created PoCs/Projects

## Documentation Domains

| Area         | Directory            | Purpose                                      |
|--------------|---------------------|----------------------------------------------|
| Framework    | docs/framework/      | Core methodology, patterns, best practices   |
| Development  | docs/development/    | Project implementation, workflows, stack     |
| Defaults     | docs/defaults/       | Templates and default settings               |
| User         | docs/user/           | User-specific documentation                  |

- [Framework Documentation](docs/framework/README.md)
- [Development Documentation](docs/development/README.md)
- [Defaults Documentation](docs/defaults/README.md)
- [User Documentation](docs/user/README.md)

## Development Workflow

### 1. Specification-First
- Start with `specifications.txt` (rough ideas)
- Refine into `SPECIFICATIONS.md` (formal requirements)
- Ensure specifications are LLM-regenerable

### 2. Test-Driven Development
- Write failing test for new feature
- Implement minimal code to pass test
- Refactor while keeping tests green
- Test edge cases and error conditions

### 3. Incremental Implementation
- Make one small change at a time
- Validate each change before proceeding
- Get user feedback on each increment
- Document what changed and why

### 4. Continuous Validation
- Run validation scripts after each change
- Check for regressions
- Ensure specification alignment
- Update documentation as needed

## Getting Started
1. Read the [SPECIFICATIONS.md](SPECIFICATIONS.md) for project requirements.
2. Explore [docs/framework/](docs/framework/) for methodology and patterns.
3. Explore [docs/development/](docs/development/) for implementation workflows.
4. Create your own project in the `projects/` directory.
5. Use validation scripts to ensure quality and completeness.

## Copyright Header Rules
- Documentation files (Markdown): **Do NOT** include copyright header at the top.
- Code templates (Python, etc.): **MUST** include: `# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)` at the top.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License
MIT License. See [LICENSE](LICENSE).

## Acknowledgments

- Cursor IDE team for their amazing AI capabilities
- The Python community for their excellent tools and libraries
- All contributors who help make this framework better

## Contact

Jaime Moraga - jmoraga@mines.edu

Project Link: [https://github.com/yourusername/SpecFirst](https://github.com/yourusername/SpecFirst) 