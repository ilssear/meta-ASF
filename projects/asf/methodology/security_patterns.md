# Security Patterns

## Overview
This document outlines security patterns and best practices for the SpecFirst framework. These patterns integrate **Test-Driven Development (TDD)** for security validation and follow **PERA cycles** (Plan-Execute-Report/Review-Adjust) for continuous security improvement.

## TDD for Security Testing

### Security-First TDD Pattern
Security patterns are validated through TDD to ensure robust protection:

```python
# Example: Security TDD pattern
def test_security_requirements_tdd():
    """Example of TDD workflow for security features."""
    # RED: Write failing security test first
    def test_password_validation():
        """Test password security requirements."""
        # Should reject weak passwords
        with pytest.raises(SecurityError):
            create_user({"password": "123"})  # Too weak
        
        # Should accept strong passwords
        user = create_user({"password": "SecurePass123!"})
        assert user.password_hash is not None
    
    # GREEN: Implement security measures
    def create_user(user_data):
        if not is_strong_password(user_data["password"]):
            raise SecurityError("Password too weak")
        user = User(**user_data)
        user.password_hash = hash_password(user_data["password"])
        return user
    
    # REFACTOR: Enhance security while keeping tests green
    def create_user(user_data):
        validate_password_strength(user_data["password"])
        user = User(**user_data)
        user.password_hash = hash_password_with_salt(user_data["password"])
        user.salt = generate_salt()
        return user
```

### Security Testing with PERA Cycles
Security patterns evolve through PERA cycles for continuous improvement:

1. **Plan**: Define security requirements and threat models
2. **Execute**: Implement security measures with TDD validation
3. **Report/Review**: Assess security effectiveness and identify gaps
4. **Adjust**: Enhance security patterns based on findings

## Core Security Principles

### 1. Defense in Depth
- Multiple layers of security
- Redundant security measures
- Fail-safe defaults
- Regular security audits
- Continuous monitoring

### 2. Least Privilege
- Minimal required permissions
- Role-based access control
- Regular permission reviews
- Principle of least authority
- Access logging

### 3. Secure by Default
- Secure configurations
- Default security settings
- Security templates
- Regular updates
- Security documentation

## Implementation Patterns

### 1. Authentication
```python
# Example: Secure authentication pattern
from typing import Optional
import hashlib
import secrets

def authenticate_user(username: str, password: str) -> Optional[str]:
    """
    Authenticate a user with secure password handling.
    
    Args:
        username: User's username
        password: User's password
        
    Returns:
        Optional[str]: Session token if authentication successful
    """
    # Get stored credentials
    stored_hash = get_stored_hash(username)
    if not stored_hash:
        return None
        
    # Verify password
    if not verify_password(password, stored_hash):
        return None
        
    # Generate secure session token
    return secrets.token_urlsafe(32)
```

### 2. Authorization
```python
# Example: Role-based authorization pattern
from enum import Enum
from typing import List, Set

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class Authorization:
    def __init__(self):
        self.role_permissions: Dict[Role, Set[str]] = {
            Role.ADMIN: {"read", "write", "delete", "admin"},
            Role.USER: {"read", "write"},
            Role.GUEST: {"read"}
        }
    
    def check_permission(self, role: Role, permission: str) -> bool:
        """Check if role has permission."""
        return permission in self.role_permissions.get(role, set())
```

### 3. Data Protection
```python
# Example: Secure data handling pattern
from cryptography.fernet import Fernet
import base64

class SecureData:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.cipher.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        return self.cipher.decrypt(encrypted_data.encode()).decode()
```

## Security Best Practices

### 1. Input Validation
- Validate all inputs
- Sanitize user data
- Use type checking
- Implement input limits
- Log validation failures

### 2. Output Encoding
- Encode all outputs
- Prevent XSS attacks
- Use secure templates
- Validate content types
- Implement CSP

### 3. Error Handling
- Secure error messages
- Log security events
- Implement rate limiting
- Use secure defaults
- Regular security reviews

## Security Testing

### 1. Unit Testing
```python
# Example: Security test pattern
import pytest
from unittest.mock import patch

def test_authentication_security():
    """Test authentication security measures."""
    # Test password hashing
    password = "secure_password"
    hashed = hash_password(password)
    assert hashed != password
    
    # Test brute force protection
    with patch('time.sleep') as mock_sleep:
        for _ in range(5):
            authenticate_user("user", "wrong_password")
        assert mock_sleep.call_count == 5
```

### 2. Integration Testing
```python
# Example: Security integration test
def test_secure_data_flow():
    """Test secure data flow through system."""
    # Test data encryption
    secure_data = SecureData()
    original = "sensitive_data"
    encrypted = secure_data.encrypt_data(original)
    decrypted = secure_data.decrypt_data(encrypted)
    assert decrypted == original
```

## Security Monitoring

### 1. Logging
```python
# Example: Security logging pattern
import logging
from datetime import datetime

class SecurityLogger:
    def __init__(self):
        self.logger = logging.getLogger("security")
        self.logger.setLevel(logging.INFO)
        
    def log_security_event(self, event_type: str, details: dict):
        """Log security-related events."""
        self.logger.info({
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "details": details
        })
```

### 2. Monitoring
- Real-time monitoring
- Alert thresholds
- Incident response
- Security metrics
- Regular reviews

## Continuous Security Improvement with PERA Cycles

### Security Pattern Evolution
Security patterns evolve through PERA cycles to address emerging threats:

```python
# Example: Security pattern evolution through PERA cycles
class SecurityPatternEvolution:
    """Example of how security patterns evolve through PERA cycles."""
    
    # Initial security pattern (Plan phase)
    def test_basic_authentication(self):
        """Basic authentication test."""
        user = authenticate_user("user", "password")
        assert user is not None
    
    # Enhanced security pattern (Execute phase with TDD)
    def test_authentication_with_rate_limiting(self):
        """Enhanced authentication with rate limiting."""
        # RED: Test rate limiting requirements
        for _ in range(5):
            authenticate_user("user", "wrong_password")
        
        # Should be blocked after 5 attempts
        with pytest.raises(RateLimitError):
            authenticate_user("user", "wrong_password")
    
    # Comprehensive security pattern (Report/Review phase)
    def test_authentication_with_multifactor(self):
        """Comprehensive authentication with MFA."""
        # Test MFA requirements
        user = authenticate_user("user", "password")
        assert user.requires_mfa
        
        # Test MFA validation
        mfa_code = generate_mfa_code(user)
        session = validate_mfa(user, mfa_code)
        assert session.is_authenticated
    
    # Advanced security pattern (Adjust phase)
    def test_authentication_with_adaptive_security(self):
        """Advanced authentication with adaptive security."""
        # Test adaptive security based on risk
        low_risk_session = authenticate_user("user", "password", risk_level="low")
        assert not low_risk_session.requires_mfa
        
        high_risk_session = authenticate_user("user", "password", risk_level="high")
        assert high_risk_session.requires_mfa
```

### Security Quality Assurance Integration
Security patterns integrate with the overall quality assurance process:

1. **TDD for Security Validation**: Validate security measures with comprehensive tests
2. **TDD for Threat Modeling**: Use tests to validate threat mitigation strategies
3. **TDD for Compliance**: Ensure security patterns meet compliance requirements
4. **PERA for Security Evolution**: Iteratively improve security patterns based on threats

## Related Documentation
- See `docs/framework/best_practices/implementation_guide.md` for implementation details
- See `docs/development/testing/security_testing.md` for security testing
- See `docs/framework/patterns/testing_patterns.md` for testing patterns 