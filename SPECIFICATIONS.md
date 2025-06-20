# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Framework

# Version Information
This section defines the canonical version and update timestamp for the framework. These values serve as the source of truth for all versioning across the framework's documentation and generated artifacts. When this section is updated, the changes should be propagated to all relevant files, particularly the header of the `.cursorrules` implementation guide.

- **Version**: `1.0.1`
- **Last Updated**: `2025-06-20`
- **Status**: Active

## Project Overview
The SpecFirst Framework is a comprehensive development methodology and toolset that emphasizes **specification-driven development**, **AI/LLM code generation**, and **continuous PERA cycles**. The framework provides language-agnostic patterns, best practices, and validation tools to help developers of all skill levels create high-quality software efficiently through specification → generation → review → refinement cycles.

### Purpose
- Provide a specification-driven development framework with AI/LLM integration
- Support developers from beginners (Vibe Coders) to advanced teams
- Enable continuous improvement through PERA cycles
- Deliver validation tools for specification-driven development
- Maintain documentation as a first-class deliverable
- Enable rapid feedback loops and continuous improvement
- Use TDD as a quality assurance tool during code generation and debugging
- Emphasize incremental development after initial code generation

## Core Concepts

### What is SpecFirst?
SpecFirst is a development framework that emphasizes:
1. **Specification-First Development**: Complete specifications before implementation
2. **AI/LLM-Driven Code Generation**: Use AI to generate code from specifications
3. **User Review and Feedback**: Continuous user validation of generated code
4. **Specification Refinement**: Iterative improvement of specifications based on feedback
5. **PDCA Cycle Integration**: Plan-Do-Check-Act cycle for continuous improvement
6. **Language-Agnostic Design**: Patterns that work across all programming languages

### Framework Philosophy
- **Specification as Source of Truth**: All development starts with and is driven by specifications
- **AI/LLM Code Generation**: Use AI to generate code from detailed specifications
- **User-Centric Validation**: User feedback drives specification refinement
- **PERA Methodology**: Continuous improvement through specification → generation → review → refinement cycles
- **Incremental Development**: After initial generation, make small, focused changes (15 min - 2 hours)
- **Cross-Platform Compatibility**: Technology-agnostic specifications with language-specific implementations
- **Beginner-Friendly**: Accessible to non-technical users while powerful for experts

### Key Principles
- **Specification-Driven**: All development starts with complete specifications
- **AI/LLM Integration**: Use AI to generate code from specifications
- **User Feedback Loops**: Continuous user review and feedback
- **Specification Refinement**: Iterative improvement of specifications
- **PERA Cycles**: Plan-Execute-Report/Review-Adjust for continuous improvement
- **Incremental Changes**: Small, focused changes after initial generation
- **Error Prevention**: Avoid common development pitfalls

### Development Workflow
The SpecFirst framework follows a continuous PERA cycle:

1. **Plan (Specification)**: Create or refine complete specifications
2. **Execute (AI Generation)**: Use AI/LLM to generate code from specifications
3. **Report/Review (User Review)**: User reviews generated code and provides feedback
4. **Adjust (Specification Refinement)**: Refine specifications based on feedback

This cycle repeats continuously, with each iteration improving both specifications and generated code. After the initial code generation, subsequent changes should be incremental (15 minutes to 2 hours) to maintain rapid feedback loops.

### TDD Integration
While SpecFirst is specification-driven, **Test-Driven Development (TDD)** is used during the code generation and debugging phases:

- **TDD for Code Generation**: When AI generates code, TDD ensures quality and correctness
- **TDD for Debugging**: When issues arise, TDD helps identify and fix problems
- **TDD for Refinement**: When specifications are refined, TDD validates the changes

TDD serves as a quality assurance tool within the SpecFirst methodology, not as the primary driver.

## Target Users

### 1. Vibe Coders (Beginners)
- Creative individuals with great ideas but no coding experience
- Need intuitive, visual approach to software development
- Want to focus on the "vibe" and user experience
- Prefer plain language over technical terms
- Value step-by-step guidance and templates
- Need working projects quickly with smart defaults

### 2. Intermediate Developers
- Have basic coding experience but want structured approach
- Need guidance on TDD and incremental development
- Want to improve code quality and reduce rework
- Require clear documentation for maintenance
- Can leverage advanced features and frameworks
- Need validation tools and best practices

### 3. Advanced Teams
- Experienced development teams seeking methodology
- Need enterprise-level testing and validation
- Require comprehensive tooling and automation
- Want property-based testing and advanced patterns
- Need integration testing and CI/CD support
- Require team collaboration and process improvement

### 4. Project Managers
- Need clear project scope definition and tracking
- Want measurable success criteria and progress tracking
- Require team coordination and resource planning
- Need risk management and quality assurance
- Want working demos and stakeholder communication
- Require process documentation and best practices

## Core Components

### 1. Documentation Structure
The framework's documentation is organized into four main domains:

- **Framework Documentation** (`docs/framework/`): Core methodology, patterns, and best practices (technology-agnostic)
- **Development Documentation** (`docs/development/`): Project implementation, workflows, and stack-specific guides (technology-specific)
- **Defaults** (`docs/defaults/`): Templates and default settings for quick project setup
- **User** (`docs/user/`): User-specific documentation, including communication, preferences, and customizations

### 2. Key Files
- **SPECIFICATIONS.md**: This file - the source of truth for the framework
- **.cursorrules**: AI assistant configuration and implementation guide
- **README.md**: User interface and getting started guide
- **LICENSE**: GPL 3.0 license file
- **.gitignore**: Version control exclusions
- **docs/framework/**: Core methodology and patterns
- **docs/development/**: Implementation guides and workflows
- **docs/defaults/**: Templates and default settings
- **docs/user/**: User-specific documentation

### 3. Validation Tools
- **validate_project.py**: Determines project development stage
- **check_docs.py**: Validates documentation completeness
- **check_structure.py**: Validates project structure integrity

## Implementation Requirements

### Source Files
The framework must generate the following source files from this specification:

1. **.cursorrules** (REQUIRED)
   - AI assistant configuration and behavior rules
   - Development methodology and best practices
   - Specification-driven development and PDCA cycle guidelines
   - TDD as quality assurance tool
   - Validation and quality assurance rules
   - User preference handling
   - Framework-specific rules and patterns

2. **README.md** (REQUIRED)
   - Framework overview and key features
   - Getting started guide with installation instructions
   - Usage examples and validation tools
   - Documentation structure and navigation
   - Development workflow with PDCA cycles and best practices
   - Troubleshooting and support information

3. **LICENSE** (REQUIRED)
   - GPL 3.0 license text
   - Copyright information
   - License terms and conditions
   - Usage rights and restrictions

4. **.gitignore** (REQUIRED)
   - Python-specific exclusions
   - IDE and editor files
   - Build artifacts and temporary files
   - Environment-specific files
   - Security-sensitive files

### Documentation Files

#### Framework Documentation (`docs/framework/`)

1. **README.md** (REQUIRED)
   - Framework overview and core methodology
   - Specification-driven development and PDCA cycles
   - Language-specific test framework recommendations
   - Common patterns and best practices
   - Getting started guide and references

2. **methodology/** (REQUIRED)
   - **AGILE_SPECFIRST.md**: Core methodology combining Agile and SpecFirst
   - **CURSOR_INTEGRATION.md**: Integration with Cursor IDE
   - **VIBE_USER_GUIDE.md**: User-focused development guide
   - **EXAMPLE_SPECIFICATIONS.md**: Example specifications
   - **SPECIFICATION_VALIDATION.md**: Validation principles

3. **best_practices/** (REQUIRED)
   - **README.md**: Overview of best practices with specification-driven development focus
   - **implementation_guide.md**: Step-by-step implementation guide
   - **specification_guide.md**: Specification writing guide
   - **test_frameworks_guide.md**: Comprehensive testing framework recommendations

4. **patterns/** (REQUIRED)
   - **README.md**: Overview of patterns with specification-driven development and PDCA cycles
   - **api_patterns.md**: API design patterns
   - **security_patterns.md**: Security patterns
   - **testing_patterns.md**: Testing patterns

5. **style/** (REQUIRED)
   - **README.md**: Style guide overview with specification-driven development guidelines
   - **python_style.md**: Python-specific style guide

#### Development Documentation (`docs/development/`)

1. **README.md** (REQUIRED)
   - Development documentation overview
   - Implementation workflows and stack-specific guides
   - Testing procedures and validation tools
   - Setup and configuration guides

2. **workflow/** (REQUIRED)
   - **README.md**: Workflow overview
   - **development_workflow.md**: Development process with specification-driven development and PDCA cycles
   - **testing_workflow.md**: Testing process and validation
   - **deployment_workflow.md**: Deployment process

3. **testing/** (REQUIRED)
   - **README.md**: Testing overview
   - **unit_testing.md**: Unit testing with TDD as quality assurance
   - **integration_testing.md**: Integration testing
   - **e2e_testing.md**: End-to-end testing
   - **security_testing.md**: Security testing

4. **setup/** (REQUIRED)
   - **README.md**: Setup overview
   - **environment_setup.md**: Environment setup
   - **project_setup.md**: Project setup
   - **tool_setup.md**: Tool setup

5. **documentation/** (REQUIRED)
   - **README.md**: Documentation overview and writing guidelines

#### Defaults Documentation (`docs/defaults/`)

1. **README.md** (REQUIRED)
   - Defaults overview and templates
   - Settings and configuration options
   - Quick project setup guides

2. **templates/** (REQUIRED)
   - **copyright/**: Copyright templates and examples
   - **config/**: Configuration templates
   - **testing/**: Testing templates
   - **api/**: API templates
   - **security/**: Security templates
   - **framework/**: Framework templates

3. **settings/** (REQUIRED)
   - **README.md**: Settings overview
   - **default_settings.md**: Default settings
   - **environment_settings.md**: Environment settings
   - **tool_settings.md**: Tool settings

#### User Documentation (`docs/user/`)

1. **README.md** (REQUIRED)
   - User documentation overview
   - Communication and preferences
   - Customization and configuration

2. **communication/** (REQUIRED)
   - **README.md**: Communication guidelines and best practices

3. **preferences/** (REQUIRED)
   - **README.md**: User preferences and customization options

4. **config/** (OPTIONAL)
   - User-generated configuration documentation

5. **custom/** (OPTIONAL)
   - User-generated customization documentation

### Testing Requirements

#### Test-Driven Development (TDD) as Quality Assurance
Within the SpecFirst methodology, TDD serves as a quality assurance tool during code generation and debugging phases:

- **TDD for Code Generation**: When AI generates code from specifications, TDD ensures quality and correctness
- **TDD for Debugging**: When issues arise in generated code, TDD helps identify and fix problems
- **TDD for Refinement**: When specifications are refined, TDD validates that changes maintain functionality
- **TDD for Validation**: Tests validate that generated code matches specification requirements

TDD requirements within SpecFirst:
- Tests must validate both success and failure cases
- Tests must be comprehensive and cover edge cases
- Test coverage should aim for 90% or higher
- Tests must be fast, independent, and repeatable
- Tests must align with specification requirements

#### Testing Framework Recommendations
The framework must provide language-specific testing framework recommendations:

**For Beginners (Vibe Coders):**
- JavaScript: Jest (easy setup, great documentation)
- Python: pytest (simple syntax, powerful features)
- Java: JUnit 5 (industry standard, great IDE support)
- C#: xUnit (modern, fast, great .NET integration)
- Ruby: RSpec (readable syntax, good for BDD)
- Go: Built-in testing (simple, no dependencies)
- Rust: Built-in testing (simple, no dependencies)

**For Intermediate Developers:**
- JavaScript: Vitest (fast, modern, Vite integration)
- Python: pytest + pytest-cov (comprehensive testing)
- Java: JUnit 5 + Mockito (advanced mocking)
- C#: xUnit + Moq (advanced mocking)
- Ruby: RSpec + FactoryBot (advanced features)
- Go: testify (comprehensive utilities)
- Rust: Built-in + proptest (property-based testing)

**For Advanced Teams:**
- JavaScript: Jest + Testing Library (comprehensive ecosystem)
- Python: pytest + hypothesis (property-based testing)
- Java: JUnit 5 + TestContainers (integration testing)
- C#: xUnit + FluentAssertions (expressive assertions)
- Ruby: RSpec + Cucumber (BDD approach)
- Go: testify + testcontainers (comprehensive testing)
- Rust: Built-in + proptest (property-based testing)

#### Cross-Platform Testing Tools
- **Playwright**: End-to-end testing for web apps
- **Cypress**: Frontend testing with great UI
- **Selenium**: Cross-browser testing
- **Postman**: API testing
- **Insomnia**: API testing and development

### Validation Requirements

#### Automated Validation
- **validate_project.py**: Determines project development stage (1-6)
- **check_docs.py**: Validates documentation completeness
- **check_structure.py**: Validates project structure integrity

#### Validation Checklist
- [ ] All tests pass
- [ ] No regressions introduced
- [ ] Implementation matches specifications
- [ ] Documentation is complete and accurate
- [ ] Code follows style guidelines
- [ ] Error handling is comprehensive
- [ ] User feedback incorporated
- [ ] Changes are properly documented

### Security Requirements

#### Security-First Approach
- Never expose sensitive data in documentation or code
- Use configuration templates for sensitive information
- Implement comprehensive .gitignore patterns
- Validate all user inputs and sanitize outputs
- Follow secure coding practices in all examples
- Include security testing in validation processes

#### Security Patterns
- Authentication and authorization patterns
- Data protection and encryption
- Input validation and sanitization
- Secure communication protocols
- Error handling without information disclosure

### Performance Requirements

#### Framework Performance
- Documentation generation must be fast (< 30 seconds)
- Validation scripts must complete quickly (< 10 seconds)
- Test execution should be optimized for speed
- Documentation should be easily searchable and navigable

#### User Experience
- Clear, concise documentation
- Intuitive navigation and structure
- Fast loading and responsive design
- Accessible to users with different skill levels
- Comprehensive examples and tutorials

## File Generation Order

### Phase 1: Core Framework Files
1. **LICENSE** - GPL 3.0 license file
2. **.gitignore** - Version control exclusions
3. **docs/framework/README.md** - Framework overview

### Phase 2: Framework Documentation
1. **docs/framework/methodology/** - Core methodology files
2. **docs/framework/best_practices/** - Best practices with specification-driven development focus
3. **docs/framework/patterns/** - Implementation patterns
4. **docs/framework/style/** - Style guidelines

### Phase 3: Development Documentation
1. **docs/development/README.md** - Development overview
2. **docs/development/workflow/** - Development workflows with PDCA cycles
3. **docs/development/testing/** - Testing procedures with TDD as quality assurance
4. **docs/development/setup/** - Setup guides
5. **docs/development/documentation/** - Documentation guides

### Phase 4: Defaults and User Documentation
1. **docs/defaults/** - Templates and default settings
2. **docs/user/** - User-specific documentation

### Phase 5: Main Interface Files
1. **README.md** - User interface and getting started guide
2. **.cursorrules** - AI assistant configuration (generated last)

## Success Criteria

### Framework Success Metrics
1. **Documentation Completeness**: All required files generated and up-to-date
2. **Language Coverage**: Support for 7+ programming languages with specific recommendations
3. **Skill Level Support**: Clear guidance for beginners, intermediate, and advanced developers
4. **Specification-Driven Development**: Comprehensive specification patterns and examples
5. **AI/LLM Integration**: Effective code generation from specifications
6. **PERA Cycle Implementation**: Continuous improvement through specification → generation → review → refinement
7. **Incremental Development**: Small, focused changes after initial generation
8. **TDD Quality Assurance**: TDD effectively validates generated code and specification alignment
9. **User Adoption**: Framework is accessible and useful for target user groups
10. **Maintainability**: Clear structure and update processes for ongoing maintenance

### Quality Assurance
1. **Specification Alignment**: All generated files align with this specification
2. **Cross-Reference Accuracy**: All internal links and references are valid
3. **Consistency**: Consistent formatting and style across all documentation
4. **Completeness**: All required sections and content are present
5. **Accuracy**: All examples and code snippets are correct and functional
6. **Accessibility**: Documentation is accessible to users of all skill levels

### Validation Requirements
1. **Automated Checks**: All validation scripts pass without errors
2. **Documentation Validation**: All required documentation files exist and are complete
3. **Structure Validation**: Project structure follows defined patterns
4. **Content Validation**: All content meets quality and completeness standards
5. **Cross-Reference Validation**: All internal links and references are valid

## Maintenance and Updates

### Update Triggers
1. **Framework Version Updates**: When version number or timestamp changes
2. **New Language Support**: When adding support for new programming languages
3. **Testing Framework Updates**: When new testing frameworks become available
4. **User Feedback**: When incorporating user feedback and improvements
5. **Security Updates**: When security requirements or patterns change
6. **Best Practice Evolution**: When development best practices evolve

### Update Process
1. **Specification Review**: Review and update this specification first
2. **Documentation Generation**: Regenerate all documentation from updated specification
3. **Validation**: Run all validation scripts to ensure quality
4. **Testing**: Test all examples and code snippets
5. **Review**: Review generated content for accuracy and completeness
6. **Deployment**: Deploy updated framework with proper versioning

### Version Control
1. **Clear Commit Messages**: Descriptive commit messages for all changes
2. **Feature Branches**: Use feature branches for major updates
3. **Version Tagging**: Tag releases with appropriate version numbers
4. **Change Documentation**: Document all changes in version history
5. **Rollback Capability**: Maintain ability to rollback to previous versions

## References

### External Resources
- [GPL 3.0 License](https://www.gnu.org/licenses/gpl-3.0.en.html)
- [Jest Documentation](https://jestjs.io/)
- [pytest Documentation](https://docs.pytest.org/)
- [JUnit 5 Documentation](https://junit.org/junit5/)
- [xUnit Documentation](https://xunit.net/)
- [RSpec Documentation](https://rspec.info/)
- [Go Testing Documentation](https://golang.org/pkg/testing/)
- [Rust Testing Documentation](https://doc.rust-lang.org/book/ch11-00-testing.html)
- [Playwright Documentation](https://playwright.dev/)
- [Cypress Documentation](https://docs.cypress.io/)

### Internal References
- [Framework Methodology](docs/framework/methodology/AGILE_SPECFIRST.md)
- [Vibe User Guide](docs/framework/methodology/VIBE_USER_GUIDE.md)
- [Cursor Integration](docs/framework/methodology/CURSOR_INTEGRATION.md)
- [Testing Framework Guide](docs/framework/best_practices/test_frameworks_guide.md)
- [Development Workflow](docs/development/workflow/development_workflow.md)
- [Unit Testing Guide](docs/development/testing/unit_testing.md)

## Version History

- **v1.0.0** (2025-06-03): Initial framework specification
- **v1.0.1** (2025-06-20): Added TDD, incremental development, and validation features 