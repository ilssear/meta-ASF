# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Template for API endpoints.

This template provides a standard structure for API endpoints, including:
- Request validation
- Response formatting
- Error handling
- Authentication
- Rate limiting
"""

from typing import Any, Dict, List, Optional, Union
from fastapi import APIRouter, Depends, HTTPException, Query, Path
from pydantic import BaseModel, Field

# Request Models
class RequestModel(BaseModel):
    """Base model for request data."""
    field1: str = Field(..., description="Description of field1")
    field2: Optional[int] = Field(None, description="Description of field2")
    
# Response Models
class ResponseModel(BaseModel):
    """Base model for response data."""
    status: str = Field(..., description="Status of the request")
    data: Dict[str, Any] = Field(..., description="Response data")
    message: Optional[str] = Field(None, description="Optional message")
    
# Error Models
class ErrorModel(BaseModel):
    """Base model for error responses."""
    error: str = Field(..., description="Error message")
    code: int = Field(..., description="Error code")
    details: Optional[Dict[str, Any]] = Field(None, description="Error details")
    
# Router
router = APIRouter(
    prefix="/api/v1",
    tags=["example"],
    responses={
        400: {"model": ErrorModel, "description": "Bad Request"},
        401: {"model": ErrorModel, "description": "Unauthorized"},
        403: {"model": ErrorModel, "description": "Forbidden"},
        404: {"model": ErrorModel, "description": "Not Found"},
        500: {"model": ErrorModel, "description": "Internal Server Error"}
    }
)

# Dependencies
async def get_current_user() -> Dict[str, Any]:
    """Get current authenticated user.
    
    Returns:
        Dict[str, Any]: User information
        
    Raises:
        HTTPException: If user is not authenticated
    """
    # Implement authentication logic here
    raise HTTPException(status_code=401, detail="Not authenticated")

# Endpoints
@router.get("/items/{item_id}", response_model=ResponseModel)
async def get_item(
    item_id: int = Path(..., description="The ID of the item to get"),
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> ResponseModel:
    """Get an item by ID.
    
    Args:
        item_id: The ID of the item to get
        current_user: The current authenticated user
        
    Returns:
        ResponseModel: The requested item
        
    Raises:
        HTTPException: If item is not found
    """
    # Implement get item logic here
    return ResponseModel(
        status="success",
        data={"item_id": item_id},
        message="Item retrieved successfully"
    )

@router.post("/items", response_model=ResponseModel)
async def create_item(
    item: RequestModel,
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> ResponseModel:
    """Create a new item.
    
    Args:
        item: The item data
        current_user: The current authenticated user
        
    Returns:
        ResponseModel: The created item
        
    Raises:
        HTTPException: If item creation fails
    """
    # Implement create item logic here
    return ResponseModel(
        status="success",
        data={"item": item.dict()},
        message="Item created successfully"
    )

@router.put("/items/{item_id}", response_model=ResponseModel)
async def update_item(
    item_id: int = Path(..., description="The ID of the item to update"),
    item: RequestModel = None,
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> ResponseModel:
    """Update an item.
    
    Args:
        item_id: The ID of the item to update
        item: The updated item data
        current_user: The current authenticated user
        
    Returns:
        ResponseModel: The updated item
        
    Raises:
        HTTPException: If item update fails
    """
    # Implement update item logic here
    return ResponseModel(
        status="success",
        data={"item_id": item_id, "item": item.dict() if item else None},
        message="Item updated successfully"
    )

@router.delete("/items/{item_id}", response_model=ResponseModel)
async def delete_item(
    item_id: int = Path(..., description="The ID of the item to delete"),
    current_user: Dict[str, Any] = Depends(get_current_user)
) -> ResponseModel:
    """Delete an item.
    
    Args:
        item_id: The ID of the item to delete
        current_user: The current authenticated user
        
    Returns:
        ResponseModel: Confirmation of deletion
        
    Raises:
        HTTPException: If item deletion fails
    """
    # Implement delete item logic here
    return ResponseModel(
        status="success",
        data={"item_id": item_id},
        message="Item deleted successfully"
    ) 