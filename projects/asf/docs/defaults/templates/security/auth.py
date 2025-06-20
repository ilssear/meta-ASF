# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Authentication template for the SpecFirst Development Framework.

This template provides a standard implementation for user authentication,
including token generation, password hashing, and user verification.
"""

import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import Dict, Any, Optional

# Configuration for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuration for JWT
SECRET_KEY = "YOUR_SECRET_KEY"  # Replace with a strong, secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class AuthHandler:
    """
    Handles all authentication-related tasks.
    
    This class provides methods for password hashing, token generation,
    and user verification.
    """
    
    def get_password_hash(self, password: str) -> str:
        """
        Hash a password using bcrypt.
        
        Args:
            password: The password to hash.
            
        Returns:
            The hashed password.
        """
        return pwd_context.hash(password)
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against a hashed password.
        
        Args:
            plain_password: The plain password to verify.
            hashed_password: The hashed password to compare against.
            
        Returns:
            True if the password is correct, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)
    
    def create_access_token(self, data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
        """
        Create a new access token.
        
        Args:
            data: The data to encode in the token.
            expires_delta: The expiration time for the token.
            
        Returns:
            The encoded access token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def decode_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Decode an access token.
        
        Args:
            token: The token to decode.
            
        Returns:
            The decoded token payload, or None if invalid.
        """
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token has expired
        except jwt.InvalidTokenError:
            return None  # Invalid token
    
    def get_user_from_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Get user information from a token.
        
        Args:
            token: The access token.
            
        Returns:
            The user information, or None if the token is invalid.
        """
        payload = self.decode_token(token)
        if payload:
            # You would typically query your database here to get the user
            # For this example, we'll just return the payload
            return payload
        return None


# Example usage
if __name__ == "__main__":
    auth_handler = AuthHandler()
    
    # Password hashing and verification
    password = "mysecretpassword"
    hashed_password = auth_handler.get_password_hash(password)
    
    print(f"Password: {password}")
    print(f"Hashed Password: {hashed_password}")
    
    is_correct = auth_handler.verify_password(password, hashed_password)
    print(f"Password is correct: {is_correct}")
    
    is_incorrect = auth_handler.verify_password("wrongpassword", hashed_password)
    print(f"Password is correct (with wrong password): {is_incorrect}")
    
    # Token generation and decoding
    user_data = {"sub": "user@example.com", "role": "admin"}
    access_token = auth_handler.create_access_token(data=user_data)
    
    print(f"\nAccess Token: {access_token}")
    
    decoded_payload = auth_handler.decode_token(access_token)
    print(f"Decoded Payload: {decoded_payload}")
    
    user_from_token = auth_handler.get_user_from_token(access_token)
    print(f"User from Token: {user_from_token}")
    
    # Example of an expired token
    expired_token = auth_handler.create_access_token(
        data=user_data, expires_delta=timedelta(seconds=-1)
    )
    
    decoded_expired = auth_handler.decode_token(expired_token)
    print(f"\nDecoded Expired Token: {decoded_expired}")
    
    # Example of an invalid token
    invalid_token = "this.is.an.invalid.token"
    decoded_invalid = auth_handler.decode_token(invalid_token)
    print(f"Decoded Invalid Token: {decoded_invalid}")
		
# Helper functions for use in other modules
def get_current_user(token: str) -> Optional[Dict[str, Any]]:
    """
    Get the current user from a token.
    
    This function would typically be used in an API endpoint
    to authenticate and authorize a user.
    
    Args:
        token: The access token.
        
    Returns:
        The current user, or None if invalid.
    """
    auth_handler = AuthHandler()
    return auth_handler.get_user_from_token(token)

def requires_auth(role: str):
    """
    Decorator to protect API endpoints.
    
    This decorator checks for a valid token and user role
    before allowing access to an endpoint.
    
    Args:
        role: The required role for the endpoint.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # In a real application, you would get the token from the request header
            token = kwargs.get("token")
            
            if not token:
                raise PermissionError("Authentication required")
            
            user = get_current_user(token)
            
            if not user or role not in user.get("roles", []):
                raise PermissionError("Insufficient permissions")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator 