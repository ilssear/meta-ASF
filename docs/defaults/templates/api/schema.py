# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Template for API schemas.

This template provides a standard structure for API schemas, including:
- Data models
- Validation rules
- Relationships
- Custom validators
"""

from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, validator, root_validator

# Base Models
class BaseSchema(BaseModel):
    """Base schema with common fields."""
    id: int = Field(..., description="Unique identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        """Pydantic model configuration."""
        orm_mode = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
        
# User Schema
class UserBase(BaseSchema):
    """Base user schema."""
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: str = Field(..., description="Email address")
    is_active: bool = Field(default=True, description="Whether the user is active")
    
    @validator('email')
    def validate_email(cls, v: str) -> str:
        """Validate email format.
        
        Args:
            v: Email address to validate
            
        Returns:
            str: Validated email address
            
        Raises:
            ValueError: If email is invalid
        """
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()
        
class UserCreate(UserBase):
    """Schema for creating a user."""
    password: str = Field(..., min_length=8, description="Password")
    
    @validator('password')
    def validate_password(cls, v: str) -> str:
        """Validate password strength.
        
        Args:
            v: Password to validate
            
        Returns:
            str: Validated password
            
        Raises:
            ValueError: If password is too weak
        """
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v
        
class UserUpdate(BaseModel):
    """Schema for updating a user."""
    username: Optional[str] = Field(None, min_length=3, max_length=50, description="Username")
    email: Optional[str] = Field(None, description="Email address")
    password: Optional[str] = Field(None, min_length=8, description="Password")
    is_active: Optional[bool] = Field(None, description="Whether the user is active")
    
class UserInDB(UserBase):
    """Schema for user in database."""
    hashed_password: str = Field(..., description="Hashed password")
    
class User(UserBase):
    """Schema for user response."""
    pass
    
# Item Schema
class ItemBase(BaseSchema):
    """Base item schema."""
    title: str = Field(..., min_length=1, max_length=100, description="Item title")
    description: Optional[str] = Field(None, description="Item description")
    owner_id: int = Field(..., description="ID of the item owner")
    
class ItemCreate(ItemBase):
    """Schema for creating an item."""
    pass
    
class ItemUpdate(BaseModel):
    """Schema for updating an item."""
    title: Optional[str] = Field(None, min_length=1, max_length=100, description="Item title")
    description: Optional[str] = Field(None, description="Item description")
    
class ItemInDB(ItemBase):
    """Schema for item in database."""
    pass
    
class Item(ItemBase):
    """Schema for item response."""
    owner: User = Field(..., description="Item owner")
    
# Response Schemas
class PaginatedResponse(BaseModel):
    """Schema for paginated responses."""
    items: List[Any] = Field(..., description="List of items")
    total: int = Field(..., description="Total number of items")
    page: int = Field(..., description="Current page number")
    size: int = Field(..., description="Number of items per page")
    pages: int = Field(..., description="Total number of pages")
    
class ErrorResponse(BaseModel):
    """Schema for error responses."""
    error: str = Field(..., description="Error message")
    code: int = Field(..., description="Error code")
    details: Optional[Dict[str, Any]] = Field(None, description="Error details") 