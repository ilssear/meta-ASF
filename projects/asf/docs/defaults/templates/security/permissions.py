# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Permissions template.

from typing import List, Dict, Optional
from enum import Enum

class Permission(Enum):
    """Permission levels for access control."""
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"

class Role:
    """Role definition for access control."""
    
    def __init__(self, name: str, permissions: List[Permission]):
        """Initialize role.
        
        Args:
            name: Role name
            permissions: List of permissions for role
        """
        self.name = name
        self.permissions = permissions

class PermissionManager:
    """Permission manager for handling access control."""
    
    def __init__(self):
        """Initialize permission manager."""
        self.roles: Dict[str, Role] = {}
        self._initialize_default_roles()
    
    def _initialize_default_roles(self):
        """Initialize default roles."""
        self.roles = {
            "user": Role("user", [Permission.READ]),
            "editor": Role("editor", [Permission.READ, Permission.WRITE]),
            "admin": Role("admin", [Permission.READ, Permission.WRITE, Permission.DELETE, Permission.ADMIN])
        }
    
    def get_role(self, role_name: str) -> Optional[Role]:
        """Get role by name.
        
        Args:
            role_name: Name of role to get
            
        Returns:
            Optional[Role]: Role if found, None otherwise
        """
        return self.roles.get(role_name)
    
    def has_permission(self, role_name: str, permission: Permission) -> bool:
        """Check if role has permission.
        
        Args:
            role_name: Name of role to check
            permission: Permission to check for
            
        Returns:
            bool: True if role has permission
        """
        role = self.get_role(role_name)
        if not role:
            return False
        return permission in role.permissions
    
    def add_role(self, name: str, permissions: List[Permission]) -> None:
        """Add new role.
        
        Args:
            name: Name of role to add
            permissions: List of permissions for role
        """
        self.roles[name] = Role(name, permissions)
    
    def remove_role(self, name: str) -> None:
        """Remove role.
        
        Args:
            name: Name of role to remove
        """
        self.roles.pop(name, None) 