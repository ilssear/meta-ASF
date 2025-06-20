# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Unit Testing

## Overview
This document describes unit testing practices and standards for the SpecFirst Development Framework. Unit testing ensures that individual components work correctly in isolation.

## Unit Testing Principles

### 1. Test-Driven Development (TDD)
- Write tests before writing code
- Use tests to drive design decisions
- Ensure code meets test requirements
- Maintain high test coverage

### 2. Isolation
- Test individual units in isolation
- Mock external dependencies
- Avoid testing multiple units together
- Use test fixtures for setup

### 3. Completeness
- Test all code paths
- Include edge cases and error conditions
- Test both success and failure scenarios
- Validate all outputs and side effects

### 4. Maintainability
- Write clear, readable tests
- Use descriptive test names
- Keep tests simple and focused
- Avoid test code duplication

## Unit Test Structure

### Test File Organization
```
tests/
├── unit/
│   ├── test_module1.py
│   ├── test_module2.py
│   └── test_module3.py
├── fixtures/
│   ├── test_data.py
│   └── mock_objects.py
└── conftest.py
```

### Test Function Structure
```python
def test_function_name_scenario():
    """
    Test description explaining what is being tested.
    
    This test verifies that the function behaves correctly
    under specific conditions.
    """
    # Arrange - Setup test data and conditions
    input_data = create_test_data()
    expected_result = calculate_expected_result()
    
    # Act - Execute the function being tested
    actual_result = function_being_tested(input_data)
    
    # Assert - Verify the results
    assert actual_result == expected_result
```

## Test Categories

### 1. Function Tests
- Test individual functions
- Verify input/output behavior
- Test parameter validation
- Check error handling

### 2. Class Tests
- Test class methods
- Verify object state changes
- Test constructor behavior
- Validate inheritance

### 3. Module Tests
- Test module-level functions
- Verify module initialization
- Test module configuration
- Check module dependencies

### 4. Integration Tests (Limited)
- Test component interactions
- Verify data flow between units
- Test interface contracts
- Validate integration points

## Test Writing Guidelines

### Test Naming
- Use descriptive test names
- Follow pattern: `test_function_name_scenario`
- Include expected behavior in name
- Use clear, readable names

### Test Documentation
- Include docstring for each test
- Explain what is being tested
- Describe expected behavior
- Document any special conditions

### Test Data
- Use realistic test data
- Include edge cases
- Test with various input types
- Use consistent data formats

### Assertions
- Use specific assertions
- Test one thing per assertion
- Include meaningful error messages
- Use appropriate assertion types

## Test Framework Setup

### Python Testing (pytest)
```python
import pytest
from unittest.mock import Mock, patch
from your_module import function_to_test

class TestYourModule:
    """Test suite for your module."""
    
    def setup_method(self):
        """Setup method called before each test."""
        self.test_data = create_test_data()
    
    def teardown_method(self):
        """Teardown method called after each test."""
        cleanup_test_data()
    
    def test_function_success_case(self):
        """Test successful execution of function."""
        # Arrange
        input_data = "test_input"
        expected = "expected_output"
        
        # Act
        result = function_to_test(input_data)
        
        # Assert
        assert result == expected
    
    def test_function_error_case(self):
        """Test error handling of function."""
        # Arrange
        invalid_input = None
        
        # Act & Assert
        with pytest.raises(ValueError, match="Invalid input"):
            function_to_test(invalid_input)
```

### JavaScript Testing (Jest)
```javascript
const { functionToTest } = require('./your-module');

describe('YourModule', () => {
  let testData;
  
  beforeEach(() => {
    testData = createTestData();
  });
  
  afterEach(() => {
    cleanupTestData();
  });
  
  test('should handle success case correctly', () => {
    // Arrange
    const inputData = 'test_input';
    const expected = 'expected_output';
    
    // Act
    const result = functionToTest(inputData);
    
    // Assert
    expect(result).toBe(expected);
  });
  
  test('should throw error for invalid input', () => {
    // Arrange
    const invalidInput = null;
    
    // Act & Assert
    expect(() => {
      functionToTest(invalidInput);
    }).toThrow('Invalid input');
  });
});
```

## Mocking and Stubbing

### When to Mock
- External API calls
- Database operations
- File system operations
- Network requests
- Complex dependencies

### Mocking Examples
```python
# Python with unittest.mock
@patch('module.external_api_call')
def test_function_with_mock(mock_api):
    # Arrange
    mock_api.return_value = {'status': 'success'}
    
    # Act
    result = function_using_api()
    
    # Assert
    assert result == 'success'
    mock_api.assert_called_once()
```

```javascript
// JavaScript with Jest
jest.mock('./external-api');

test('should handle API response correctly', () => {
  // Arrange
  const mockApiResponse = { status: 'success' };
  require('./external-api').mockResolvedValue(mockApiResponse);
  
  // Act
  return functionUsingApi().then(result => {
    // Assert
    expect(result).toBe('success');
  });
});
```

## Test Fixtures

### Data Fixtures
```python
# test_fixtures.py
@pytest.fixture
def sample_user_data():
    """Provide sample user data for tests."""
    return {
        'id': 1,
        'name': 'Test User',
        'email': 'test@example.com',
        'active': True
    }

@pytest.fixture
def sample_product_data():
    """Provide sample product data for tests."""
    return {
        'id': 1,
        'name': 'Test Product',
        'price': 99.99,
        'category': 'electronics'
    }
```

### Mock Fixtures
```python
@pytest.fixture
def mock_database():
    """Provide a mock database for tests."""
    with patch('module.database') as mock_db:
        mock_db.query.return_value.filter.return_value.first.return_value = None
        yield mock_db

@pytest.fixture
def mock_external_api():
    """Provide a mock external API for tests."""
    with patch('module.external_api') as mock_api:
        mock_api.get.return_value.json.return_value = {'data': 'test'}
        yield mock_api
```

## Test Coverage

### Coverage Metrics
- **Line Coverage**: Percentage of code lines executed
- **Branch Coverage**: Percentage of code branches executed
- **Function Coverage**: Percentage of functions called
- **Statement Coverage**: Percentage of statements executed

### Coverage Goals
- **Minimum Coverage**: 80% line coverage
- **Target Coverage**: 90% line coverage
- **Critical Paths**: 100% coverage for critical functions
- **Error Handling**: 100% coverage for error paths

### Coverage Tools
```python
# pytest-cov configuration
[tool:pytest]
addopts = --cov=your_module --cov-report=html --cov-report=term-missing
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
```

## Test Execution

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_module.py

# Run specific test function
pytest tests/unit/test_module.py::test_specific_function

# Run with coverage
pytest --cov=your_module

# Run with verbose output
pytest -v

# Run with parallel execution
pytest -n auto
```

### Test Discovery
- Tests should be discoverable automatically
- Use consistent naming conventions
- Place tests in appropriate directories
- Use test configuration files

## Best Practices

### Test Design
- Write tests that are easy to understand
- Test one thing at a time
- Use descriptive test names
- Keep tests independent

### Test Data Management
- Use factories for test data creation
- Clean up test data after tests
- Use realistic test data
- Avoid hardcoded test values

### Test Maintenance
- Keep tests up-to-date with code changes
- Refactor tests when code is refactored
- Remove obsolete tests
- Review test coverage regularly

### Performance
- Keep tests fast
- Use efficient test data setup
- Avoid unnecessary I/O in tests
- Use parallel test execution when possible

## Common Patterns

### Parameterized Tests
```python
@pytest.mark.parametrize("input,expected", [
    ("hello", "HELLO"),
    ("world", "WORLD"),
    ("", ""),
    ("123", "123"),
])
def test_uppercase_function(input, expected):
    """Test uppercase function with various inputs."""
    result = uppercase_function(input)
    assert result == expected
```

### Test Classes
```python
class TestUserManager:
    """Test suite for UserManager class."""
    
    def setup_method(self):
        """Setup test environment."""
        self.user_manager = UserManager()
        self.test_user = User(name="Test", email="test@example.com")
    
    def test_create_user(self):
        """Test user creation."""
        result = self.user_manager.create_user(self.test_user)
        assert result.id is not None
        assert result.name == "Test"
    
    def test_get_user(self):
        """Test user retrieval."""
        created_user = self.user_manager.create_user(self.test_user)
        retrieved_user = self.user_manager.get_user(created_user.id)
        assert retrieved_user == created_user
```

## Error Testing

### Exception Testing
```python
def test_function_raises_exception():
    """Test that function raises appropriate exception."""
    with pytest.raises(ValueError) as exc_info:
        function_that_raises_exception()
    
    assert str(exc_info.value) == "Expected error message"
```

### Error Condition Testing
```python
def test_function_handles_error_gracefully():
    """Test error handling behavior."""
    result = function_with_error_handling(invalid_input)
    assert result.error_code == "INVALID_INPUT"
    assert result.error_message == "Input validation failed"
```

## References
- [AGILE_SPECFIRST.md](../../framework/methodology/AGILE_SPECFIRST.md) - Core methodology
- [VIBE_USER_GUIDE.md](../../framework/methodology/VIBE_USER_GUIDE.md) - User guidance
- [CURSOR_INTEGRATION.md](../../framework/methodology/CURSOR_INTEGRATION.md) - IDE integration

## Version Information
- Version: 1.0.0
- Last Updated: 2024-03-19
- Status: Active 