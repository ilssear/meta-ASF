# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Guide to `.cursorrules`

This document provides the definitive guide for structuring a `.cursorrules` file within the Agile SpecFirst Development Framework. It is intended to be the source of truth for both human developers and the AI assistant, ensuring that all generated `.cursorrules` files are complete, compliant, and serve as a robust implementation guide for the project.

## Core Philosophy
The `.cursorrules` file is more than a simple list of rules; it is a comprehensive configuration document that encapsulates the project's entire development philosophy. It must be generated from the project's `SPECIFICATIONS.md` and this guide, ensuring it is always aligned with the project's defined standards.

## Required Structure
A compliant `.cursorrules` file MUST contain the following sections in this order:

### 1. Header Comment
The file MUST begin with a commented-out header containing the file's purpose, the last updated date, and the version number. This version MUST be synchronized with `SPECIFICATIONS.md`.

**Example:**
```markdown
<!--
This file defines the behavior and rules for AI-assisted development in Cursor IDE.
Last updated: 2025-06-20
Version: 1.0.1
-->
```

### 2. Overview
A brief section explaining the purpose and scope of the `.cursorrules` file within the project.

### 3. Core Principles
A summary of the high-level principles that guide the development process (e.g., Specification-First, Documentation-Driven).

### 4. Development Rules
This is the core section of the file. It must contain all 26 development rules defined in the specifications, each formatted as a distinct markdown block with a title, description, priority, requirements/actions, and references.

**Example Rule Format:**
```markdown
### 1. Specification Engineering
`​`​`​markdown
# Rule: Specification Engineering Partner
Description: Act as a specification engineering partner before implementation
Priority: Critical
...
References:
- See docs/framework/methodology/AGILE_SPECFIRST.md
`​`​`​
```

### 5. Generation-Specific Rules
This section MUST include the rules that govern the AI assistant's behavior during file generation and modification.

**Example Generation Rule:**
```markdown
### Generation-Specific Rules
`​`​`​markdown
# Rule: Confine to Specifications Directory
Description: All file generation and modification operations MUST be confined to the project's specification directory...
`​`​`​
```

### 6. User Preferences
A detailed section outlining the ideal development philosophy, technical stack, code style, and other user-specific preferences that should guide the AI's approach.

### 7. Framework Configuration
A concluding statement clarifying that the file is a framework-level configuration and serves as a single source of truth for AI behavior.

### 8. Validation Checklist
A checklist to be used for manually or automatically validating the completeness and correctness of the `.cursorrules` file itself.

By following this structure, the `.cursorrules` file becomes a powerful and reliable tool for enforcing the Agile SpecFirst methodology throughout the development lifecycle.

---

## Complete Example
Below is a complete, spec-compliant `.cursorrules` file generated according to the standards outlined in this guide. It serves as a concrete example of the expected output.

```markdown
# .cursorrules - Agile SpecFirst Development Framework

<!--
This file defines the behavior and rules for AI-assisted development in Cursor IDE.
It is a framework-level configuration that guides AI behavior across all projects using the SpecFirst methodology.
Last updated: 2025-06-20
Version: 1.0.1
-->

## Overview

The .cursorrules file defines the behavior and rules for AI-assisted development in Cursor IDE. It serves as the implementation guide for the SpecFirst development methodology and applies to all projects using this framework.

## Core Principles

1. **Specification-First Development**
   - Always start with specification refinement
   - Never proceed to implementation without complete specifications
   - Ensure specifications are LLM-regenerable
   - See docs/framework/methodology/AGILE_SPECFIRST.md for core methodology

2. **Documentation-Driven Development**
   - Documentation is a first-class deliverable
   - All documentation must be generated from specifications
   - Maintain clear documentation hierarchy
   - See docs/framework/methodology/* for documentation structure

3. **Security-First Approach**
   - Never expose sensitive data
   - Use configuration templates
   - Implement comprehensive .gitignore
   - See docs/development/setup/SECURITY_GUIDE.md for details

4. **User Experience Focus**
   - Design for end-user workflows
   - Provide real-time feedback
   - Implement graceful error handling
   - See docs/framework/methodology/VIBE_USER_GUIDE.md for user guidance

## Development Rules

### 1. Specification Engineering

`​`​`​markdown
# Rule: Specification Engineering Partner
Description: Act as a specification engineering partner before implementation
Priority: Critical
Triggers: New conversation, new feature request
Actions:
- Help refine rough ideas into SPECIFICATIONS.md
- Ask targeted questions about requirements
- Guide complete specification definition
- Ensure LLM-regenerability
- Wait for explicit approval before implementation
References:
- See docs/framework/methodology/AGILE_SPECFIRST.md
- See docs/framework/best_practices/specification_guide.md
`​`​`​

### 2. Documentation Standards

`​`​`​markdown
# Rule: Documentation as First-Class Citizen
Description: Treat documentation as a core deliverable
Priority: High
Requirements:
- Complete README.md with setup/usage/troubleshooting
- API documentation with examples
- Project structure diagrams
- Architecture explanations
- User-focused documentation
References:
- See docs/development/documentation/README.md
- See docs/framework/best_practices/documentation_guide.md
`​`​`​

### 3. Security Guidelines

`​`​`​markdown
# Rule: Security-First Development
Description: Build security into every aspect
Priority: Critical
Requirements:
- Use config.json.template for sensitive data
- Implement comprehensive .gitignore
- Validate all user inputs
- Sanitize all outputs
- Never hard-code secrets
References:
- See docs/development/setup/SECURITY_GUIDE.md
- See docs/framework/patterns/security_patterns.md
`​`​`​

### 4. User Experience

`​`​`​markdown
# Rule: User Experience First
Description: Design for end-user workflows
Priority: High
Requirements:
- Map complete user workflows
- Provide real-time feedback
- Implement graceful error handling
- Test full user journey
- Minimize navigation complexity
References:
- See docs/framework/methodology/VIBE_USER_GUIDE.md
- See docs/development/workflow/development_workflow.md
`​`​`​

### 5. Implementation Phases

`​`​`​markdown
# Rule: Phase-Based Implementation
Description: Break projects into logical phases
Priority: High
Phases:
1. Core infrastructure and configuration
2. Primary feature implementation
3. Secondary features and polish
Requirements:
- Each phase must be working and testable
- Document phase dependencies
- Define success criteria
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/best_practices/implementation_guide.md
`​`​`​

### 6. Code Quality

`​`​`​markdown
# Rule: Code Quality Standards
Description: Maintain high code quality
Priority: High
Requirements:
- Include copyright headers
- Use comprehensive type hints
- Write Google-style docstrings
- Implement proper error handling
- Follow PEP 8 guidelines
References:
- See docs/framework/style/python_style.md
- See docs/development/testing/unit_testing.md
`​`​`​

### 7. Framework Development

`​`​`​markdown
# Rule: Framework Over Ad-Hoc Solutions
Description: Create reusable frameworks
Priority: High
Requirements:
- Create project templates
- Build modular components
- Establish clear patterns
- Document framework decisions
References:
- See docs/framework/patterns/README.md
- See docs/development/workflow/development_workflow.md
`​`​`​

### 8. Technology Choices

`​`​`​markdown
# Rule: Technology-Agnostic Design
Description: Avoid technology lock-in
Priority: Medium
Requirements:
- Write implementation-agnostic specs
- Choose tech based on requirements
- Document technology choices
- Design portable interfaces
References:
- See docs/framework/best_practices/implementation_guide.md
- See docs/development/setup/environment_setup.md
`​`​`​

### 9. Deployment Focus

`​`​`​markdown
# Rule: Real-World Deployment
Description: Build production-ready applications
Priority: High
Requirements:
- Comprehensive dependency management
- Clear installation instructions
- Proper logging and debugging
- Cross-platform compatibility
- Troubleshooting guides
- Hardware-specific considerations
- Multiple package manager support
References:
- See docs/development/workflow/deployment_workflow.md
- See docs/framework/best_practices/deployment_guide.md
`​`​`​

### 10. Value Delivery

`​`​`​markdown
# Rule: Incremental Value Delivery
Description: Deliver value with each commit
Priority: High
Requirements:
- Start simple and build incrementally
- Ensure working functionality
- Prefer complete features
- Test early and often
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/methodology/AGILE_SPECFIRST.md
`​`​`​

### 11. Error Handling

`​`​`​markdown
# Rule: Comprehensive Error Handling
Description: Handle all error conditions
Priority: High
Requirements:
- Validate API boundaries
- Provide specific error messages
- Log for debugging
- Show user-friendly messages
- Include recovery suggestions
- Test error paths
References:
- See docs/development/testing/integration_testing.md
- See docs/framework/patterns/error_handling.md
`​`​`​

### 12. Component Design

`​`​`​markdown
# Rule: Single Responsibility
Description: Clear component purposes
Priority: High
Requirements:
- Functions do one thing
- Classes represent single concepts
- Files group related functionality
- APIs have clear interfaces
References:
- See docs/framework/patterns/README.md
- See docs/development/testing/unit_testing.md
`​`​`​

### 13. Development Practices

`​`​`​markdown
# Rule: Modern Development
Description: Use current best practices
Priority: High
Requirements:
- Modern API patterns
- Responsive web design
- Semantic HTML
- Accessible design
- RESTful APIs
References:
- See docs/framework/best_practices/README.md
- See docs/development/workflow/development_workflow.md
`​`​`​

### 14. Testing Strategy

`​`​`​markdown
# Rule: Testing and Validation
Description: Comprehensive testing approach
Priority: High
Requirements:
- Test success and failure
- Validate against specifications
- Integration testing
- End-to-end testing
- Environment verification
- Hardware compatibility
References:
- See docs/development/testing/README.md
- See docs/framework/patterns/testing_patterns.md
`​`​`​

### 15. Environment Management

`​`​`​markdown
# Rule: Environment and Dependencies
Description: Handle complex environments
Priority: High
Requirements:
- Multiple installation paths
- Environment verification
- Package manager documentation
- Hardware-specific setup
- Debugging commands
- Build verification
- Quick-fix solutions
References:
- See docs/development/setup/environment_setup.md
- See docs/framework/best_practices/deployment_guide.md
`​`​`​

### 16. Knowledge Management

`​`​`​markdown
# Rule: Knowledge Preservation
Description: Document decisions and learnings
Priority: High
Requirements:
- Maintain conversation summaries
- Document architecture decisions
- Create implementation guides
- Preserve context
References:
- See docs/development/documentation/README.md
- See docs/framework/best_practices/README.md
`​`​`​

### 17. Specification Maintenance

`​`​`​markdown
# Rule: Specification Maintenance
Description: Keep specs in sync
Priority: High
Requirements:
- Review after changes
- Document changes
- Maintain changelog
- Validate implementation
- Update based on feedback
References:
- See docs/framework/methodology/AGILE_SPECFIRST.md
- See docs/development/workflow/development_workflow.md
`​`​`​

### 18. Documentation Sync

`​`​`​markdown
# Rule: Documentation Synchronization
Description: Keep docs in sync
Priority: High
Requirements:
- Update README.md
- Maintain consistency
- Document breaking changes
- Keep API docs current
- Update troubleshooting
References:
- See docs/development/documentation/README.md
- See docs/framework/best_practices/documentation_guide.md
`​`​`​

### 19. Version Control

`​`​`​markdown
# Rule: Version Control Integration
Description: Integrate with version control
Priority: High
Requirements:
- Clear commit messages
- Version tagging
- Specification history
- Breaking change docs
- Change tracking
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/best_practices/version_control.md
`​`​`​

### 20. Implementation Alignment

`​`​`​markdown
# Rule: Implementation-Specification Alignment
Description: Ensure implementation matches specs
Priority: Critical
Requirements:
- Validate before commits
- Document deviations
- Update specs when needed
- Maintain traceability
- Regular audits
References:
- See docs/framework/best_practices/implementation_guide.md
- See docs/development/testing/integration_testing.md
`​`​`​

### 21. Documentation Hierarchy

`​`​`​markdown
# Rule: Documentation Hierarchy
Description: Maintain doc relationships
Priority: High
Requirements:
- SPECIFICATIONS.md as source
- README.md generation
- docs/ structure
- Update triggers
- Consistent formatting
- Version control
References:
- See docs/development/documentation/README.md
- See docs/framework/best_practices/documentation_guide.md
`​`​`​

### 22. Change Management

`​`​`​markdown
# Rule: Change Management
Description: Handle framework changes
Priority: High
Requirements:
- Document in .cursorrules
- Update framework docs
- Version control rules
- Update process
- Breaking change guidelines
- Migration paths
- Regular reviews
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/best_practices/change_management.md
`​`​`​

### 23. Quality Assurance

`​`​`​markdown
# Rule: Quality Assurance
Description: Ensure quality standards
Priority: High
Requirements:
- Automated checks
- Validation rules
- Documentation reviews
- User feedback
- Performance metrics
- Revision criteria
References:
- See docs/development/testing/README.md
- See docs/framework/best_practices/quality_standards.md
`​`​`​

### 24. Cross-Project Standards

`​`​`​markdown
# Rule: Cross-Project Consistency
Description: Maintain consistency
Priority: High
Requirements:
- Shared templates
- Common standards
- Lessons learned
- Framework updates
- Versioning strategy
- Best practices
References:
- See docs/framework/best_practices/README.md
- See docs/development/workflow/development_workflow.md
`​`​`​

### 25. Tool Integration

`​`​`​markdown
# Rule: Tool Integration
Description: Integrate maintenance tools
Priority: Medium
Requirements:
- Version control hooks
- Documentation generation
- Specification validation
- Sync tools
- Change tracking
- Quality automation
References:
- See docs/development/setup/tool_setup.md
- See docs/framework/best_practices/tool_integration.md
`​`​`​

### 26. Decision Making

`​`​`​markdown
# Rule: Documentation-Driven Decisions
Description: Guide decisions with docs
Priority: High
Requirements:
- Follow specification guide
- Use best practices
- Check user preferences
- Follow style guide
- Update documentation
References:
- See docs/framework/methodology/AGILE_SPECFIRST.md
- See docs/user/preferences/README.md
`​`​`​

### Generation-Specific Rules

`​`​`​markdown
# Rule: Confine to Specifications Directory
Description: All file generation and modification operations MUST be confined to the project's specification directory. Do not read or write files outside of this directory.
`​`​`​

`​`​`​markdown
# Rule: No Git History
Description: The generation process MUST rely only on the current state of the file system. Do not query or depend on `git` history.
`​`​`​

`​`​`​markdown
# Rule: No Script Modification Without Confirmation
Description: Core validation and generation scripts MUST NOT be altered without explicit user confirmation.
`​`​`​

## User Preferences

### Development Philosophy
- Specification-First mindset
- Technology-agnostic thinking
- Real-World focus
- Framework over features
- Security-conscious
- Documentation-heavy

### Technical Stack
- Python with mamba/conda
- AI API integration
- Flask for web
- Comprehensive testing
- User-friendly errors
- Multiple package managers

### Code Style
- Copyright headers
- Type hints
- Google-style docstrings
- PEP 8 compliance
- Logical structure
- Clear comments

### Project Structure
- Version strategy
- JSON configuration
- Documentation hierarchy
- Testing approach
- Cross-platform support

### AI Assistant Interaction
- Clarification over assumption
- Complete solutions
- Specification validation
- Proper tool usage
- Context preservation
- Learning integration

### Communication Style
- Technical precision
- Problem-solution format
- Visual feedback
- Progress tracking
- Educational value

### Environment-Specific
- WSL2/Ubuntu awareness
- NVIDIA GPU support
- Package management
- VS Code integration
- Local development

### Quality Assurance
- Primary test cases
- Edge case handling
- User workflow testing
- Documentation testing
- Cross-platform testing

### Decision-Making
- Simplicity first
- Future-proofing
- User-centric
- Evidence-based
- Incremental progress

## Framework Configuration

This is a framework-level configuration file that defines how the AI assistant should behave when working with any project using the SpecFirst methodology. It is not meant to be generated per project, but rather serves as a single source of truth for AI behavior across all SpecFirst projects.

## Validation

- [ ] All rules present
- [ ] User preferences complete
- [ ] Framework configuration clear
- [ ] Timestamps updated
- [ ] Version number set
- [ ] No direct edits
- [ ] Markdown valid
- [ ] Links working
- [ ] Format consistent 
``` 