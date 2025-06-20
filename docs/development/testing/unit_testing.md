# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
# Unit Testing in SpecFirst

## Overview
This document outlines unit testing practices and procedures for the SpecFirst framework.

## Testing Principles

### 1. Test Isolation
- Independent test cases
- No shared state
- Clean test environment
- Isolated dependencies
- Predictable results

### 2. Test Coverage
- Function coverage
- Statement coverage
- Branch coverage
- Condition coverage
- Path coverage

### 3. Test Quality
- Clear test names
- Descriptive assertions
- Minimal setup
- Proper teardown
- Meaningful failures

## Test Structure

### 1. Basic Test
```python
# Example: Basic unit test
import pytest

def test_addition():
    """Test basic addition functionality."""
    # Arrange
    a = 1
    b = 2
    
    # Act
    result = add(a, b)
    
    # Assert
    assert result == 3
```

### 2. Test Class
```python
# Example: Test class structure
class TestCalculator:
    def setup_method(self):
        """Set up test environment."""
        self.calculator = Calculator()
    
    def teardown_method(self):
        """Clean up test environment."""
        self.calculator = None
    
    def test_addition(self):
        """Test addition operation."""
        result = self.calculator.add(1, 2)
        assert result == 3
    
    def test_subtraction(self):
        """Test subtraction operation."""
        result = self.calculator.subtract(3, 1)
        assert result == 2
```

## Test Categories

### 1. Function Tests
```python
# Example: Function tests
def test_string_operations():
    """Test string manipulation functions."""
    # Test concatenation
    result = concatenate("Hello", "World")
    assert result == "HelloWorld"
    
    # Test splitting
    parts = split_string("Hello,World", ",")
    assert parts == ["Hello", "World"]
```

### 2. Class Tests
```python
# Example: Class tests
class TestUser:
    def test_user_creation(self):
        """Test user object creation."""
        user = User("john", "john@example.com")
        assert user.username == "john"
        assert user.email == "john@example.com"
    
    def test_user_validation(self):
        """Test user data validation."""
        with pytest.raises(ValueError):
            User("", "invalid-email")
```

## Test Fixtures

### 1. Basic Fixture
```python
# Example: Basic fixture
import pytest

@pytest.fixture
def sample_data():
    """Provide sample test data."""
    return {
        "name": "Test User",
        "age": 30,
        "email": "test@example.com"
    }

def test_user_creation(sample_data):
    """Test user creation with fixture data."""
    user = User(**sample_data)
    assert user.name == sample_data["name"]
    assert user.age == sample_data["age"]
```

### 2. Advanced Fixture
```python
# Example: Advanced fixture
@pytest.fixture(scope="class")
def database():
    """Provide test database connection."""
    db = TestDatabase()
    db.connect()
    yield db
    db.disconnect()

class TestUserRepository:
    def test_user_creation(self, database):
        """Test user creation in database."""
        user = User("test", "test@example.com")
        database.save(user)
        assert database.find_by_email("test@example.com") is not None
```

## Mocking and Stubbing

### 1. Basic Mocking
```python
# Example: Basic mocking
from unittest.mock import Mock, patch

def test_external_service():
    """Test external service interaction."""
    mock_service = Mock()
    mock_service.get_data.return_value = {"status": "success"}
    
    result = process_data(mock_service)
    assert result["status"] == "success"
```

### 2. Advanced Mocking
```python
# Example: Advanced mocking
@patch('external_service.API')
def test_api_interaction(mock_api):
    """Test API interaction with mocking."""
    mock_api.return_value.get_data.return_value = {
        "id": 1,
        "name": "Test"
    }
    
    result = fetch_data()
    assert result["id"] == 1
    assert result["name"] == "Test"
```

## Test Organization

### 1. Test Directory Structure
```
tests/
├── unit/
│   ├── test_calculator.py
│   ├── test_user.py
│   └── test_utils.py
├── integration/
│   ├── test_api.py
│   └── test_database.py
└── conftest.py
```

### 2. Test Naming
- Clear and descriptive
- Follow pattern: test_<function>_<scenario>
- Include expected outcome
- Use consistent format
- Avoid abbreviations

## Test Execution

### 1. Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_calculator.py

# Run specific test
pytest tests/unit/test_calculator.py::test_addition

# Run with coverage
pytest --cov=src tests/
```

### 2. Test Reports
- HTML reports
- XML reports
- Coverage reports
- Test summaries
- Failure details

## Best Practices

### 1. Test Design
- One assertion per test
- Clear test names
- Proper setup/teardown
- Meaningful test data
- Isolated tests

### 2. Test Maintenance
- Regular updates
- Remove obsolete tests
- Update test data
- Review coverage
- Document changes

## Related Documentation
- See `docs/development/testing/integration_testing.md` for integration testing
- See `docs/development/testing/security_testing.md` for security testing
- See `docs/framework/patterns/testing_patterns.md` for testing patterns

## Key Principles

### 1. Specification-Driven Testing
- Tests must directly validate specification requirements
- Each specification requirement should have corresponding test cases
- Test cases should be written before implementation (TDD approach)

### 2. Test Organization
- Tests should mirror the project structure
- Each module should have its own test suite
- Test files should be named `test_<module_name>.py`

### 3. Test Coverage
- Aim for 100% coverage of specification requirements
- Focus on behavior coverage over code coverage
- Document any intentional coverage gaps

## Implementation Guidelines

### Test Structure
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

import pytest
from typing import Any, Dict

class TestSpecificationRequirement:
    """Test suite for a specific specification requirement."""
    
    def test_requirement_validation(self) -> None:
        """Test that the implementation meets the requirement."""
        # Test implementation
        pass

    def test_edge_cases(self) -> None:
        """Test edge cases and boundary conditions."""
        # Edge case tests
        pass

    def test_error_handling(self) -> None:
        """Test error handling and recovery."""
        # Error handling tests
        pass
```

### Best Practices
1. Use descriptive test names
2. Follow the Arrange-Act-Assert pattern
3. Keep tests independent and isolated
4. Use fixtures for common setup
5. Mock external dependencies

### Test Categories
1. **Requirement Tests**
   - Validate core functionality
   - Test against specification requirements
   - Verify expected behavior

2. **Edge Case Tests**
   - Test boundary conditions
   - Validate error handling
   - Check edge case behavior

3. **Integration Tests**
   - Test component interactions
   - Verify data flow
   - Validate system behavior

## Tools and Frameworks

### Primary Tools
- pytest for test execution
- coverage.py for coverage analysis
- mypy for type checking
- black for code formatting

### Configuration
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

# pytest.ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = --verbose --cov=src --cov-report=term-missing
```

## Common Patterns

### Fixture Usage
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

import pytest
from typing import Generator, Any

@pytest.fixture
def test_data() -> Generator[Dict[str, Any], None, None]:
    """Provide test data for test cases."""
    data = {
        "input": "test_input",
        "expected": "test_output"
    }
    yield data
```

### Mocking
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

from unittest.mock import Mock, patch

def test_with_mock() -> None:
    """Test using mock objects."""
    with patch('module.function') as mock_func:
        mock_func.return_value = "mocked_result"
        # Test implementation
```

## Troubleshooting

### Common Issues
1. **Test Isolation**
   - Problem: Tests affecting each other
   - Solution: Use fixtures and proper cleanup

2. **Mocking Complexity**
   - Problem: Complex mock setups
   - Solution: Use factory functions for mocks

3. **Test Maintenance**
   - Problem: Brittle tests
   - Solution: Focus on behavior over implementation

## Version History
- v1.0.0 (2025-01-01): Initial release
- v1.1.0 (2025-02-01): Added troubleshooting section
- v1.2.0 (2025-03-01): Updated best practices

## References
- [SpecFirst Testing Guide](../framework/best_practices/testing_guide.md)
- [Python Testing Best Practices](../framework/best_practices/python_testing.md)
- [SpecFirst Methodology](../framework/methodology/AGILE_SPECFIRST.md) 