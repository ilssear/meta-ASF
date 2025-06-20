# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Cursor Rules Specification

## Overview
This document defines the definitive guide for structuring a `.cursorrules` file. It serves as the source of truth for `.cursorrules` generation and ensures consistency across all SpecFirst projects.

## Purpose
The `.cursorrules` file is the master set of rules for the AI assistant, containing all implementation details, development methodology, and project-specific guidelines.

## Required Structure

### 1. Header Section
```markdown
# .cursorrules - [Project Name] Development Framework

<!--
This file defines the behavior and rules for AI-assisted development in Cursor IDE.
It is a framework-level configuration that guides AI behavior across all projects using the [Methodology] methodology.
Last updated: [Date]
Version: [Version]
-->
```

### 2. Overview Section
- Project overview and purpose
- Core methodology description
- Key principles and values
- Target user groups

### 3. Core Principles Section
- Specification-first development
- Documentation-driven implementation
- User-centric validation
- Iterative refinement
- Cross-platform compatibility
- Beginner-friendly approach
- Practical focus
- Smart defaults

### 4. Development Rules Section
Each rule must include:
- Rule name and description
- Priority level (Critical, High, Medium, Low)
- Triggers and conditions
- Required actions
- References to relevant documentation

### 5. User Preferences Section
- Development philosophy
- Technical stack preferences
- Code style guidelines
- Project structure preferences
- AI assistant interaction style
- Communication preferences
- Environment-specific settings
- Quality assurance standards

### 6. Framework Configuration Section
- Framework-level configuration details
- Cross-project standards
- Version control integration
- Tool integration requirements
- Decision-making guidelines

### 7. Validation Section
- Quality assurance checklist
- Documentation standards
- Implementation validation
- Cross-reference requirements
- Change management process

## Content Requirements

### Development Rules
Must include rules for:
1. Specification Engineering
2. Documentation Standards
3. Security Guidelines
4. User Experience
5. Implementation Phases
6. Code Quality
7. Framework Development
8. Technology Choices
9. Deployment Focus
10. Value Delivery
11. Error Handling
12. Component Design
13. Development Practices
14. Testing Strategy
15. Environment Management
16. Knowledge Management
17. Specification Maintenance
18. Documentation Sync
19. Version Control
20. Implementation Alignment

### User Preferences
Must include:
- Development philosophy
- Technical stack preferences
- Code style guidelines
- Project structure preferences
- AI assistant interaction style
- Communication preferences
- Environment-specific settings
- Quality assurance standards
- Decision-making approach

### Framework Configuration
Must include:
- Framework-level configuration
- Cross-project standards
- Version control integration
- Tool integration
- Decision-making guidelines
- Change management
- Quality assurance
- Cross-project consistency
- Tool integration
- Decision making

## Generation Process

### Dependencies
- `.cursorrules` depends on all other documentation
- Must be generated after all other files are in place
- References all documentation files
- Contains consolidated project rules and preferences

### Generation Order
1. SPECIFICATIONS.md (Source of Truth)
2. docs/framework/methodology/* (Mirrored Documentation)
3. docs/framework/* (Framework Documentation)
4. docs/development/* (Development Documentation)
5. docs/user/* (User Documentation)
6. README.md (Project Interface)
7. .cursorrules (Implementation Guide - Generated Last)

### Validation Requirements
- All rules must be present and complete
- User preferences must be comprehensive
- Framework configuration must be clear
- All timestamps must be updated
- Version numbers must be set
- No direct edits allowed
- Markdown must be valid
- All links must be working
- Format must be consistent

## File Relationships

### Input Files
- SPECIFICATIONS.md: Project definition and requirements
- methodology/*.md: Core methodology documentation
- docs/framework/*: Framework documentation
- docs/development/*: Development guides
- docs/user/*: User documentation
- docs/defaults/*: Templates and defaults

### Output File
- .cursorrules: Master implementation guide

### Cross-References
- All documentation files must be referenced
- Internal links must be valid
- File paths must be correct
- Version information must be consistent

## Quality Standards

### Completeness
- All required sections present
- No missing information
- Complete examples
- Full coverage of topics
- Comprehensive references

### Consistency
- Uniform formatting
- Consistent terminology
- Standardized structure
- Aligned style
- Matching patterns

### Accuracy
- Up-to-date information
- Correct references
- Valid examples
- Accurate instructions
- Proper cross-references

### Accessibility
- Clear organization
- Easy navigation
- Logical structure
- Helpful cross-references
- Intuitive layout

## Maintenance

### Update Triggers
- Framework version updates
- New methodology features
- User feedback incorporation
- Security requirement changes
- Best practice evolution
- Tool integration updates

### Update Process
1. Review change impact
2. Identify affected sections
3. Update content
4. Validate cross-references
5. Test generation process
6. Update version information

### Version Control
- Clear commit messages
- Feature branches for major updates
- Version tagging
- Change documentation
- Rollback capability

## References
- [AGILE_SPECFIRST.md](AGILE_SPECFIRST.md)
- [VIBE_USER_GUIDE.md](VIBE_USER_GUIDE.md)
- [CURSOR_INTEGRATION.md](CURSOR_INTEGRATION.md)
- [EXAMPLE_SPECIFICATIONS.md](EXAMPLE_SPECIFICATIONS.md)
- [SPECIFICATION_VALIDATION.md](SPECIFICATION_VALIDATION.md) 


## Full working Cursor Rules Example

This document provides a comprehensive example of Cursor Rules implementation for the Agile SpecFirst Development Framework. It serves as a reference for setting up and maintaining cursor rules across projects.

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
   - Ensure specifications are maintainable and LLM-regenerable
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

5. **Incremental Development**
   - After initial code generation, make small, focused changes (15 min - 2 hours)
   - Update documentation at every cycle
   - Get user feedback on each increment
   - Validate each change before proceeding

## Development Rules

### 1. Specification Engineering

```markdown
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
```

### 2. Documentation Standards

```markdown
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
```

### 3. Security Guidelines

```markdown
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
```

### 4. User Experience

```markdown
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
```

### 5. Implementation Phases

```markdown
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
```

### 6. Code Quality

```markdown
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
```

### 7. Framework Development

```markdown
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
```

### 8. Technology Choices

```markdown
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
```

### 9. Deployment Focus

```markdown
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
```

### 10. Value Delivery

```markdown
# Rule: Incremental Value Delivery
Description: Deliver value with each commit
Priority: High
Requirements:
- Start simple and build incrementally
- After initial generation, make small, focused changes (15 min - 2 hours)
- Ensure working functionality
- Prefer complete features
- Test early and often
- Update documentation at every cycle
- Get user feedback on each increment
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/methodology/AGILE_SPECFIRST.md
```

### 11. Error Handling

```markdown
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
```

### 12. Component Design

```markdown
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
```

### 13. Development Practices

```markdown
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
```

### 14. Testing Strategy

```markdown
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
```

### 15. Environment Management

```markdown
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
```

### 16. Knowledge Management

```markdown
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
```

### 17. Specification Maintenance

```markdown
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
```

### 18. Documentation Sync

```markdown
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
```

### 19. Version Control

```markdown
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
```

### 20. Implementation Alignment

```markdown
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
```

### 21. Documentation Structure

```markdown
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
```

### 22. Change Management

```markdown
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
```

### 23. Quality Assurance

```markdown
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
```

### 24. Cross-Project Standards

```markdown
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
```

### 25. Tool Integration

```markdown
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
```

### 26. Decision Making

```markdown
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
```

### 27. Test-Driven Development

```markdown
# Rule: Test-First Development
Description: Write tests before implementation
Priority: High
Requirements:
- Write failing test before new feature
- Test both success and failure cases
- Validate against specifications
- Run tests after each change
- Use tests to guide implementation
- Follow Red-Green-Refactor cycle
- Test edge cases and error conditions
References:
- See docs/development/testing/unit_testing.md
- See docs/framework/methodology/AGILE_SPECFIRST.md
```

### 28. Incremental Changes

```markdown
# Rule: Small, Focused Changes
Description: Make one small change at a time
Priority: High
Requirements:
- Change one thing at a time
- Test each change before proceeding
- Validate against specifications
- Get user feedback on each increment
- Document what was changed and why
- Break large changes into phases
- Each phase must be testable independently
References:
- See docs/development/workflow/development_workflow.md
- See docs/framework/methodology/AGILE_SPECFIRST.md
```

### 29. Change Validation

```markdown
# Rule: Validate Before Committing
Description: Ensure changes meet specifications
Priority: Critical
Requirements:
- Run validation scripts after changes
- Test both positive and negative cases
- Verify no regressions introduced
- Check that changes align with methodology
- Get explicit approval for major changes
- Use validation checklist before committing
- Document any exceptions or deviations
References:
- See scripts/validate_project.py
- See scripts/check_docs.py
- See docs/framework/best_practices/implementation_guide.md
```

### 30. User Feedback Integration

```markdown
# Rule: Rapid Feedback Loops
Description: Get feedback early and often
Priority: High
Requirements:
- Seek feedback at every stage
- Use feedback to refine specifications
- Incorporate feedback before closing features
- Shorten feedback loops to catch issues early
- Test with real users when possible
- Document feedback and decisions
References:
- See docs/framework/methodology/AGILE_SPECFIRST.md
- See docs/development/workflow/development_workflow.md
```

### 31. Specification Alignment

```markdown
# Rule: Implementation-Specification Sync
Description: Keep implementation aligned with specifications
Priority: Critical
Requirements:
- Validate implementation against SPECIFICATIONS.md
- Update specifications when implementation deviates
- Maintain traceability between specs and code
- Document any deviations with rationale
- Regular audits of specification compliance
References:
- See docs/framework/best_practices/implementation_guide.md
- See docs/development/testing/integration_testing.md
```

### 32. Error Prevention

```markdown
# Rule: Prevent Common Mistakes
Description: Avoid common development pitfalls
Priority: High
Requirements:
- Don't make multiple changes at once
- Don't skip testing phases
- Don't ignore user feedback
- Don't proceed without validation
- Don't violate incremental development principles
- Document lessons learned from mistakes
References:
- See docs/development/workflow/development_workflow.md
- See docs/development/testing/unit_testing.md
```

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
