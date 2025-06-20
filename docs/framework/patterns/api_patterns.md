# API Patterns Guide - Agile SpecFirst Framework

## 🎯 Core Principles

### 1. RESTful Design
- Resource-oriented URLs
- Standard HTTP methods
- Stateless operations
- Consistent response formats

### 2. Security First
- Authentication required
- Input validation
- Rate limiting
- Error handling

### 3. Documentation
- OpenAPI/Swagger specs
- Example requests/responses
- Error scenarios
- Authentication details

## 💻 API Standards

### 1. URL Structure
```
# Base URL
https://api.example.com/v1

# Resource endpoints
GET    /users              # List users
POST   /users              # Create user
GET    /users/{id}         # Get user
PUT    /users/{id}         # Update user
DELETE /users/{id}         # Delete user

# Nested resources
GET    /users/{id}/posts   # List user posts
POST   /users/{id}/posts   # Create user post
GET    /users/{id}/posts/{post_id}  # Get user post
```

### 2. Request/Response Format
```python
# Request
{
    "data": {
        "type": "user",
        "attributes": {
            "name": "John Doe",
            "email": "john@example.com"
        }
    }
}

# Response
{
    "data": {
        "type": "user",
        "id": "123",
        "attributes": {
            "name": "John Doe",
            "email": "john@example.com",
            "created_at": "2025-01-20T12:00:00Z"
        }
    },
    "meta": {
        "version": "1.0.0"
    }
}
```

### 3. Error Handling
```python
# Error Response
{
    "errors": [{
        "status": "400",
        "code": "invalid_input",
        "title": "Invalid Input",
        "detail": "Email format is invalid",
        "source": {
            "pointer": "/data/attributes/email"
        }
    }]
}
```

## 🛠️ Implementation Patterns

### 1. Flask API Example
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
API implementation example.
"""

from typing import Dict, List, Optional
from flask import Flask, request, jsonify
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/api/v1/users", methods=["GET"])
def list_users() -> Dict:
    """
    List all users.

    Returns:
        Dict: User list response.
    """
    try:
        users = get_users()
        return {
            "data": [user.to_dict() for user in users],
            "meta": {"version": "1.0.0"}
        }
    except Exception as e:
        logger.exception("Failed to list users: %s", e)
        return error_response(500, "internal_error", str(e))

@app.route("/api/v1/users", methods=["POST"])
def create_user() -> Dict:
    """
    Create a new user.

    Returns:
        Dict: Created user response.
    """
    try:
        data = request.get_json()
        validate_user_data(data)
        user = create_user(data)
        return {
            "data": user.to_dict(),
            "meta": {"version": "1.0.0"}
        }, 201
    except ValueError as e:
        return error_response(400, "invalid_input", str(e))
    except Exception as e:
        logger.exception("Failed to create user: %s", e)
        return error_response(500, "internal_error", str(e))
```

### 2. FastAPI Example
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
FastAPI implementation example.
"""

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

class UserCreate(BaseModel):
    """User creation model."""
    name: str
    email: EmailStr

class UserResponse(BaseModel):
    """User response model."""
    id: str
    name: str
    email: str
    created_at: datetime

@app.get("/api/v1/users", response_model=List[UserResponse])
async def list_users() -> List[UserResponse]:
    """
    List all users.

    Returns:
        List[UserResponse]: List of users.
    """
    try:
        users = await get_users()
        return [UserResponse.from_orm(user) for user in users]
    except Exception as e:
        logger.exception("Failed to list users: %s", e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/v1/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate) -> UserResponse:
    """
    Create a new user.

    Args:
        user: User creation data.

    Returns:
        UserResponse: Created user.

    Raises:
        HTTPException: If creation fails.
    """
    try:
        created_user = await create_user(user.dict())
        return UserResponse.from_orm(created_user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("Failed to create user: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
```

## ✅ Best Practices

### 1. Authentication
- Use JWT tokens
- Implement refresh tokens
- Secure password storage
- Rate limiting

### 2. Validation
- Input validation
- Output sanitization
- Type checking
- Schema validation

### 3. Error Handling
- Consistent error format
- Proper status codes
- Detailed error messages
- Error logging

### 4. Documentation
- OpenAPI specification
- Example requests
- Error scenarios
- Authentication flow

## ❌ Common Pitfalls

### 1. Security Issues
- ❌ Missing authentication
- ❌ Insecure endpoints
- ❌ No rate limiting
- ❌ Exposed sensitive data

### 2. Design Issues
- ❌ Inconsistent URLs
- ❌ Poor error handling
- ❌ Missing validation
- ❌ Unclear documentation

### 3. Performance Issues
- ❌ No caching
- ❌ Inefficient queries
- ❌ No pagination
- ❌ Missing compression

## 📚 Examples

### 1. Good API Design
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Well-designed API example.
"""

from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, EmailStr, validator
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

class UserBase(BaseModel):
    """Base user model."""
    name: str
    email: EmailStr

    @validator('name')
    def name_must_not_be_empty(cls, v):
        """Validate name is not empty."""
        if not v.strip():
            raise ValueError('name must not be empty')
        return v

class UserCreate(UserBase):
    """User creation model."""
    password: str

    @validator('password')
    def password_must_be_strong(cls, v):
        """Validate password strength."""
        if len(v) < 8:
            raise ValueError('password must be at least 8 characters')
        return v

class UserResponse(UserBase):
    """User response model."""
    id: str
    created_at: datetime

    class Config:
        """Pydantic config."""
        orm_mode = True

@app.get("/api/v1/users", response_model=List[UserResponse])
async def list_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserResponse = Depends(get_current_user)
) -> List[UserResponse]:
    """
    List users with pagination.

    Args:
        skip: Number of records to skip.
        limit: Maximum number of records to return.
        current_user: Current authenticated user.

    Returns:
        List[UserResponse]: List of users.

    Raises:
        HTTPException: If listing fails.
    """
    try:
        users = await get_users(skip=skip, limit=limit)
        return [UserResponse.from_orm(user) for user in users]
    except Exception as e:
        logger.exception("Failed to list users: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
```

### 2. Poor API Design
```python
@app.route("/users", methods=["GET"])
def get_users():
    users = db.query("SELECT * FROM users")
    return jsonify(users)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    db.execute("INSERT INTO users VALUES (%s, %s)", data["name"], data["email"])
    return jsonify({"status": "success"})
```

## Version History

### v1.0.0 (2025-01-15)
- Initial API patterns
- Basic standards
- Common pitfalls

### v1.1.0 (2025-01-20)
- Enhanced examples
- Detailed standards
- Best practices

## References
- [Agile SpecFirst Framework](../methodology/AGILE_SPECFIRST.md)
- [Implementation Guide](../best_practices/implementation_guide.md)
- [Best Practices Guide](../best_practices/README.md) 