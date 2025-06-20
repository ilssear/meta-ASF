# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Framework

## Overview
SpecFirst is a specification-driven development framework. This project is organized into four main documentation domains:

- **Framework documentation**: Core methodology, patterns, and best practices (technology-agnostic)
- **Development documentation**: Project implementation, workflows, and stack-specific guides (technology-specific)
- **Defaults**: Templates and default settings for quick project setup
- **User**: User-specific documentation, including communication, preferences, and customizations

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

2. Set up a new project:
```bash
# Create project structure
mkdir my_project
cd my_project

# Initialize with SpecFirst
cp ../docs/defaults/templates/SPECIFICATIONS.md.template SPECIFICATIONS.md
# Edit SPECIFICATIONS.md with your project details
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

## Getting Started
1. Read the [SPECIFICATIONS.md](SPECIFICATIONS.md) for project requirements.
2. Explore [docs/framework/](docs/framework/) for methodology and patterns.
3. Explore [docs/development/](docs/development/) for implementation workflows.
4. Create your own project in the `projects/` directory.

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