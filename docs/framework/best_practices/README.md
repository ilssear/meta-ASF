# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Best Practices

## Overview

This guide outlines the best practices for using the SpecFirst framework, ensuring consistent, high-quality development across all projects. The framework emphasizes **specification-driven development**, **AI/LLM code generation**, **PERA cycles**, and **TDD as quality assurance** to deliver value quickly and reliably.

## Core Principles

### 🎯 Specification-Driven Development
- **Complete specifications first**: Never start coding without full specifications
- **LLM-regenerable specs**: Write specifications that AI can understand and implement
- **User validation**: Get feedback on specifications before implementation
- **Continuous refinement**: Update specifications based on user feedback

### 🔄 PERA Cycle Integration
- **Plan**: Create or refine complete specifications
- **Execute**: Use AI/LLM to generate code from specifications
- **Report/Review**: User reviews generated code and provides feedback
- **Adjust**: Refine specifications based on feedback

### 🔄 Incremental Development
- **Small, focused changes**: 15 minutes to 2 hours per change after initial generation
- **Phase-based implementation**: Break large features into manageable phases
- **Continuous validation**: Validate each change before proceeding
- **User feedback loops**: Get feedback on each increment
- **Documentation updates**: Update docs at every cycle

## Core Best Practices

### 1. Specification-Driven Development
- **Start with specifications**: Create complete, LLM-regenerable specifications before implementation
- **AI/LLM integration**: Use AI to generate code from detailed specifications
- **User feedback loops**: Continuously refine specifications based on user feedback
- **Specification validation**: Use specifications to validate generated code
- **PDCA cycles**: Plan-Do-Check-Act for continuous improvement

### 2. AI/LLM Code Generation
- **Detailed specifications**: Provide clear, comprehensive specifications for AI generation
- **Quality validation**: Use TDD to validate AI-generated code
- **Iterative refinement**: Improve both specifications and generated code
- **Specification alignment**: Maintain alignment between specifications and implementation
- **Documentation**: Document generation decisions and rationale

### 3. PERA Cycle Implementation
- **Plan (Specification)**: Create or refine complete specifications
- **Execute (AI Generation)**: Use AI/LLM to generate code from specifications
- **Report/Review (User Review)**: User reviews generated code and provides feedback
- **Adjust (Specification Refinement)**: Refine specifications based on feedback
- **Continuous improvement**: Repeat cycle for ongoing enhancement

### 4. TDD as Quality Assurance
- **Validate generated code**: Use TDD to ensure AI-generated code meets requirements
- **Test specification requirements**: Write tests to validate against specifications
- **Comprehensive coverage**: Test success, failure, and edge cases
- **Continuous testing**: Run tests after every change
- **Quality assurance**: Use TDD as a quality gate for generated code

### 5. Rapid Feedback Integration
- **Early feedback**: Seek feedback at every stage
- **Short feedback loops**: Catch issues early
- **User-driven evolution**: Use feedback to refine specifications
- **Continuous improvement**: Document lessons learned
- **Validation checkpoints**: Use automated validation tools

## Development Best Practices

### 1. Specification-First Workflow
```javascript
// PLAN: Define complete specification
const specification = {
    feature: "User Registration",
    requirements: [
        "Accept email and password",
        "Validate email format",
        "Create user account",
        "Return user object"
    ],
    successCriteria: [
        "Valid email creates account",
        "Invalid email returns error",
        "User object contains email and status"
    ]
};

// DO: Generate code using AI
function registerUser(userData) {
    if (!isValidEmail(userData.email)) {
        throw new Error('Invalid email format');
    }
    return {
        email: userData.email,
        isActive: true,
        createdAt: new Date()
    };
}

// CHECK: Validate with TDD
function testUserRegistration() {
    // Test valid registration
    const user = registerUser({email: 'test@example.com', password: 'secure123'});
    expect(user.email).toBe('test@example.com');
    expect(user.isActive).toBe(true);
    
    // Test invalid email
    expect(() => registerUser({email: 'invalid', password: 'secure123'}))
        .toThrow('Invalid email format');
}

// ACT: Refine based on feedback
// If user feedback indicates need for password validation:
const refinedSpec = {
    ...specification,
    requirements: [...specification.requirements, "Validate password strength"]
};
```

### 2. AI/LLM Code Generation Pattern
1. **Create detailed specification** with clear requirements
2. **Generate code** using AI from specification
3. **Apply TDD** to validate generated code
4. **Test thoroughly** to ensure quality
5. **Refine code** based on test results
6. **Get user feedback** on functionality
7. **Refine specification** based on feedback

### 3. Project Structure
- Follow standard layout with clear separation of concerns
- Use clear naming conventions
- Organize by feature
- Maintain clean architecture
- Include validation scripts

### 4. Code Quality
- Follow language-specific style guides
- Write clean, readable code
- Use type hints/annotations where available
- Document functions with appropriate docstring format
- Handle errors gracefully

### 5. Version Control
- Clear, descriptive commit messages
- Feature branches for major changes
- Regular, small commits
- Code reviews for all changes
- Clean, linear history

## Testing Best Practices

### 1. TDD as Quality Assurance
- **Write tests** to validate specification requirements
- **Test AI-generated code** thoroughly
- **Test both success and failure** cases
- **Use descriptive test names** that explain the scenario
- **Maintain high test coverage** (aim for 90%+)

### 2. Test Categories
- **Unit tests**: Test individual functions and methods
- **Integration tests**: Test component interactions
- **End-to-end tests**: Test complete user workflows
- **Performance tests**: Test system performance
- **Security tests**: Test security vulnerabilities

### 3. Test Quality
- **Fast execution**: Tests should run quickly
- **Independent**: Tests should not depend on each other
- **Repeatable**: Tests should produce same results
- **Self-validating**: Tests should clearly pass or fail
- **Specification-aligned**: Tests should validate specification requirements

## Language-Specific Testing Recommendations

### JavaScript/TypeScript
```javascript
// Jest example
describe('User Registration', () => {
    test('should register valid user', () => {
        const userData = { email: 'test@example.com', password: 'secure123' };
        const user = registerUser(userData);
        expect(user.email).toBe('test@example.com');
        expect(user.isActive).toBe(true);
    });

    test('should reject invalid email', () => {
        const userData = { email: 'invalid', password: 'secure123' };
        expect(() => registerUser(userData)).toThrow('Invalid email format');
    });
});
```

### Python
```python
# pytest example
class TestUserRegistration:
    def test_valid_registration(self):
        user_data = {"email": "test@example.com", "password": "secure123"}
        user = register_user(user_data)
        assert user.email == "test@example.com"
        assert user.is_active == True
    
    def test_invalid_email(self):
        user_data = {"email": "invalid", "password": "secure123"}
        with pytest.raises(ValueError, match="Invalid email format"):
            register_user(user_data)
```

### Java
```java
// JUnit 5 example
@Test
void shouldRegisterValidUser() {
    UserData userData = new UserData("test@example.com", "secure123");
    User user = registerUser(userData);
    assertEquals("test@example.com", user.getEmail());
    assertTrue(user.isActive());
}

@Test
void shouldRejectInvalidEmail() {
    UserData userData = new UserData("invalid", "secure123");
    assertThrows(ValueError.class, () -> registerUser(userData));
}
```

### C#
```csharp
// xUnit example
[Fact]
public void ShouldRegisterValidUser()
{
    var userData = new UserData("test@example.com", "secure123");
    var user = RegisterUser(userData);
    Assert.Equal("test@example.com", user.Email);
    Assert.True(user.IsActive);
}

[Fact]
public void ShouldRejectInvalidEmail()
{
    var userData = new UserData("invalid", "secure123");
    Assert.Throws<ValueError>(() => RegisterUser(userData));
}
```

## Validation Best Practices

### 1. Automated Validation
- **Run validation scripts** after each change
- **Check for regressions** in existing functionality
- **Validate against specifications** to ensure alignment
- **Test edge cases** and error conditions
- **Verify documentation** completeness

### 2. Validation Tools
- **`validate_project.py`**: Determines project development stage
- **`check_docs.py`**: Validates documentation completeness
- **`check_structure.py`**: Validates project structure integrity
- **Unit test suites**: Validate individual components
- **Integration tests**: Validate component interactions

### 3. Validation Checklist
- [ ] All tests pass
- [ ] No regressions introduced
- [ ] Implementation matches specifications
- [ ] Documentation is complete and accurate
- [ ] Code follows style guidelines
- [ ] Error handling is comprehensive
- [ ] User feedback incorporated
- [ ] Changes are properly documented

## User Experience Best Practices

### 1. Interface Design
- **User-centric design**: Design for end-user workflows
- **Consistent patterns**: Use established UI/UX patterns
- **Clear feedback**: Provide real-time feedback
- **Error prevention**: Prevent errors before they occur
- **Accessibility**: Ensure accessibility compliance

### 2. Performance
- **Fast response times**: Optimize for speed
- **Efficient operations**: Minimize resource usage
- **Resource optimization**: Use resources efficiently
- **Caching strategy**: Implement appropriate caching
- **Load handling**: Handle high load gracefully

### 3. Error Handling
- **Clear error messages**: Provide helpful error information
- **Recovery options**: Offer ways to recover from errors
- **User guidance**: Guide users through error resolution
- **Comprehensive logging**: Log errors for debugging
- **Monitoring**: Monitor for errors in production

## Maintenance Best Practices

### 1. Code Maintenance
- **Regular updates**: Keep dependencies current
- **Dependency management**: Manage dependencies carefully
- **Code cleanup**: Remove dead code and improve structure
- **Performance optimization**: Continuously optimize performance
- **Security patches**: Apply security updates promptly

### 2. Documentation Maintenance
- **Keep current**: Update documentation with code changes
- **Version control**: Track documentation changes
- **Regular reviews**: Review documentation periodically
- **Update examples**: Keep examples current
- **Maintain references**: Keep cross-references accurate

### 3. Testing Maintenance
- **Regular test runs**: Run tests frequently
- **Update test cases**: Update tests as requirements change
- **Performance monitoring**: Monitor test performance
- **Security scanning**: Scan for security vulnerabilities
- **User feedback**: Incorporate user feedback into tests

## Common Mistakes to Avoid

### 1. Specification Mistakes
- ❌ **Vague requirements**: Unclear or ambiguous specifications
- ❌ **Missing edge cases**: Not considering edge cases
- ❌ **Outdated specs**: Not keeping specifications current
- ❌ **No validation**: Not validating against specifications
- ❌ **Poor structure**: Poorly structured specifications

### 2. AI/LLM Generation Mistakes
- ❌ **Incomplete specifications**: Not providing enough detail for AI generation
- ❌ **No validation**: Not validating AI-generated code with TDD
- ❌ **Ignoring feedback**: Not incorporating user feedback
- ❌ **Poor alignment**: Not maintaining specification-code alignment
- ❌ **No documentation**: Not documenting generation decisions

### 3. TDD Quality Assurance Mistakes
- ❌ **Skipping tests**: Not testing AI-generated code
- ❌ **Incomplete coverage**: Not testing edge cases
- ❌ **Complex tests**: Making tests too complex
- ❌ **Ignoring failures**: Not fixing failing tests
- ❌ **No specification alignment**: Not aligning tests with specifications

## Tools and Resources

### 1. Development Tools
- **IDE setup**: Configure IDE for specification-driven workflow
- **Version control**: Use Git for version control
- **Testing tools**: pytest, unittest, etc.
- **Documentation tools**: Markdown editors, documentation generators
- **Validation tools**: Custom validation scripts

### 2. Monitoring Tools
- **Performance monitoring**: Monitor application performance
- **Error tracking**: Track and analyze errors
- **User analytics**: Analyze user behavior
- **Security scanning**: Scan for security vulnerabilities
- **Log analysis**: Analyze application logs

### 3. Documentation Tools
- **Markdown editors**: Edit documentation efficiently
- **Diagram tools**: Create visual diagrams
- **Version control**: Track documentation changes
- **Documentation generators**: Generate documentation automatically
- **Validation tools**: Validate documentation completeness

## References

1. [Specification Guide](specification_guide.md)
2. [Implementation Guide](implementation_guide.md)
3. [Test Frameworks Guide](test_frameworks_guide.md)
4. [Security Guide](../security/README.md)
5. [Style Guide](../style/README.md)

## Additional Resources

- [Agile SpecFirst Methodology](../methodology/AGILE_SPECFIRST.md)
- [Vibe Coder's Guide](../methodology/VIBE_USER_GUIDE.md)
- [Cursor Integration Guide](../methodology/CURSOR_INTEGRATION.md)
- [Implementation Patterns](../patterns/README.md)
- [Development Setup](../../development/setup/README.md)
- [Workflow Guide](../../development/workflow/README.md)
- [Testing Procedures](../../development/testing/README.md)

## Copyright Headers

### Policy
1. Project-Level Files
   - Use actual copyright information
   - Applies to core framework files
   - Example: `# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)`

2. Documentation Files
   - Use generic placeholders
   - Applies to all files in `docs/` directory
   - Example: `# Copyright (c) [Year], [Full Name] ([Email Address])`

3. Code Examples
   - Use generic placeholders
   - Applies to all example code
   - Example: `# Copyright (c) [Year], [Full Name] ([Email Address])`

### Templates

1. Project-Level Template:
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
[Module Description]
"""
```

2. Documentation Template:
```markdown
# Copyright (c) [Year], [Full Name] ([Email Address])

# [Document Title]

[Document Content]
```

3. Code Example Template:
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

"""
[Example Description]
"""

[Example Code]
```

## Version History

### Best Practices
1. Always include copyright headers
2. Use appropriate template for file type
3. Keep headers consistent within each file
4. Update year when needed
5. Include email address for contact 

- **v1.0.0** (2025-06-03): Initial best practices guide
- **v1.0.1** (2025-06-20): Added specification-driven development, AI/LLM integration, and PDCA cycles 
