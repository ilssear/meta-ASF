# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Authentication template.

from typing import Dict, Optional
from datetime import datetime, timedelta
import jwt
from passlib.context import CryptContext

class AuthManager:
    """Authentication manager for handling user authentication."""
    
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        """Initialize authentication manager.
        
        Args:
            secret_key: Secret key for JWT token generation
            algorithm: Algorithm to use for JWT token generation
        """
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash.
        
        Args:
            plain_password: Plain text password
            hashed_password: Hashed password
            
        Returns:
            bool: True if password matches hash
        """
        return self.pwd_context.verify(plain_password, hashed_password)
    
    def get_password_hash(self, password: str) -> str:
        """Generate password hash.
        
        Args:
            password: Plain text password
            
        Returns:
            str: Hashed password
        """
        return self.pwd_context.hash(password)
    
    def create_access_token(self, data: Dict, expires_delta: Optional[timedelta] = None) -> str:
        """Create JWT access token.
        
        Args:
            data: Data to encode in token
            expires_delta: Token expiration time
            
        Returns:
            str: JWT access token
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    
    def verify_token(self, token: str) -> Dict:
        """Verify JWT token.
        
        Args:
            token: JWT token to verify
            
        Returns:
            Dict: Decoded token data
            
        Raises:
            jwt.InvalidTokenError: If token is invalid
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.InvalidTokenError:
            raise 