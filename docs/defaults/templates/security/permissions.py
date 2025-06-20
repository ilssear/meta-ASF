# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""Template for permissions.

This template provides a standard structure for permissions, including:
- Role-based access control
- Permission checking
- Resource ownership
- Action authorization
"""

from enum import Enum
from typing import Any, Callable, Dict, List, Optional, Set, Union
from fastapi import Depends, HTTPException, status
from pydantic import BaseModel

# Models
class Role(str, Enum):
    """User roles."""
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
    GUEST = "guest"

class Permission(str, Enum):
    """User permissions."""
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    MANAGE = "manage"

class Resource(str, Enum):
    """Resource types."""
    USER = "user"
    ITEM = "item"
    SETTING = "setting"
    REPORT = "report"

class User(BaseModel):
    """User model with roles and permissions."""
    id: int
    username: str
    roles: Set[Role]
    permissions: Set[Permission]

# Role-Permission mappings
ROLE_PERMISSIONS: Dict[Role, Set[Permission]] = {
    Role.ADMIN: {
        Permission.CREATE,
        Permission.READ,
        Permission.UPDATE,
        Permission.DELETE,
        Permission.MANAGE
    },
    Role.MANAGER: {
        Permission.CREATE,
        Permission.READ,
        Permission.UPDATE,
        Permission.MANAGE
    },
    Role.USER: {
        Permission.CREATE,
        Permission.READ,
        Permission.UPDATE
    },
    Role.GUEST: {
        Permission.READ
    }
}

# Resource-Permission mappings
RESOURCE_PERMISSIONS: Dict[Resource, Set[Permission]] = {
    Resource.USER: {
        Permission.CREATE,
        Permission.READ,
        Permission.UPDATE,
        Permission.DELETE,
        Permission.MANAGE
    },
    Resource.ITEM: {
        Permission.CREATE,
        Permission.READ,
        Permission.UPDATE,
        Permission.DELETE
    },
    Resource.SETTING: {
        Permission.READ,
        Permission.UPDATE,
        Permission.MANAGE
    },
    Resource.REPORT: {
        Permission.CREATE,
        Permission.READ,
        Permission.MANAGE
    }
}

# Permission functions
def get_user_permissions(user: User) -> Set[Permission]:
    """Get all permissions for a user.
    
    Args:
        user: User to get permissions for
        
    Returns:
        Set[Permission]: Set of user permissions
    """
    permissions = set()
    for role in user.roles:
        permissions.update(ROLE_PERMISSIONS.get(role, set()))
    permissions.update(user.permissions)
    return permissions

def check_permission(
    user: User,
    resource: Resource,
    permission: Permission
) -> bool:
    """Check if user has permission for resource.
    
    Args:
        user: User to check
        resource: Resource to check
        permission: Permission to check
        
    Returns:
        bool: True if user has permission
    """
    user_permissions = get_user_permissions(user)
    resource_permissions = RESOURCE_PERMISSIONS.get(resource, set())
    return permission in user_permissions and permission in resource_permissions

def require_permission(
    resource: Resource,
    permission: Permission
) -> Callable:
    """Create permission requirement decorator.
    
    Args:
        resource: Resource to check
        permission: Permission to check
        
    Returns:
        Callable: Decorator function
    """
    def decorator(user: User = Depends(get_current_user)) -> User:
        """Check permission requirement.
        
        Args:
            user: Current user
            
        Returns:
            User: Current user if authorized
            
        Raises:
            HTTPException: If user is not authorized
        """
        if not check_permission(user, resource, permission):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return user
    return decorator

# Resource ownership
def check_ownership(
    user: User,
    resource: Resource,
    resource_id: int
) -> bool:
    """Check if user owns resource.
    
    Args:
        user: User to check
        resource: Resource type
        resource_id: Resource ID
        
    Returns:
        bool: True if user owns resource
    """
    # Implement resource ownership check
    return True

def require_ownership(
    resource: Resource
) -> Callable:
    """Create ownership requirement decorator.
    
    Args:
        resource: Resource type
        
    Returns:
        Callable: Decorator function
    """
    def decorator(
        user: User = Depends(get_current_user),
        resource_id: int = Path(...)
    ) -> User:
        """Check ownership requirement.
        
        Args:
            user: Current user
            resource_id: Resource ID
            
        Returns:
            User: Current user if authorized
            
        Raises:
            HTTPException: If user is not authorized
        """
        if not check_ownership(user, resource, resource_id):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Resource not owned by user"
            )
        return user
    return decorator 