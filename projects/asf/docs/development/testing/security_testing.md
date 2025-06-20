# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Security Testing Guide

## Overview

This guide outlines security testing strategies and procedures for the SpecFirst framework, ensuring comprehensive security validation and vulnerability assessment.

## Security Testing Strategy

### 1. Security Test Types
- **Authentication Testing**
  - Login functionality
  - Password validation
  - Session management
  - Multi-factor authentication
  - Account lockout mechanisms

- **Authorization Testing**
  - Role-based access control
  - Permission validation
  - Resource access control
  - API endpoint security
  - Data access restrictions

- **Input Validation Testing**
  - SQL injection prevention
  - XSS protection
  - CSRF protection
  - File upload security
  - Command injection prevention

- **Data Protection Testing**
  - Encryption validation
  - Secure transmission
  - Data sanitization
  - Privacy compliance
  - Audit logging

### 2. Security Test Organization
```python
# Example security test structure
class TestSecurity:
    """Security test suite for the application."""
    
    def test_authentication(self):
        """Test authentication mechanisms."""
        # Test valid login
        # Test invalid credentials
        # Test account lockout
        # Test session management
    
    def test_authorization(self):
        """Test authorization controls."""
        # Test role-based access
        # Test permission checks
        # Test resource protection
        # Test API security
    
    def test_input_validation(self):
        """Test input validation and sanitization."""
        # Test SQL injection prevention
        # Test XSS protection
        # Test CSRF protection
        # Test file upload security
```

## Security Testing Procedures

### 1. Authentication Testing
```python
# Example authentication test
def test_user_authentication():
    """Test user authentication functionality."""
    
    # Test valid login
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "secure123"
    })
    assert response.status_code == 200
    assert "token" in response.json()
    
    # Test invalid credentials
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401
    
    # Test account lockout
    for _ in range(5):
        client.post("/auth/login", json={
            "username": "testuser",
            "password": "wrongpassword"
        })
    
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "secure123"
    })
    assert response.status_code == 423  # Account locked
```

### 2. Authorization Testing
```python
# Example authorization test
def test_role_based_access():
    """Test role-based access control."""
    
    # Test admin access
    admin_token = get_auth_token("admin")
    response = client.get("/admin/users", headers={
        "Authorization": f"Bearer {admin_token}"
    })
    assert response.status_code == 200
    
    # Test user access denied
    user_token = get_auth_token("user")
    response = client.get("/admin/users", headers={
        "Authorization": f"Bearer {user_token}"
    })
    assert response.status_code == 403
```

### 3. Input Validation Testing
```python
# Example input validation test
def test_sql_injection_prevention():
    """Test SQL injection prevention."""
    
    malicious_input = "'; DROP TABLE users; --"
    response = client.post("/api/users", json={
        "name": malicious_input,
        "email": "test@example.com"
    })
    
    # Should not cause database error
    assert response.status_code in [400, 422]
    
    # Verify table still exists
    response = client.get("/api/users")
    assert response.status_code == 200
```

## Security Test Implementation

### 1. Security Test Setup
```python
# Security test configuration
import pytest
from unittest.mock import patch

class SecurityTestConfig:
    """Configuration for security tests."""
    
    def __init__(self):
        self.test_users = {
            "admin": {"username": "admin", "password": "admin123"},
            "user": {"username": "user", "password": "user123"},
            "guest": {"username": "guest", "password": "guest123"}
        }
        
        self.malicious_inputs = [
            "<script>alert('xss')</script>",
            "'; DROP TABLE users; --",
            "../../../etc/passwd",
            "{{7*7}}",
            "javascript:alert('xss')"
        ]
```

### 2. Security Test Execution
```bash
# Run security tests
pytest tests/security/ -v

# Run specific security test categories
pytest tests/security/test_authentication.py -v
pytest tests/security/test_authorization.py -v
pytest tests/security/test_input_validation.py -v

# Run with security reporting
pytest tests/security/ --html=security-report.html
```

## Security Best Practices

### 1. Test Design
- **Comprehensive coverage**: Test all security aspects
- **Realistic scenarios**: Use realistic attack vectors
- **Edge cases**: Test boundary conditions
- **Error handling**: Verify secure error responses
- **Logging validation**: Ensure security events are logged

### 2. Test Maintenance
- **Regular updates**: Keep tests current with threats
- **Vulnerability tracking**: Monitor new security issues
- **Tool integration**: Use security testing tools
- **Automation**: Automate security test execution
- **Reporting**: Generate security test reports

### 3. Security Tools
- **Static analysis**: Use tools like Bandit for Python
- **Dynamic testing**: Use tools like OWASP ZAP
- **Dependency scanning**: Use tools like Safety
- **Container scanning**: Use tools like Trivy
- **Code review**: Manual security code review

## Security Testing Checklist

### Authentication
- [ ] Valid login works correctly
- [ ] Invalid credentials are rejected
- [ ] Account lockout after failed attempts
- [ ] Session management is secure
- [ ] Password requirements are enforced
- [ ] Multi-factor authentication works
- [ ] Password reset functionality is secure

### Authorization
- [ ] Role-based access control works
- [ ] Users can only access authorized resources
- [ ] API endpoints are properly protected
- [ ] Data access is restricted by user role
- [ ] Admin functions require admin privileges
- [ ] Guest access is properly limited

### Input Validation
- [ ] SQL injection attempts are blocked
- [ ] XSS attacks are prevented
- [ ] CSRF protection is implemented
- [ ] File uploads are validated
- [ ] Command injection is prevented
- [ ] Input length limits are enforced

### Data Protection
- [ ] Sensitive data is encrypted
- [ ] Data transmission is secure
- [ ] Audit logs are maintained
- [ ] Data retention policies are followed
- [ ] Privacy requirements are met
- [ ] Data disposal is secure

## References
- [Unit Testing Guide](unit_testing.md) - Unit testing fundamentals
- [Integration Testing Guide](integration_testing.md) - Integration testing
- [Security Patterns](../../framework/patterns/security_patterns.md) - Security patterns
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) - OWASP testing guide 