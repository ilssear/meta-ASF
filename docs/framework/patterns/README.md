# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# SpecFirst Implementation Patterns

## Overview

This guide outlines the common implementation patterns used in the SpecFirst framework, providing standardized approaches to common development scenarios. The framework emphasizes **specification-driven development**, **AI/LLM code generation**, **PERA cycles**, and **TDD as quality assurance** patterns.

## Core Patterns

### 🔄 PERA Cycle Pattern
The fundamental pattern for continuous improvement:

1. **Plan**: Create or refine complete specifications
2. **Execute**: Use AI/LLM to generate code from specifications
3. **Report/Review**: User reviews generated code and provides feedback
4. **Adjust**: Refine specifications based on feedback

### 🔄 Incremental Development Pattern
After initial code generation, use small, focused changes:

1. **Identify small change** (15 min - 2 hours)
2. **Update specifications** if needed
3. **Make incremental change**
4. **Validate change** against specifications
5. **Update documentation**
6. **Get user feedback**
7. **Repeat for next increment**

## Specification-Driven Patterns

### 1. PERA Cycle Pattern
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

// EXECUTE: Generate code using AI
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

// REPORT/REVIEW: Validate with TDD
function testUserRegistration() {
    // Test valid registration
    const user = registerUser({email: 'test@example.com', password: 'secure123'});
    expect(user.email).toBe('test@example.com');
    expect(user.isActive).toBe(true);
    
    // Test invalid email
    expect(() => registerUser({email: 'invalid', password: 'secure123'}))
        .toThrow('Invalid email format');
}

// ADJUST: Refine based on feedback
// If user feedback indicates need for password validation:
const refinedSpec = {
    ...specification,
    requirements: [...specification.requirements, "Validate password strength"]
};
```

### 2. AI/LLM Code Generation Pattern
```javascript
// 1. Create detailed specification
const spec = {
    function: "calculateTotal",
    input: "Array of items with price property",
    output: "Total price as number",
    requirements: [
        "Handle empty array (return 0)",
        "Sum all item prices",
        "Handle null/undefined prices (treat as 0)",
        "Return number type"
    ]
};

// 2. Generate code using AI
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + (item.price || 0), 0);
}

// 3. Validate with TDD
function testCalculateTotal() {
    expect(calculateTotal([])).toBe(0);
    expect(calculateTotal([{price: 10}, {price: 20}])).toBe(30);
    expect(calculateTotal([{price: 10}, {price: null}])).toBe(10);
    expect(typeof calculateTotal([{price: 5}])).toBe('number');
}
```

### 3. Specification Refinement Pattern
```javascript
// Initial specification
const initialSpec = {
    feature: "Data Processing",
    requirements: ["Process input data", "Return processed result"]
};

// After user feedback
const refinedSpec = {
    feature: "Data Processing",
    requirements: [
        "Process input data",
        "Return processed result",
        "Handle empty input",
        "Validate input format",
        "Log processing steps"
    ],
    constraints: [
        "Must process within 5 seconds",
        "Must handle files up to 10MB"
    ]
};
```

## TDD Quality Assurance Patterns

### 1. Specification Validation Pattern
```javascript
// Validate implementation against specifications
function validateImplementation(specFile, implementationFiles) {
    const specRequirements = parseSpecifications(specFile);
    const implementedFeatures = analyzeImplementation(implementationFiles);
    
    const missingFeatures = specRequirements.filter(req => 
        !implementedFeatures.includes(req)
    );
    const extraFeatures = implementedFeatures.filter(feat => 
        !specRequirements.includes(feat)
    );
    
    return {
        valid: missingFeatures.length === 0 && extraFeatures.length === 0,
        missing: missingFeatures,
        extra: extraFeatures
    };
}
```

### 2. TDD for AI-Generated Code Pattern
```javascript
// 1. Write test for specification requirement
function testCalculateTotal() {
    const items = [{price: 10}, {price: 20}];
    const total = calculateTotal(items);
    expect(total).toBe(30);
}

// 2. Generate code using AI from specification
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + item.price, 0);
}

// 3. Run tests to validate generated code
// 4. Refine code if tests fail
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + (item.price || 0), 0);
}
```

### 3. Test Organization Pattern
```javascript
// tests/userManagement.test.js
describe('User Registration', () => {
    test('should register valid user', () => {
        // Test valid user registration
    });
    
    test('should reject invalid email', () => {
        // Test invalid email handling
    });
    
    test('should reject duplicate email', () => {
        // Test duplicate email handling
    });
});

describe('User Authentication', () => {
    test('should authenticate valid credentials', () => {
        // Test valid login
    });
    
    test('should reject invalid credentials', () => {
        // Test invalid credentials
    });
});
```

## Language-Specific TDD Examples

### JavaScript/TypeScript (Jest)
```javascript
describe('Calculator', () => {
    test('should add two numbers', () => {
        expect(add(2, 3)).toBe(5);
    });
    
    test('should handle negative numbers', () => {
        expect(add(-1, 1)).toBe(0);
    });
    
    test('should handle zero', () => {
        expect(add(0, 5)).toBe(5);
    });
});
```

### Python (pytest)
```python
class TestCalculator:
    def test_add_two_numbers(self):
        assert add(2, 3) == 5
    
    def test_handle_negative_numbers(self):
        assert add(-1, 1) == 0
    
    def test_handle_zero(self):
        assert add(0, 5) == 5
```

### Java (JUnit 5)
```java
@Test
void shouldAddTwoNumbers() {
    assertEquals(5, add(2, 3));
}

@Test
void shouldHandleNegativeNumbers() {
    assertEquals(0, add(-1, 1));
}

@Test
void shouldHandleZero() {
    assertEquals(5, add(0, 5));
}
```

### C# (xUnit)
```csharp
[Fact]
public void ShouldAddTwoNumbers()
{
    Assert.Equal(5, Add(2, 3));
}

[Fact]
public void ShouldHandleNegativeNumbers()
{
    Assert.Equal(0, Add(-1, 1));
}

[Fact]
public void ShouldHandleZero()
{
    Assert.Equal(5, Add(0, 5));
}
```

## AI/LLM Integration Patterns

### 1. Specification-to-Code Pattern
```javascript
// 1. Define detailed specification
const spec = {
    function: "processUserData",
    input: "User object with name, email, age",
    output: "Processed user object",
    requirements: [
        "Validate email format",
        "Ensure age is positive number",
        "Capitalize first letter of name",
        "Add processing timestamp"
    ]
};

// 2. Generate code using AI
function processUserData(user) {
    if (!isValidEmail(user.email)) {
        throw new Error('Invalid email format');
    }
    if (user.age <= 0) {
        throw new Error('Age must be positive');
    }
    
    return {
        name: user.name.charAt(0).toUpperCase() + user.name.slice(1),
        email: user.email,
        age: user.age,
        processedAt: new Date()
    };
}

// 3. Validate with TDD
function testProcessUserData() {
    const user = {name: 'john', email: 'john@example.com', age: 25};
    const processed = processUserData(user);
    expect(processed.name).toBe('John');
    expect(processed.processedAt).toBeInstanceOf(Date);
}
```

### 2. Feedback Integration Pattern
```javascript
// 1. Implement basic feature
function processData(data) {
    return data.toUpperCase();
}

// 2. Get user feedback and refine specification
const refinedSpec = {
    function: "processData",
    input: "String data",
    output: "Processed string",
    requirements: [
        "Convert to uppercase",
        "Handle empty strings",
        "Trim whitespace",
        "Support multiple formats"
    ]
};

// 3. Regenerate code based on refined specification
function processData(data, formatType = "upper") {
    if (!data) return "";
    
    data = data.trim();
    
    if (formatType === "upper") {
        return data.toUpperCase();
    } else if (formatType === "lower") {
        return data.toLowerCase();
    } else if (formatType === "title") {
        return data.replace(/\w\S*/g, (txt) => 
            txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase()
        );
    } else {
        throw new Error("Unsupported format");
    }
}
```

## Validation Patterns

### 1. Regression Testing Pattern
```javascript
// Test for regressions after changes
function testRegressionSuite() {
    // Test core functionality
    expect(basicCalculator(2, 3, "add")).toBe(5);
    expect(basicCalculator(5, 2, "subtract")).toBe(3);
    
    // Test error handling
    expect(() => basicCalculator(2, 3, "invalid")).toThrow("Unsupported operation");
    
    // Test edge cases
    expect(basicCalculator(0, 0, "add")).toBe(0);
}
```

### 2. Documentation Validation Pattern
```javascript
// Validate documentation completeness
function validateDocumentation(specFile, docFiles) {
    const specDocs = extractDocRequirements(specFile);
    const existingDocs = analyzeDocumentation(docFiles);
    
    const missingDocs = specDocs.filter(doc => 
        !existingDocs.includes(doc)
    );
    
    return {
        complete: missingDocs.length === 0,
        missing: missingDocs,
        guidance: generateDocGuidance(missingDocs)
    };
}
```

## API Patterns

### 1. RESTful API Design
- Resource-based URLs
- HTTP method semantics
- Status code usage
- Response formatting
- Error handling

### 2. Authentication Patterns
- JWT authentication
- OAuth integration
- Session management
- Token refresh
- Security headers

### 3. Data Validation
- Input validation
- Schema validation
- Error responses
- Custom validators
- Validation middleware

### 4. Response Patterns
- Standard response format
- Pagination
- Filtering
- Sorting
- Error handling

## Security Patterns

### 1. Authentication
- User authentication
- Token management
- Password hashing
- Session handling
- Multi-factor auth

### 2. Authorization
- Role-based access
- Permission checks
- Resource protection
- API security
- Data access control

### 3. Data Protection
- Encryption
- Data sanitization
- Secure storage
- Secure transmission
- Key management

### 4. Security Headers
- CORS configuration
- CSP headers
- HSTS
- XSS protection
- CSRF protection

## Testing Patterns

### 1. Unit Testing
- Test organization
- Mocking patterns
- Assertion patterns
- Test fixtures
- Test utilities

### 2. Integration Testing
- API testing
- Database testing
- Service testing
- Mock services
- Test data

### 3. End-to-End Testing
- User workflows
- UI testing
- API testing
- Data validation
- Error scenarios

### 4. Performance Testing
- Load testing
- Stress testing
- Benchmarking
- Resource monitoring
- Bottleneck identification

## Data Patterns

### 1. Database Design
- Schema design
- Indexing
- Relationships
- Migrations
- Backup strategy

### 2. Caching
- Cache strategies
- Cache invalidation
- Distributed caching
- Cache warming
- Cache monitoring

### 3. Data Access
- Repository pattern
- Query optimization
- Connection pooling
- Transaction management
- Error handling

### 4. Data Validation
- Schema validation
- Data sanitization
- Type checking
- Constraint validation
- Error handling

## Service Patterns

### 1. Service Design
- Service boundaries
- Interface design
- Error handling
- Logging
- Monitoring

### 2. Service Communication
- API design
- Message formats
- Error handling
- Retry logic
- Circuit breaking

### 3. Service Discovery
- Service registration
- Health checks
- Load balancing
- Failover
- Configuration

### 4. Service Monitoring
- Metrics collection
- Logging
- Tracing
- Alerting
- Performance monitoring

## UI Patterns

### 1. Component Design
- Component structure
- State management
- Event handling
- Error handling
- Loading states

### 2. Layout Patterns
- Responsive design
- Grid systems
- Component composition
- Navigation
- Error states

### 3. User Interaction
- Form handling
- Validation
- Error feedback
- Loading states
- Success feedback

### 4. Accessibility
- ARIA attributes
- Keyboard navigation
- Screen reader support
- Color contrast
- Focus management

## Error Handling Patterns

### 1. Error Types
- Validation errors
- System errors
- Network errors
- Security errors
- Business logic errors

### 2. Error Responses
- Error format
- Status codes
- Error messages
- Error details
- Recovery suggestions

### 3. Error Logging
- Error categorization
- Error context
- Error tracking
- Error reporting
- Error analysis

## Common Anti-Patterns to Avoid

### 1. Specification Anti-Patterns
- ❌ **Vague specifications**: Unclear or ambiguous requirements
- ❌ **Missing edge cases**: Not considering edge cases in specifications
- ❌ **Outdated specs**: Not keeping specifications current
- ❌ **No validation**: Not validating against specifications
- ❌ **Poor structure**: Poorly structured specifications

### 2. AI/LLM Generation Anti-Patterns
- ❌ **Incomplete specifications**: Not providing enough detail for AI generation
- ❌ **No validation**: Not validating AI-generated code with TDD
- ❌ **Ignoring feedback**: Not incorporating user feedback
- ❌ **Poor alignment**: Not maintaining specification-code alignment
- ❌ **No documentation**: Not documenting generation decisions

### 3. TDD Quality Assurance Anti-Patterns
- ❌ **Skipping tests**: Not testing AI-generated code
- ❌ **Incomplete coverage**: Not testing edge cases
- ❌ **Complex tests**: Making tests too complex
- ❌ **Ignoring failures**: Not fixing failing tests
- ❌ **No specification alignment**: Not aligning tests with specifications

## References

- [API Patterns](api_patterns.md)
- [Security Patterns](security_patterns.md)
- [Testing Patterns](testing_patterns.md)
- [Implementation Guide](../best_practices/implementation_guide.md)
- [Development Workflow](../../development/workflow/README.md)

## Version History

- **v1.0.0** (2025-06-03): Initial patterns guide
- **v1.0.1** (2025-06-20): Added specification-driven development, AI/LLM integration, and PERA cycles 