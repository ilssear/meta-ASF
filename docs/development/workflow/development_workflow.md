# Development Workflow in SpecFirst

## Overview
This guide outlines the implementation-specific development workflow for projects using the SpecFirst methodology. While the framework documentation covers methodology and patterns, this guide focuses on practical implementation using specific technologies and tools.

## Key Principles

### 1. Specification-Driven Implementation
- Follow framework methodology
- Implement based on specifications
- Maintain alignment with requirements
- Track implementation progress

### 2. Technology-Specific Development
- Choose appropriate tech stack
- Follow language best practices
- Use framework patterns
- Implement project-specific features

### 3. Quality Assurance
- Implement framework testing patterns
- Follow project testing requirements
- Maintain code quality
- Document implementation details

## Development Process

### 1. Project Setup
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

def setup_project(spec_file: str) -> Dict[str, Any]:
    """Set up project based on specifications."""
    # Implementation
    pass

def configure_environment(config: Dict[str, Any]) -> bool:
    """Configure development environment."""
    # Implementation
    pass
```

### 2. Implementation Planning
- Review framework patterns
- Plan project-specific features
- Estimate implementation effort
- Set up development environment

### 3. Development Cycle
1. Follow framework methodology
2. Implement project features
3. Apply framework patterns
4. Update project documentation
5. Review and refine

## Incremental Development Guidelines

### Change Size Guidelines

#### Small Changes (Recommended)
- **Scope**: One function, one file, or one feature
- **Time**: 15 minutes to 2 hours
- **Risk**: Low
- **Examples**:
  - Adding a new method to an existing class
  - Fixing a bug in a single function
  - Adding a new test case
  - Updating documentation for one section

#### Medium Changes (Requires Planning)
- **Scope**: One module or component
- **Time**: 2 hours to 1 day
- **Risk**: Medium
- **Examples**:
  - Refactoring a class
  - Adding a new feature to a module
  - Updating multiple related functions
  - Changing an interface

#### Large Changes (Break Down)
- **Scope**: Multiple modules or major refactoring
- **Time**: 1 day to 1 week
- **Risk**: High
- **Examples**:
  - Major architecture changes
  - Complete module rewrites
  - Framework updates
  - Database schema changes

### Before Making Changes

#### 1. Write Tests First (TDD)
```python
# Example: Adding new functionality
def test_validate_project_stage_2():
    """Test that project with missing source files is Stage 2."""
    # Arrange
    test_project = create_test_project_with_missing_source_files()
    
    # Act
    validator = ProjectValidator(test_project)
    validator.run()
    
    # Assert
    assert validator.stage == "2. Incomplete Source Files"
    assert not validator.source_files_ok
```

#### 2. Identify Impact
```python
# Example: Impact analysis
def analyze_change_impact(change_description: str) -> Dict[str, Any]:
    """Analyze the impact of a proposed change."""
    return {
        "files_affected": ["validate_project.py", "framework_validator.py"],
        "tests_needed": ["test_source_file_validation"],
        "dependencies": ["SpecParser", "DocumentationChecker"],
        "risk_level": "low",
        "rollback_plan": "git revert or restore from backup"
    }
```

#### 3. Plan the Smallest Possible Change
```python
# Example: Breaking down a large change
def plan_incremental_refactor():
    """Plan incremental refactoring of validation scripts."""
    phases = [
        {
            "phase": 1,
            "change": "Create shared SpecParser module",
            "files": ["lib/spec_parser.py"],
            "tests": ["test_spec_parser_basic"],
            "validation": "Parser can extract source files"
        },
        {
            "phase": 2,
            "change": "Update validate_project.py to use shared parser",
            "files": ["validate_project.py"],
            "tests": ["test_validate_project_with_shared_parser"],
            "validation": "Project validation still works"
        },
        {
            "phase": 3,
            "change": "Update check_structure.py to use shared parser",
            "files": ["check_structure.py"],
            "tests": ["test_check_structure_with_shared_parser"],
            "validation": "Structure checking still works"
        }
    ]
    return phases
```

#### 4. Get Approval for Approach
```python
# Example: Change proposal
def propose_change(change: Dict[str, Any]) -> bool:
    """Propose a change and get approval."""
    print(f"Proposed Change: {change['description']}")
    print(f"Files Affected: {change['files']}")
    print(f"Tests Needed: {change['tests']}")
    print(f"Risk Level: {change['risk']}")
    print(f"Estimated Time: {change['time']}")
    
    # Get user approval
    return input("Proceed with this change? (y/n): ").lower() == 'y'
```

### During Implementation

#### 1. Make One Change at a Time
```python
# Example: Incremental implementation
def implement_shared_parser_phase_1():
    """Phase 1: Create basic SpecParser class."""
    # Step 1: Create the class structure
    class SpecParser:
        def __init__(self, root_dir: Path):
            self.root_dir = root_dir
            self.specs_file = root_dir / "SPECIFICATIONS.md"
    
    # Step 2: Add basic file existence check
    def parse_source_files(self) -> List[str]:
        if not self.specs_file.is_file():
            return []
        return []
    
    # Step 3: Test this minimal implementation
    # Step 4: Add more functionality incrementally
```

#### 2. Test Each Change
```python
# Example: Testing each increment
def test_parser_initialization():
    """Test 1: Parser can be initialized."""
    parser = SpecParser(Path("test_project"))
    assert parser is not None

def test_parser_without_spec_file():
    """Test 2: Parser handles missing spec file."""
    parser = SpecParser(Path("nonexistent"))
    result = parser.parse_source_files()
    assert result == []

def test_parser_with_empty_spec():
    """Test 3: Parser handles empty spec file."""
    # Implementation
    pass
```

#### 3. Validate Against Specifications
```python
# Example: Specification validation
def validate_against_specs(implementation: Any, specs: Dict[str, Any]) -> bool:
    """Validate implementation against specifications."""
    requirements = specs.get("requirements", [])
    
    for requirement in requirements:
        if not requirement_satisfied(implementation, requirement):
            return False
    
    return True

def requirement_satisfied(implementation: Any, requirement: str) -> bool:
    """Check if implementation satisfies a specific requirement."""
    # Implementation-specific validation logic
    pass
```

### After Each Change

#### 1. Run All Tests
```bash
# Example: Test execution
python -m pytest tests/ -v
python scripts/validate_project.py --verbose
python scripts/check_docs.py --verbose
```

#### 2. Check for Regressions
```python
# Example: Regression testing
def check_for_regressions():
    """Check that existing functionality still works."""
    test_cases = [
        "test_complete_project_validation",
        "test_incomplete_project_validation", 
        "test_missing_docs_validation"
    ]
    
    for test_case in test_cases:
        if not run_test_case(test_case):
            raise RegressionError(f"Regression detected in {test_case}")
```

#### 3. Document What Changed
```python
# Example: Change documentation
def document_change(change: Dict[str, Any]):
    """Document what was changed and why."""
    changelog_entry = f"""
    ## {change['date']} - {change['description']}
    
    **Files Changed:**
    {chr(10).join(f"- {file}" for file in change['files'])}
    
    **Reason:**
    {change['reason']}
    
    **Tests Added:**
    {chr(10).join(f"- {test}" for test in change['tests'])}
    
    **Validation:**
    {change['validation']}
    """
    
    with open("CHANGELOG.md", "a") as f:
        f.write(changelog_entry)
```

### Incremental Development Checklist

#### Before Starting
- [ ] Change is broken into smallest possible pieces
- [ ] Tests written for new functionality
- [ ] Impact analysis completed
- [ ] Rollback plan prepared
- [ ] Approval obtained (if needed)

#### During Implementation
- [ ] One change at a time
- [ ] Tests pass after each change
- [ ] No regressions introduced
- [ ] Code follows style guidelines
- [ ] Changes are focused and minimal

#### After Implementation
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Changes documented in changelog
- [ ] Code reviewed (if applicable)
- [ ] User feedback incorporated

### Common Mistakes to Avoid

#### 1. Making Multiple Changes at Once
```python
# ❌ Bad: Multiple changes in one commit
def bad_multiple_changes():
    """Multiple unrelated changes."""
    # Change 1: Add new feature
    def new_feature():
        pass
    
    # Change 2: Refactor existing code
    def refactored_function():
        pass
    
    # Change 3: Fix unrelated bug
    def bug_fix():
        pass

# ✅ Good: One change per commit
def good_single_change():
    """Single, focused change."""
    # Only one change here
    def new_feature():
        pass
```

#### 2. Not Testing Each Increment
```python
# ❌ Bad: Testing only at the end
def bad_development_process():
    """Write all code, then test."""
    # Write 100 lines of code
    # ... lots of implementation ...
    
    # Test only at the end
    run_all_tests()

# ✅ Good: Test each increment
def good_development_process():
    """Test each small change."""
    # Write 5 lines, test
    def small_feature_1():
        pass
    test_small_feature_1()
    
    # Write 5 more lines, test
    def small_feature_2():
        pass
    test_small_feature_2()
```

#### 3. Ignoring Feedback
```python
# ❌ Bad: Ignoring user feedback
def bad_feedback_handling():
    """Ignore feedback and continue."""
    user_feedback = get_user_feedback()
    if user_feedback.suggests_changes():
        # Ignore feedback
        continue_with_original_plan()

# ✅ Good: Incorporate feedback
def good_feedback_handling():
    """Incorporate feedback into development."""
    user_feedback = get_user_feedback()
    if user_feedback.suggests_changes():
        # Pause and reconsider
        revised_plan = incorporate_feedback(original_plan, user_feedback)
        implement_revised_plan(revised_plan)
```

## Best Practices

### Project Structure
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

# Project structure
project_root/
├── src/                    # Source code
│   ├── core/              # Core functionality
│   ├── api/               # API implementation
│   └── utils/             # Utility functions
├── tests/                 # Test files
│   ├── unit/             # Unit tests
│   ├── integration/      # Integration tests
│   └── e2e/              # End-to-end tests
└── docs/                 # Documentation
    ├── api/              # API documentation
    └── guides/           # User guides
```

### Implementation Guidelines
1. Follow framework patterns
2. Use project-specific standards
3. Maintain code quality
4. Keep documentation updated
5. Follow testing requirements

## Tools and Configuration

### Development Environment
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

# .env.example
PYTHONPATH=src
TEST_ENV=development
DEBUG=True
LOG_LEVEL=DEBUG
```

### IDE Configuration
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

## Implementation Patterns

### Feature Implementation
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

from typing import Any, Dict, List

class ProjectFeature:
    """Project-specific feature implementation."""
    
    def __init__(self, spec: Dict[str, Any]) -> None:
        """Initialize with specification."""
        self.spec = spec
        self.validate_spec()
    
    def validate_spec(self) -> None:
        """Validate specification requirements."""
        # Implementation
        pass
    
    def implement(self) -> None:
        """Implement the feature."""
        # Implementation
        pass
```

### Error Handling
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

class ProjectError(Exception):
    """Base class for project errors."""
    pass

class ImplementationError(ProjectError):
    """Error in implementation."""
    pass

class ConfigurationError(ProjectError):
    """Error in configuration."""
    pass
```

## Troubleshooting

### Common Issues
1. **Framework Integration**
   - Problem: Framework pattern mismatch
   - Solution: Review framework documentation

2. **Implementation Issues**
   - Problem: Project-specific errors
   - Solution: Follow project guidelines

3. **Testing Challenges**
   - Problem: Test implementation issues
   - Solution: Use framework testing patterns

## Version History
- v1.0.0 (2025-01-01): Initial release
- v1.1.0 (2025-02-01): Added implementation patterns
- v1.2.0 (2025-03-01): Updated best practices

## References
- [Framework Methodology](../../framework/methodology/AGILE_SPECFIRST.md)
- [Framework Implementation Guide](../../framework/best_practices/implementation_guide.md)
- [Framework Testing Guide](../../framework/best_practices/testing_guide.md) 