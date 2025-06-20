# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Security Patterns Guide

## Overview
This guide provides comprehensive patterns and best practices for implementing security in projects following the SpecFirst framework methodology.

## Core Patterns

### 1. Security Structure
- Authentication
- Authorization
- Data protection
- Network security
- Security monitoring

### 2. Security Types
- User security
- Data security
- System security
- Network security
- Application security

### 3. Security Tools
- Authentication tools
- Authorization tools
- Encryption tools
- Monitoring tools
- Testing tools

### 4. Security Process
- Security assessment
- Security testing
- Security monitoring
- Incident response
- Security updates

## Implementation Patterns

### 1. Security Structure
- Strong authentication
- Clear authorization
- Data encryption
- Network protection
- Security monitoring

### 2. Security Types
- User protection
- Data protection
- System protection
- Network protection
- Application protection

### 3. Security Tools
- Reliable auth
- Reliable authz
- Strong encryption
- Good monitoring
- Good testing

### 4. Security Process
- Regular assessment
- Regular testing
- Regular monitoring
- Quick response
- Regular updates

## Best Practices

### 1. Security Structure
- Strong authentication
- Clear authorization
- Data encryption
- Network protection
- Security monitoring

### 2. Security Types
- User protection
- Data protection
- System protection
- Network protection
- Application protection

### 3. Security Tools
- Reliable auth
- Reliable authz
- Strong encryption
- Good monitoring
- Good testing

### 4. Security Process
- Regular assessment
- Regular testing
- Regular monitoring
- Quick response
- Regular updates

## Examples

### 1. Good Security
```python
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import jwt
import bcrypt
from cryptography.fernet import Fernet
from pydantic import BaseModel, SecretStr

class SecurityManager:
    """Comprehensive security with authentication and encryption."""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)
    
    def hash_password(self, password: str) -> str:
        """Hash password securely."""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt).decode()
    
    def verify_password(self, password: str, hashed: str) -> bool:
        """Verify password against hash."""
        return bcrypt.checkpw(password.encode(), hashed.encode())
    
    def generate_token(self, user_id: str, expires_delta: Optional[timedelta] = None) -> str:
        """Generate JWT token."""
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        
        to_encode = {
            "sub": user_id,
            "exp": expire
        }
        return jwt.encode(to_encode, self.secret_key, algorithm="HS256")
    
    def verify_token(self, token: str) -> Dict[str, Any]:
        """Verify JWT token."""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=["HS256"])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired")
        except jwt.JWTError:
            raise ValueError("Invalid token")
    
    def encrypt_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.cipher_suite.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
    
    def validate_input(self, data: Dict[str, Any]) -> bool:
        """Validate user input."""
        # Implement input validation
        return True
    
    def sanitize_output(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize output data."""
        # Implement output sanitization
        return data

class User(BaseModel):
    """User model with security."""
    id: str
    username: str
    email: str
    password: SecretStr
    role: str
    
    class Config:
        json_encoders = {
            SecretStr: lambda v: v.get_secret_value()
        }
```

### 2. Poor Security
```python
def check_password(password, stored):
    return password == stored

def encrypt_data(data):
    return data
```

## Common Pitfalls

### 1. Security Structure
- Weak authentication
- Unclear authorization
- Missing encryption
- Poor network
- Missing monitoring

### 2. Security Types
- Poor user security
- Poor data security
- Poor system security
- Poor network security
- Poor application security

### 3. Security Tools
- Unreliable auth
- Unreliable authz
- Weak encryption
- Poor monitoring
- Poor testing

### 4. Security Process
- Missing assessment
- Missing testing
- Missing monitoring
- Slow response
- Missing updates

## References
- [Specification Guide](../best_practices/specification_guide.md)
- [Implementation Guide](../best_practices/implementation_guide.md)
- [Deployment Guide](../best_practices/deployment_guide.md)
- [Security Guide](../security/README.md)
- [Style Guide](../style/README.md)
- [Agile SpecFirst Methodology](../methodology/AGILE_SPECFIRST.md) 