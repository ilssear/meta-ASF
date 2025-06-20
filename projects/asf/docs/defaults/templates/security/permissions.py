# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Permissions template for the SpecFirst Development Framework.

This template provides a standard implementation for role-based access control
(RBAC) and permission management.
"""

from typing import List, Dict, Set, Optional


class PermissionManager:
    """
    Manages roles, permissions, and user access control.
    
    This class provides methods for defining roles, assigning permissions,
    and checking user access rights.
    """
    
    def __init__(self, roles: Optional[Dict[str, List[str]]] = None):
        """
        Initialize the PermissionManager.
        
        Args:
            roles: A dictionary defining roles and their associated permissions.
                   Example: {'admin': ['read', 'write', 'delete'], 'user': ['read']}
        """
        if roles is None:
            self.roles: Dict[str, Set[str]] = {
                'admin': {'read', 'write', 'delete', 'manage_users'},
                'user': {'read', 'write'},
                'guest': {'read'}
            }
        else:
            self.roles = {role: set(perms) for role, perms in roles.items()}
    
    def add_role(self, role: str, permissions: List[str]):
        """
        Add a new role with a set of permissions.
        
        Args:
            role: The name of the role to add.
            permissions: A list of permissions for the role.
        """
        if role in self.roles:
            raise ValueError(f"Role '{role}' already exists.")
        self.roles[role] = set(permissions)
    
    def remove_role(self, role: str):
        """
        Remove an existing role.
        
        Args:
            role: The name of the role to remove.
        """
        if role not in self.roles:
            raise ValueError(f"Role '{role}' not found.")
        del self.roles[role]
    
    def grant_permission(self, role: str, permission: str):
        """
        Grant a permission to a role.
        
        Args:
            role: The role to grant the permission to.
            permission: The permission to grant.
        """
        if role not in self.roles:
            raise ValueError(f"Role '{role}' not found.")
        self.roles[role].add(permission)
    
    def revoke_permission(self, role: str, permission: str):
        """
        Revoke a permission from a role.
        
        Args:
            role: The role to revoke the permission from.
            permission: The permission to revoke.
        """
        if role not in self.roles:
            raise ValueError(f"Role '{role}' not found.")
        self.roles[role].discard(permission)
    
    def has_permission(self, user_roles: List[str], required_permission: str) -> bool:
        """
        Check if a user has a required permission.
        
        Args:
            user_roles: A list of roles assigned to the user.
            required_permission: The permission required for the action.
            
        Returns:
            True if the user has the permission, False otherwise.
        """
        for role in user_roles:
            if role in self.roles and required_permission in self.roles[role]:
                return True
        return False
    
    def get_role_permissions(self, role: str) -> Optional[Set[str]]:
        """
        Get all permissions for a given role.
        
        Args:
            role: The role to get permissions for.
            
        Returns:
            A set of permissions for the role, or None if the role does not exist.
        """
        return self.roles.get(role)

    def list_roles(self) -> List[str]:
        """
        List all available roles.
        
        Returns:
            A list of all defined roles.
        """
        return list(self.roles.keys())


# Example User class
class User:
    """
    Example User class for demonstrating permission management.
    """
    def __init__(self, username: str, roles: List[str]):
        self.username = username
        self.roles = roles


# Example usage
if __name__ == "__main__":
    # Initialize permission manager
    permission_manager = PermissionManager()
    
    # Create example users
    admin_user = User(username="admin", roles=["admin"])
    regular_user = User(username="user", roles=["user"])
    guest_user = User(username="guest", roles=["guest"])
    
    # Check permissions
    print(f"Admin can 'delete': {permission_manager.has_permission(admin_user.roles, 'delete')}")
    print(f"User can 'delete': {permission_manager.has_permission(regular_user.roles, 'delete')}")
    print(f"User can 'write': {permission_manager.has_permission(regular_user.roles, 'write')}")
    print(f"Guest can 'read': {permission_manager.has_permission(guest_user.roles, 'read')}")
    
    # Add a new role
    permission_manager.add_role("editor", ["read", "write", "edit_content"])
    editor_user = User(username="editor", roles=["editor"])
    
    print(f"\nEditor can 'edit_content': {permission_manager.has_permission(editor_user.roles, 'edit_content')}")
    print(f"Editor can 'delete': {permission_manager.has_permission(editor_user.roles, 'delete')}")
    
    # Grant permission to a role
    permission_manager.grant_permission("editor", "publish_content")
    print(f"Editor can now 'publish_content': {permission_manager.has_permission(editor_user.roles, 'publish_content')}")
    
    # Revoke permission from a role
    permission_manager.revoke_permission("editor", "write")
    print(f"Editor can still 'write': {permission_manager.has_permission(editor_user.roles, 'write')}")
    
    # List all roles
    print(f"\nAvailable roles: {permission_manager.list_roles()}")


# Decorator for checking permissions in a web framework (e.g., Flask, FastAPI)
def permission_required(permission: str):
    """
    Decorator to protect endpoints with permission checks.
    
    This decorator checks if the current user has the required permission
    before allowing access to an endpoint.
    
    Args:
        permission: The permission required for the endpoint.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # In a real application, you would get the user from the request context
            # For this example, we'll assume the user is passed as a keyword argument
            user = kwargs.get("current_user")
            
            if not user:
                raise PermissionError("Authentication required")
            
            # Initialize permission manager
            permission_manager = PermissionManager()
            
            if not permission_manager.has_permission(user.roles, permission):
                raise PermissionError("Insufficient permissions")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example of using the decorator
@permission_required("delete")
def delete_resource(resource_id: int, current_user: User):
    """
    Example function that requires 'delete' permission.
    
    Args:
        resource_id: The ID of the resource to delete.
        current_user: The user performing the action.
    """
    print(f"User '{current_user.username}' is deleting resource {resource_id}")

# Example of calling the decorated function
if __name__ == "__main__":
    print("\n--- Decorator Example ---")
    
    try:
        delete_resource(123, current_user=admin_user)
    except PermissionError as e:
        print(e)
    
    try:
        delete_resource(456, current_user=regular_user)
    except PermissionError as e:
        print(e) 