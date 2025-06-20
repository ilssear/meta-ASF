# Testing Patterns

## Overview
This document outlines common testing patterns and best practices for the SpecFirst framework. These patterns support **Test-Driven Development (TDD)** as a quality assurance tool and integrate with **PERA cycles** (Plan-Execute-Report/Review-Adjust) for continuous improvement.

## TDD as Quality Assurance Tool

### Test-Driven Development Pattern
Within the SpecFirst methodology, TDD serves as a quality assurance tool during code generation and debugging phases:

```python
# Example: TDD Red-Green-Refactor cycle
def test_user_creation_tdd():
    """Example of TDD workflow for user creation."""
    # RED: Write failing test first
    def test_create_user_with_valid_data():
        user_data = {"name": "Test User", "email": "test@example.com"}
        user = create_user(user_data)
        assert user.id is not None
        assert user.name == "Test User"
        assert user.email == "test@example.com"
    
    # GREEN: Implement minimal code to pass test
    def create_user(user_data):
        user = User(**user_data)
        user.id = generate_id()  # Minimal implementation
        return user
    
    # REFACTOR: Improve code while keeping tests green
    def create_user(user_data):
        user = User(**user_data)
        user.id = generate_uuid()  # Better implementation
        validate_user_data(user_data)  # Added validation
        return user
```

### TDD Integration with PERA Cycles
TDD patterns integrate with PERA cycles for continuous improvement:

1. **Plan**: Define test requirements and acceptance criteria
2. **Execute**: Write failing tests, implement code, refactor
3. **Report/Review**: Validate with TDD and user feedback
4. **Adjust**: Refine tests and implementation based on feedback

## Core Patterns

### 1. Arrange-Act-Assert
```python
# Example: Arrange-Act-Assert pattern
def test_user_creation():
    """Test user creation using AAA pattern."""
    # Arrange
    user_data = {
        "name": "Test User",
        "email": "test@example.com"
    }
    
    # Act
    user = create_user(user_data)
    
    # Assert
    assert user.name == user_data["name"]
    assert user.email == user_data["email"]
```

### 2. Given-When-Then
```python
# Example: Given-When-Then pattern
def test_user_login():
    """Test user login using GWT pattern."""
    # Given
    user = create_test_user()
    credentials = {
        "email": user.email,
        "password": "secure123"
    }
    
    # When
    result = login_user(credentials)
    
    # Then
    assert result.is_success
    assert result.session_token is not None
```

## Test Organization Patterns

### 1. Test Class Organization
```python
# Example: Test class organization
class TestUserManagement:
    """Test suite for user management functionality."""
    
    def setup_method(self):
        """Set up test environment."""
        self.user_service = UserService()
        self.test_data = TestData()
    
    def teardown_method(self):
        """Clean up test environment."""
        self.user_service.cleanup()
        self.test_data.cleanup()
    
    def test_user_creation(self):
        """Test user creation."""
        # Test implementation
    
    def test_user_update(self):
        """Test user update."""
        # Test implementation
    
    def test_user_deletion(self):
        """Test user deletion."""
        # Test implementation
```

### 2. Test Suite Organization
```python
# Example: Test suite organization
class TestUserAPI:
    """Test suite for user API endpoints."""
    
    def test_create_user(self):
        """Test user creation endpoint."""
        # Test implementation
    
    def test_get_user(self):
        """Test user retrieval endpoint."""
        # Test implementation
    
    def test_update_user(self):
        """Test user update endpoint."""
        # Test implementation

class TestProductAPI:
    """Test suite for product API endpoints."""
    
    def test_create_product(self):
        """Test product creation endpoint."""
        # Test implementation
    
    def test_get_product(self):
        """Test product retrieval endpoint."""
        # Test implementation
```

## Test Data Patterns

### 1. Test Data Factory
```python
# Example: Test data factory pattern
class TestDataFactory:
    """Factory for creating test data."""
    
    @staticmethod
    def create_user(**kwargs):
        """Create a test user."""
        default_data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "secure123"
        }
        default_data.update(kwargs)
        return User(**default_data)
    
    @staticmethod
    def create_product(**kwargs):
        """Create a test product."""
        default_data = {
            "name": "Test Product",
            "price": 99.99,
            "description": "Test description"
        }
        default_data.update(kwargs)
        return Product(**default_data)
```

### 2. Test Data Builder
```python
# Example: Test data builder pattern
class UserBuilder:
    """Builder for creating test users."""
    
    def __init__(self):
        self.user_data = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "secure123"
        }
    
    def with_name(self, name):
        """Set user name."""
        self.user_data["name"] = name
        return self
    
    def with_email(self, email):
        """Set user email."""
        self.user_data["email"] = email
        return self
    
    def build(self):
        """Build user object."""
        return User(**self.user_data)
```

## Mocking Patterns

### 1. Service Mock
```python
# Example: Service mock pattern
class MockUserService:
    """Mock implementation of user service."""
    
    def __init__(self):
        self.users = {}
    
    def create_user(self, user_data):
        """Create a mock user."""
        user = User(**user_data)
        self.users[user.id] = user
        return user
    
    def get_user(self, user_id):
        """Get a mock user."""
        return self.users.get(user_id)
```

### 2. Repository Mock
```python
# Example: Repository mock pattern
class MockUserRepository:
    """Mock implementation of user repository."""
    
    def __init__(self):
        self.users = {}
    
    def save(self, user):
        """Save a mock user."""
        self.users[user.id] = user
    
    def find_by_id(self, user_id):
        """Find a mock user by ID."""
        return self.users.get(user_id)
```

## Test Utility Patterns

### 1. Test Helper
```python
# Example: Test helper pattern
class TestHelper:
    """Helper functions for testing."""
    
    @staticmethod
    def create_test_user():
        """Create a test user."""
        return User(
            name="Test User",
            email="test@example.com",
            password="secure123"
        )
    
    @staticmethod
    def create_test_product():
        """Create a test product."""
        return Product(
            name="Test Product",
            price=99.99,
            description="Test description"
        )
```

### 2. Test Assertion
```python
# Example: Test assertion pattern
class TestAssertions:
    """Custom assertions for testing."""
    
    @staticmethod
    def assert_user_created(user):
        """Assert user was created correctly."""
        assert user.id is not None
        assert user.name is not None
        assert user.email is not None
    
    @staticmethod
    def assert_product_created(product):
        """Assert product was created correctly."""
        assert product.id is not None
        assert product.name is not None
        assert product.price > 0
```

## Continuous Improvement with PERA Cycles

### Testing Pattern Evolution
Testing patterns evolve through PERA cycles to improve quality and maintainability:

```python
# Example: Pattern evolution through PERA cycles
class TestPatternEvolution:
    """Example of how testing patterns evolve through PERA cycles."""
    
    # Initial pattern (Plan phase)
    def test_basic_user_creation(self):
        """Basic test pattern."""
        user = create_user({"name": "Test"})
        assert user.name == "Test"
    
    # Enhanced pattern (Execute phase with TDD)
    def test_user_creation_with_validation(self):
        """Enhanced test pattern with validation."""
        # RED: Test validation requirements
        with pytest.raises(ValueError):
            create_user({"name": ""})  # Invalid name
        
        # GREEN: Implement validation
        user = create_user({"name": "Valid Name"})
        assert user.name == "Valid Name"
    
    # Refined pattern (Report/Review phase)
    def test_user_creation_with_comprehensive_validation(self):
        """Comprehensive test pattern."""
        # Test edge cases and error conditions
        test_cases = [
            {"name": "", "expected": ValueError},
            {"name": "A" * 101, "expected": ValueError},  # Too long
            {"name": "Valid Name", "expected": User}
        ]
        
        for case in test_cases:
            if case["expected"] == ValueError:
                with pytest.raises(ValueError):
                    create_user({"name": case["name"]})
            else:
                user = create_user({"name": case["name"]})
                assert isinstance(user, User)
    
    # Optimized pattern (Adjust phase)
    def test_user_creation_with_factory_pattern(self):
        """Optimized test pattern using factory."""
        # Use test data factory for better maintainability
        user = TestDataFactory.create_user(name="Factory User")
        assert user.name == "Factory User"
```

### Quality Assurance Integration
Testing patterns integrate with the overall quality assurance process:

1. **TDD for Code Generation**: Validate AI-generated code with comprehensive tests
2. **TDD for Debugging**: Use tests to identify and fix issues systematically
3. **TDD for Refinement**: Validate specification changes maintain functionality
4. **PERA for Continuous Improvement**: Iteratively improve testing patterns and coverage

## Related Documentation
- See `docs/development/testing/unit_testing.md` for unit testing
- See `docs/development/testing/integration_testing.md` for integration testing
- See `docs/development/testing/security_testing.md` for security testing 