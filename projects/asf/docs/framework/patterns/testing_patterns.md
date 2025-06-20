# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Testing Patterns Guide

## Overview
This guide provides comprehensive patterns and best practices for testing projects following the SpecFirst framework methodology.

## Core Patterns

### 1. Testing Structure
- Unit testing
- Integration testing
- System testing
- Performance testing
- Security testing

### 2. Testing Types
- Functional testing
- Non-functional testing
- Regression testing
- Acceptance testing
- Exploratory testing

### 3. Testing Tools
- Test frameworks
- Test runners
- Test coverage
- Test reporting
- Test automation

### 4. Testing Process
- Test planning
- Test execution
- Test reporting
- Test maintenance
- Test improvement

## Implementation Patterns

### 1. Testing Structure
- Clear unit tests
- Clear integration tests
- Clear system tests
- Clear performance tests
- Clear security tests

### 2. Testing Types
- Clear functional tests
- Clear non-functional tests
- Clear regression tests
- Clear acceptance tests
- Clear exploratory tests

### 3. Testing Tools
- Reliable frameworks
- Reliable runners
- Good coverage
- Good reporting
- Good automation

### 4. Testing Process
- Clear planning
- Clear execution
- Clear reporting
- Clear maintenance
- Clear improvement

## Best Practices

### 1. Testing Structure
- Clear unit tests
- Clear integration tests
- Clear system tests
- Clear performance tests
- Clear security tests

### 2. Testing Types
- Clear functional tests
- Clear non-functional tests
- Clear regression tests
- Clear acceptance tests
- Clear exploratory tests

### 3. Testing Tools
- Reliable frameworks
- Reliable runners
- Good coverage
- Good reporting
- Good automation

### 4. Testing Process
- Clear planning
- Clear execution
- Clear reporting
- Clear maintenance
- Clear improvement

## Examples

### 1. Good Testing
```python
import pytest
from typing import Dict, Any
from datetime import datetime
from unittest.mock import Mock, patch

class TestUserService:
    """Comprehensive test suite for user service."""
    
    @pytest.fixture
    def user_service(self):
        """Create user service instance."""
        from app.services.user import UserService
        return UserService()
    
    @pytest.fixture
    def mock_db(self):
        """Create mock database."""
        return Mock()
    
    def test_create_user(self, user_service, mock_db):
        """Test user creation."""
        # Arrange
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        mock_db.create_user.return_value = {
            "id": "123",
            "username": user_data["username"],
            "email": user_data["email"],
            "created_at": datetime.now()
        }
        
        # Act
        result = user_service.create_user(user_data, mock_db)
        
        # Assert
        assert result["username"] == user_data["username"]
        assert result["email"] == user_data["email"]
        mock_db.create_user.assert_called_once_with(user_data)
    
    def test_get_user(self, user_service, mock_db):
        """Test user retrieval."""
        # Arrange
        user_id = "123"
        mock_db.get_user.return_value = {
            "id": user_id,
            "username": "testuser",
            "email": "test@example.com"
        }
        
        # Act
        result = user_service.get_user(user_id, mock_db)
        
        # Assert
        assert result["id"] == user_id
        mock_db.get_user.assert_called_once_with(user_id)
    
    @pytest.mark.parametrize("user_data,expected_error", [
        ({"username": ""}, "Username is required"),
        ({"email": "invalid"}, "Invalid email format"),
        ({"password": "123"}, "Password too short")
    ])
    def test_validate_user_data(self, user_service, user_data, expected_error):
        """Test user data validation."""
        # Act & Assert
        with pytest.raises(ValueError) as exc_info:
            user_service.validate_user_data(user_data)
        assert str(exc_info.value) == expected_error
    
    @patch("app.services.user.send_welcome_email")
    def test_welcome_email(self, mock_send_email, user_service, mock_db):
        """Test welcome email sending."""
        # Arrange
        user_id = "123"
        mock_db.get_user.return_value = {
            "id": user_id,
            "email": "test@example.com"
        }
        
        # Act
        user_service.send_welcome_email(user_id, mock_db)
        
        # Assert
        mock_send_email.assert_called_once_with("test@example.com")
```

### 2. Poor Testing
```python
def test_user():
    user = create_user("test", "test@example.com")
    assert user.username == "test"
```

## Common Pitfalls

### 1. Testing Structure
- Missing unit tests
- Missing integration tests
- Missing system tests
- Missing performance tests
- Missing security tests

### 2. Testing Types
- Missing functional tests
- Missing non-functional tests
- Missing regression tests
- Missing acceptance tests
- Missing exploratory tests

### 3. Testing Tools
- Unreliable frameworks
- Unreliable runners
- Poor coverage
- Poor reporting
- Poor automation

### 4. Testing Process
- Missing planning
- Missing execution
- Missing reporting
- Missing maintenance
- Missing improvement

## References
- [Specification Guide](../best_practices/specification_guide.md)
- [Implementation Guide](../best_practices/implementation_guide.md)
- [Deployment Guide](../best_practices/deployment_guide.md)
- [Security Guide](../security/README.md)
- [Style Guide](../style/README.md)
- [Agile SpecFirst Methodology](../methodology/AGILE_SPECFIRST.md) 