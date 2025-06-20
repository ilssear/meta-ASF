# Testing Patterns

## Overview
This document outlines common testing patterns and best practices for the SpecFirst framework.

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

## Related Documentation
- See `docs/development/testing/unit_testing.md` for unit testing
- See `docs/development/testing/integration_testing.md` for integration testing
- See `docs/development/testing/security_testing.md` for security testing 