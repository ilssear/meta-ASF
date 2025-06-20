# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Development Framework

## Project Overview
Create a framework for implementing the Agile SpecFirst methodology within the Cursor IDE environment, focusing on practical, runnable proof-of-concept projects. The framework will guide users through an iterative process of creating, refining, and implementing software specifications, with smart defaults and clear guidance to handle unknowns. The goal is to get users from idea to running project as quickly and smoothly as possible.

### Purpose
- Enable users to create complete, clear specifications before implementation
- Provide a structured approach to software development
- Make complex development accessible to beginners
- Support experienced developers with best practices
- Integrate seamlessly with Cursor IDE's AI capabilities

## Core Concepts

### What is a Specification?
A specification in SpecFirst is a structured document that describes:
1. What the software should do (functional requirements)
2. How it should behave (behavioral requirements)
3. What it should look like (visual requirements)
4. How it should perform (performance requirements)
5. How it should be secure (security requirements)

### Specification Format
Specifications must follow this structure:
1. Project Overview
   - Purpose
   - Target users
   - Key features
   - Success criteria

2. Functional Requirements
   - User stories
   - Feature descriptions
   - Input/output specifications
   - Data models

3. Behavioral Requirements
   - User workflows
   - State transitions
   - Error handling
   - Edge cases

4. Visual Requirements
   - UI/UX design
   - Layout specifications
   - Visual feedback
   - Responsive design

5. Performance Requirements
   - Response times
   - Resource usage
   - Scalability
   - Load handling

6. Security Requirements
   - Authentication
   - Authorization
   - Data protection
   - Input validation

### Documentation-First Development
- All development starts with documentation
- Documentation is the source of truth
- Code is generated from documentation
- Plain language preferred
- Smart defaults included

### LLM Regenerability
- Specifications must be detailed enough for AI to generate code
- Clear, unambiguous descriptions required
- Structured format for easy parsing
- Complete requirements and constraints
- Success criteria clearly defined

## Methodology Definition
The Agile SpecFirst methodology is a development approach that emphasizes:
1. Specification-first development: All development starts with comprehensive specifications
2. Documentation-driven implementation: Code is generated from validated specifications
3. Iterative refinement: Specifications evolve through continuous feedback and testing
4. User-centric validation: All specifications are validated against user needs
5. Cross-platform compatibility: Specifications are technology-agnostic
6. Beginner-friendly approach: Accessible to non-technical users while powerful for experts
7. Practical focus: Emphasis on working, runnable projects
8. Smart defaults: Intelligent handling of technical decisions

The methodology documentation and vibe-user guide are in:
- methodology/AGILE_SPECFIRST.md - Core methodology documentation
- methodology/VIBE_USER_GUIDE.md - Beginner-friendly guide
- methodology/CURSOR_INTEGRATION.md - Cursor IDE integration details
- methodology/SPECIFICATION_VALIDATION.md - Specification validation and QA/QC guide

## Target Users

### 1. Vibe Coders (Primary Focus)
- Creative individuals with great ideas but no coding experience
- Need intuitive, visual approach to software development
- Want to focus on the "vibe" and user experience
- Prefer plain language over technical terms
- Value step-by-step guidance
- Need templates and examples
- Want to learn as they build
- Need working projects quickly
- Trust smart defaults
- Prefer iterative development

### 2. Software Development Teams
- Need structured approach to requirements gathering
- Want to reduce rework and improve code quality
- Require clear documentation for maintenance
- Can leverage advanced features
- Need team collaboration tools
- Require version control integration
- Want automated validation
- Need working prototypes
- Use smart defaults as starting points
- Follow iterative process

### 3. Project Managers
- Need clear project scope definition
- Want to track progress against specifications
- Require measurable success criteria
- Need team coordination tools
- Want progress tracking
- Require resource planning
- Need risk management
- Need working demos
- Use default templates
- Track iterations

### 4. Individual Developers
- Need guidance on specification creation
- Want to ensure implementation matches requirements
- Require clear documentation for future reference
- Can use advanced features
- Need code generation tools
- Want testing automation
- Require deployment guides
- Need working examples
- Customize defaults
- Iterate quickly

## Core Components

### 1. Documentation Structure
- The directory containing SPECIFICATIONS.md is the project root
- All paths in this document are relative to the project root
- When working with user projects, their SPECIFICATIONS.md location is their project root
- When working with the framework itself, the framework's SPECIFICATIONS.md location is the project root

- /docs/ as the source of truth
  - Framework documentation
  - Implementation guides
  - Best practices
  - Troubleshooting guides
  - Vibe Coder's Guide (VIBE_USER_GUIDE.md)
  - Default configurations
  - Example projects
- .cursorrules as the implementation guide
  - Development rules
  - Coding standards
  - Process workflows
  - Beginner-friendly templates
  - Smart defaults
  - Iteration guides
- SPECIFICATIONS.md as the project definition
  - Complete project requirements
  - User stories
  - Technical constraints
  - Success criteria
  - Visual mockups
  - Default settings
  - Iteration history
- README.md as the user interface
  - Quick start guide
  - Installation instructions
  - Usage examples
  - Troubleshooting steps
  - Visual tutorials
  - Default options
  - Run instructions

### 2. Key Principles
- Documentation-first development
  - All development starts with documentation
  - Documentation is the source of truth
  - Code is generated from documentation
  - Plain language preferred
  - Smart defaults included
- Specification-driven implementation
  - Clear requirements before coding
  - Validation against specifications
  - Traceability between specs and code
  - Visual specification tools
  - Default implementations
- Cross-platform compatibility
  - Technology-agnostic specifications
  - Multiple implementation options
  - Platform-specific adaptations
  - Visual platform selection
  - Default platforms
- User-centric design
  - Focus on user needs
  - Clear user workflows
  - Usability testing
  - Visual feedback
  - Default layouts
- Security-first approach
  - Security requirements in specs
  - Secure by default
  - Regular security reviews
  - Automated security checks
  - Default security settings
- Beginner-friendly approach
  - Step-by-step guidance
  - Visual templates
  - Plain language
  - Interactive tutorials
  - Smart defaults
- Practical focus
  - Working projects
  - Quick results
  - Clear outcomes
  - Default configurations
  - Run instructions
- Iterative development
  - Continuous improvement
  - Regular testing
  - Version tracking
  - Default iterations
  - Progress tracking

### 3. File Relationships

#### Documentation Hierarchy
1. **Primary Source of Truth**
   - SPECIFICATIONS.md (Project Definition)
   - methodology/* (Methodology Source)
     - See methodology/AGILE_SPECFIRST.md for core methodology
     - See methodology/VIBE_USER_GUIDE.md for user guidance
     - See methodology/CURSOR_INTEGRATION.md for IDE integration
     - See methodology/EXAMPLE_SPECIFICATIONS.md for examples
   - docs/framework/* (Framework Documentation)

2. **Generated Documentation**
   - README.md (Generated from SPECIFICATIONS.md)
   - docs/development/* (Generated from .cursorrules)
   - docs/user/* (Generated from user preferences)
   - docs/framework/methodology/* (Mirrored from methodology/*)

3. **Implementation Guide**
   - .cursorrules (Final generated file, contains all implementation details)
     - Generated after all other documentation is in place
     - References all documentation files
     - Contains environment setup
     - Contains package management
     - Contains process workflows
     - Contains templates and defaults

#### Documentation Synchronization Paths
1. **Methodology Files**
   - methodology/AGILE_SPECFIRST.md → docs/framework/methodology/AGILE_SPECFIRST.md
   - methodology/VIBE_USER_GUIDE.md → docs/framework/methodology/VIBE_USER_GUIDE.md
   - methodology/CURSOR_INTEGRATION.md → docs/framework/methodology/CURSOR_INTEGRATION.md
   - methodology/EXAMPLE_SPECIFICATIONS.md → docs/framework/methodology/EXAMPLE_SPECIFICATIONS.md

2. **Framework Documentation**
   - SPECIFICATIONS.md → docs/framework/SPECIFICATION_GUIDE.md
   - SPECIFICATIONS.md → docs/framework/IMPLEMENTATION_GUIDE.md
   - SPECIFICATIONS.md → docs/framework/BEST_PRACTICES.md

3. **Development Documentation**
   - .cursorrules → docs/development/AGILE_INTEGRATION.md
   - .cursorrules → docs/development/TROUBLESHOOTING.md
   - .cursorrules → docs/development/ENVIRONMENT_SETUP.md

4. **User Documentation**
   - SPECIFICATIONS.md → docs/user/PREFERENCES.md
   - SPECIFICATIONS.md → docs/user/STYLE_GUIDE.md
   - SPECIFICATIONS.md → docs/user/WORKFLOW_GUIDE.md

#### Generation Order
1. SPECIFICATIONS.md (Source of Truth)
2. docs/framework/methodology/* (Mirrored Documentation)
3. docs/framework/* (Framework Documentation)
4. docs/development/* (Development Documentation)
5. docs/user/* (User Documentation)
6. README.md (Project Interface)
7. .cursorrules (Implementation Guide)

#### File Dependencies
- .cursorrules depends on all other documentation
- README.md depends on SPECIFICATIONS.md
- docs/* depends on methodology/* and SPECIFICATIONS.md
- All files must reference SPECIFICATIONS.md as source of truth

## Documentation Structure

### Documentation Domains

| Area         | Directory            | Purpose                                      |
|--------------|---------------------|----------------------------------------------|
| Framework    | docs/framework/      | Core methodology, patterns, best practices   |
| Development  | docs/development/    | Project implementation, workflows, stack     |
| Defaults     | docs/defaults/       | Templates and default settings               |
| User         | docs/user/           | User-specific documentation                  |

- **Framework documentation**: Technology-agnostic, covers methodology, patterns, and best practices for all projects.
- **Development documentation**: Technology-specific, covers how to implement projects using the framework.
- **Defaults**: Templates and default settings for quick project setup.
- **User**: User-specific documentation, including communication, preferences, and customizations.

### Directory Structure

project_root/  # Directory containing SPECIFICATIONS.md
├── docs/
│   ├── framework/
│   │   ├── methodology/
│   │   ├── best_practices/
│   │   ├── patterns/
│   │   └── style/
│   ├── development/
│   │   ├── workflow/
│   │   ├── testing/
│   │   ├── setup/
│   │   └── documentation/
│   ├── defaults/
│   │   ├── templates/
│   │   └── settings/
│   └── user/
│       ├── communication/
│       ├── preferences/
│       ├── config/
│       └── custom/
├── scripts/
│   └── check_docs.py  # Documentation validation tool
└── projects/
    └── <project_name>/  # Each project has its own SPECIFICATIONS.md as its root

### File Statuses
- All methodology, best practices, and pattern docs in `framework/` are **REQUIRED**.
- All workflow, testing, and setup docs in `development/` are **REQUIRED**.
- Templates and user-specific files in `defaults/templates/copyright/` and `user/` are **OPTIONAL** or user-generated.

### Copyright Header Rules
- Documentation files (Markdown): **Do NOT** include copyright header at the top.
- Code templates (Python, etc.): **MUST** include: `# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)` at the top.

## Implementation Requirements

### Development Environment
The framework's development environment configuration is defined in `defaults/environment.json`. This file contains all environment-specific settings and is used to generate the appropriate configuration for different contexts.

### Framework Scripts
The framework includes essential scripts in the `scripts/` directory:
- `check_docs.py`: Documentation validation tool
  * Validates documentation structure
  * Checks required files
  * Verifies cross-references
  * Ensures documentation standards
  * Maintains documentation quality

### Documentation Generation
The framework must automatically generate all required documentation files from SPECIFICATIONS.md:

1. Framework Documentation (/docs/framework/)
   - methodology/
     - AGILE_SPECFIRST.md (REQUIRED)
       * Core methodology documentation
       * Agile principles in SpecFirst
       * Methodology phases
       * Key workflows
       * Success metrics
       * Best practices
       * Tools and resources
       * Common challenges and solutions
     - VIBE_USER_GUIDE.md (REQUIRED)
       * Beginner-friendly guide
       * Getting started steps
       * Tips for success
       * Common pitfalls
       * Iterative process
       * Help resources
     - CURSOR_INTEGRATION.md (REQUIRED)
       * Cursor IDE integration details
       * AI assistant features
       * Documentation management
       * Development workflow
       * Best practices
       * Success metrics
       * Common challenges
     - EXAMPLE_SPECIFICATIONS.md (REQUIRED)
       * Example project specification
       * Complete structure
       * Best practices
       * Common patterns
       * Implementation examples
   - best_practices/
     - README.md (REQUIRED)
       * Overview of best practices
       * Key principles
       * Implementation guidelines
     - specification_guide.md (OPTIONAL)
     - implementation_guide.md (OPTIONAL)
     - deployment_guide.md (OPTIONAL)
   - patterns/
     - README.md (REQUIRED)
       * Overview of patterns
       * Pattern categories
       * Usage guidelines
     - api_patterns.md (OPTIONAL)
     - security_patterns.md (OPTIONAL)
     - testing_patterns.md (OPTIONAL)
   - style/
     - README.md (REQUIRED)
       * Style guide overview
       * Code formatting rules
       * Documentation standards
     - python_style.md (OPTIONAL)
     - javascript_style.md (OPTIONAL)
     - html_style.md (OPTIONAL)
     - css_style.md (OPTIONAL)

2. Development Guides (/docs/development/)
   - setup/
     - README.md (REQUIRED)
       * Setup overview
       * Environment requirements
       * Installation steps
     - environment_setup.md (OPTIONAL)
     - project_setup.md (OPTIONAL)
     - tool_setup.md (OPTIONAL)
   - workflow/
     - README.md (REQUIRED)
       * Workflow overview
       * Development process
       * Best practices
     - development_workflow.md (REQUIRED)
     - testing_workflow.md (REQUIRED)
     - deployment_workflow.md (REQUIRED)
   - testing/
     - README.md (REQUIRED)
       * Testing overview
       * Test types
       * Testing guidelines
     - unit_testing.md (REQUIRED)
     - integration_testing.md (REQUIRED)
     - e2e_testing.md (REQUIRED)
   - documentation/
     - README.md (REQUIRED)
       * Documentation overview
       * Writing guidelines
       * Maintenance process

3. User Preferences (/docs/user/)
   - config/
     - README.md (User-generated)
       * Configuration overview
       * Available options
       * Customization guide
   - custom/
     - README.md (User-generatedL)
       * Customization overview
       * Extension points
       * Examples
   - preferences/
     - README.md (REQUIRED)
       * User preferences overview
       * Default settings
       * Customization options
   - communication/
     - README.md (REQUIRED)
       * Communication guidelines
       * Best practices
       * Templates

4. Default Configurations (/docs/defaults/)
   - templates/
     - copyright/
       - project_level.py (REQUIRED)
       - documentation.md (REQUIRED)
       - code_example.py (REQUIRED)
       - README.md (REQUIRED)
     - config/
       - config.json.template (REQUIRED)
     - testing/
       - test_case.py (REQUIRED)
       - test_suite.py (REQUIRED)
       - test_fixture.py (REQUIRED)
     - api/
       - endpoint.py (OPTIONAL)
       - schema.py (OPTIONAL)
       - swagger.yaml (OPTIONAL)
     - security/
       - auth.py (REQUIRED)
       - permissions.py (REQUIRED)
       - security.md (REQUIRED)
     - framework/
       - agile_integration.md (REQUIRED)
       - deployment_guide.md (REQUIRED)
       - expected_behavior.md (REQUIRED)
       - implementation_guide.md (REQUIRED)
       - specification_guide.md (REQUIRED)
       - value_proposition.md (REQUIRED)
   - settings/
     - README.md (OPTIONAL)
     - default_settings.md (OPTIONAL)
     - environment_settings.md (OPTIONAL)
     - tool_settings.md (OPTIONAL)

### Documentation Requirements

1. Required Files (Must Exist)
   - All methodology/*.md files
   - All README.md files in main directories
   - All template files in defaults/templates/copyright/
   - All template files in defaults/templates/config/
   - All template files in defaults/templates/testing/
   - All workflow documentation files
   - All testing documentation files
   - User preference and communication README.md files

2. Optional Files (May Be Generated Later)
   - Best practices detailed guides
   - Pattern implementation details
   - Style guide specifics
   - API and security templates
   - Framework-specific templates
   - Settings and configuration details
   - User-specific configuration files (These are User-generated)

3. File Generation Priority
   - Priority 1: Required files
   - Priority 2: User-facing documentation
   - Priority 3: Development guides
   - Priority 4: Optional templates
   - Priority 5: Extended documentation

4. Documentation Standards
   - All files must include copyright header
   - All files must follow consistent formatting
   - All files must be UTF-8 encoded
   - All files must use proper markdown syntax
   - All files must include version information
   - All files must be properly cross-referenced

### Documentation Update Triggers

1. Framework Documentation Updates
   - New framework features added
   - Best practices updated
   - Implementation patterns changed
   - User feedback incorporated
   - Security requirements modified
   - Style guidelines updated

2. Development Documentation Updates
   - Process improvements made
   - Testing strategies updated
   - New issues identified
   - Solutions documented
   - Agile methodology changes
   - Value proposition updates

3. User Documentation Updates
   - User preferences change
   - Style guidelines updated
   - Communication patterns evolve
   - Quality standards modified
   - Configuration options added
   - Customization features added

4. Default Configuration Updates
   - New default patterns established
   - Technology stack changes
   - Deployment requirements change
   - Security requirements update
   - Template improvements
   - Default settings modified

### Documentation Maintenance Process

1. Update Identification
   - Review change impact
   - Identify affected documents
   - Check cross-references
   - Verify dependencies
   - Plan update sequence

2. Content Updates
   - Make necessary changes
   - Update cross-references
   - Maintain version history
   - Add update dates
   - Document rationale

3. Quality Validation
   - Check for broken links
   - Verify formatting consistency
   - Validate hierarchy
   - Ensure single source of truth
   - Confirm up-to-date information

4. Documentation Standards
   - Consistent formatting
   - Clear hierarchy
   - Version tracking
   - Cross-referencing
   - Update timestamps
   - Change history

### Documentation Quality Metrics

1. Completeness
   - All required sections present
   - No missing information
   - Complete examples
   - Full coverage of topics
   - Comprehensive references

2. Consistency
   - Uniform formatting
   - Consistent terminology
   - Standardized structure
   - Aligned style
   - Matching patterns

3. Accuracy
   - Up-to-date information
   - Correct references
   - Valid examples
   - Accurate instructions
   - Proper cross-references

4. Accessibility
   - Clear organization
   - Easy navigation
   - Logical structure
   - Helpful cross-references
   - Intuitive layout

## User Workflows

### 1. Vibe Coder Workflow
1. Project Initialization
   - Choose project template
   - Set up visual environment
   - Configure basic settings
   - Use default options
   - Run setup

2. Specification Creation
   - Use visual templates
   - Draw interface mockups
   - Write plain language specs
   - Use default specs
   - Run specs

3. Implementation
   - Use visual code generation
   - Follow guided steps
   - Apply visual patterns
   - Use default code
   - Run code

4. Validation
   - Run visual tests
   - Check user experience
   - Get visual feedback
   - Use default tests
   - Run tests

5. Maintenance
   - Update visual docs
   - Refine visual specs
   - Improve visual design
   - Use default updates
   - Run updates

### 2. Experienced Developer Workflow
1. Project Initialization
   - Create project structure
   - Set up documentation
   - Configure environment
   - Customize defaults
   - Run setup

2. Specification Creation
   - Define requirements
   - Create user stories
   - Document constraints
   - Modify defaults
   - Run specs

3. Implementation
   - Generate code
   - Follow patterns
   - Apply best practices
   - Customize code
   - Run code

4. Validation
   - Test against specs
   - Verify requirements
   - Document results
   - Customize tests
   - Run tests

5. Maintenance
   - Update documentation
   - Refine specifications
   - Improve implementation
   - Customize updates
   - Run updates

## Success Criteria

### 1. Documentation Quality
- Complete specifications
- Clear requirements
- Consistent formatting
- Up-to-date content
- Cross-references maintained

### 2. Implementation Quality
- Code matches specifications
- Tests pass
- Security requirements met
- Performance targets achieved
- User experience validated

### 3. Process Efficiency
- Quick setup
- Fast implementation
- Easy maintenance
- Clear workflows
- Automated validation

### 4. User Satisfaction
- Intuitive interface
- Clear guidance
- Working features
- Helpful feedback
- Easy updates

### 5. Documentation Generation
- All required files generated
- Content matches specifications
- Cross-references maintained
- Examples included
- Instructions clear

## Technical Constraints

### 1. Cursor IDE Integration
- Must work in Cursor IDE
- Support AI assistant features
- Real-time documentation
- Code generation
- Error handling

### 2. Cross-Platform Support
- Windows compatibility
- macOS compatibility
- Linux compatibility
- WSL2 support
- Browser compatibility

### 3. Version Control
- Git integration
- Branch management
- Merge strategies
- Version tracking
- Change history

### 4. Security Requirements
- Secure defaults
- API key management
- Input validation
- Error handling
- Access control

## Next Steps

### 1. Documentation
- Create templates
- Write guides
- Add examples
- Update references
- Validate content

### 2. Implementation
- Set up structure
- Create defaults
- Add templates
- Test workflows
- Validate features

### 3. Testing
- Create test cases
- Run validations
- Check security
- Verify performance
- Test user flows

### 4. Deployment
- Package framework
- Create installer
- Write documentation
- Test installation
- Validate setup

## References
- AGILE_SPECFIRST.md - Core methodology documentation
- VIBE_USER_GUIDE.md - Beginner-friendly guide
- CURSOR_INTEGRATION.md - Cursor IDE integration details
- EXAMPLE_SPECIFICATIONS.md - Example project specification

## Continuous Improvement and Integration

### Continuous Integration (CI)
- The CI pipeline MUST run the documentation checker script (`scripts/check_docs.py`) on every commit and before each release.
- This script parses `SPECIFICATIONS.md` to extract all required documentation file paths and checks for their existence in the repository.
- The build MUST fail if any required documentation file is missing.
- This ensures that the documentation structure always matches the specification and prevents incomplete releases.
- Developers MUST update documentation and rerun the script after any change to `SPECIFICATIONS.md` or the documentation structure.

### Continuous Improvement
- Continuous Improvement is an ongoing process of making incremental enhancements to the project, including code quality, documentation, user experience, and team workflows.
- Regular retrospectives, feedback sessions, and process optimizations are essential.
- The methodology and documentation should evolve over time based on lessons learned and user feedback.

## User Preferences
- **docs/user/communication/** and **docs/user/preferences/** contain valid, pre-populated documents that guide communication and user preferences.
- **docs/user/config/** and **docs/user/custom/** are intentionally left empty to allow users and teams to create their own rules and configurations.

# Version Information
- Version: 1.0.0
- Last Updated: 2024-03-19
- Status: Draft 

## Validation Checklist
- [ ] All required sections present
- [ ] Cross-references verified
- [ ] Examples validated
- [ ] Security requirements met
- [ ] User workflows verified 

## Related Documents
- [AGILE_SPECFIRST.md](methodology/AGILE_SPECFIRST.md)
- [VIBE_USER_GUIDE.md](methodology/VIBE_USER_GUIDE.md)
- [CURSOR_INTEGRATION.md](methodology/CURSOR_INTEGRATION.md) 

### Documentation Best Practices
- Documentation Standards
  - Use clear, concise language
  - Include practical examples
  - Maintain consistent formatting
  - Keep cross-references up to date
  - Version documentation with code
- Documentation Review
  - Peer review required for major changes
  - Validate against specifications
  - Check for broken links
  - Verify code examples
  - Update timestamps
- Documentation Maintenance
  - Regular link validation
  - Example code verification
  - Cross-reference updates
  - Version history tracking
  - Change documentation 

## Workflow Definitions
See methodology/AGILE_SPECFIRST.md for detailed workflow definitions and methodology/EXAMPLE_SPECIFICATIONS.md for practical examples of each workflow.

The core workflows include:
1. Initial Project Setup
2. Feature Addition
3. Bug Fix
4. Documentation Update
5. Code Review
6. Testing
7. Security Review

For detailed workflow steps, triggers, and examples, refer to:
- methodology/AGILE_SPECFIRST.md - Core workflow definitions
- methodology/EXAMPLE_SPECIFICATIONS.md - Practical workflow examples
- methodology/VIBE_USER_GUIDE.md - User-focused workflow guidance
- methodology/CURSOR_INTEGRATION.md - IDE-specific workflow details

## Workflow Integration

### Specification Files
- specifications.txt: Initial project definition and requirements
- SPECIFICATIONS.md: Refined, validated specifications
- Both files drive the AI Assistant's behavior and responses

### AI Assistant Role
- Guides users through each workflow
- Maintains specification consistency
- Ensures documentation completeness
- Validates implementation against specs
- Provides real-time feedback and suggestions

### Workflow Triggers
- User actions (new project, feature request, bug report)
- Code changes
- Documentation updates
- Security reviews
- Regular maintenance tasks

### Success Criteria
- Complete, clear specifications
- Consistent documentation
- Validated implementation
- Comprehensive testing
- Secure, maintainable code 