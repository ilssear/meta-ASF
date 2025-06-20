# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Example code file template for the SpecFirst Development Framework.

This template demonstrates the standard structure and formatting for Python
code files in the framework, including copyright headers, docstrings, and
proper code organization.
"""

import os
import sys
from typing import Dict, List, Optional, Any
from pathlib import Path

# Standard library imports first
import json
import logging

# Third-party imports
import requests
from pydantic import BaseModel

# Local imports
from .config import Config
from .utils import helper_function


class ExampleClass(BaseModel):
    """
    Example class demonstrating proper structure and documentation.
    
    This class shows how to implement a Pydantic model with proper
    type hints, docstrings, and validation.
    """
    
    name: str
    description: Optional[str] = None
    metadata: Dict[str, Any] = {}
    
    class Config:
        """Pydantic configuration for the model."""
        extra = "forbid"
        validate_assignment = True
    
    def __init__(self, **data):
        """Initialize the example class with validation."""
        super().__init__(**data)
        self._validate_data()
    
    def _validate_data(self) -> None:
        """
        Validate the class data.
        
        Raises:
            ValueError: If validation fails.
        """
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the class instance to a dictionary.
        
        Returns:
            Dictionary representation of the class.
        """
        return self.dict()
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ExampleClass":
        """
        Create an instance from a dictionary.
        
        Args:
            data: Dictionary containing class data.
            
        Returns:
            New instance of ExampleClass.
        """
        return cls(**data)


def example_function(param1: str, param2: Optional[int] = None) -> str:
    """
    Example function demonstrating proper function documentation.
    
    This function shows how to write clear, well-documented functions
    with proper type hints, docstrings, and error handling.
    
    Args:
        param1: Required string parameter.
        param2: Optional integer parameter.
        
    Returns:
        String result of the function operation.
        
    Raises:
        ValueError: If param1 is empty or param2 is negative.
        
    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        "test_42"
    """
    # Input validation
    if not param1.strip():
        raise ValueError("param1 cannot be empty")
    
    if param2 is not None and param2 < 0:
        raise ValueError("param2 cannot be negative")
    
    # Function logic
    result = param1
    if param2 is not None:
        result = f"{param1}_{param2}"
    
    return result


class ExampleManager:
    """
    Example manager class for handling complex operations.
    
    This class demonstrates how to implement a manager class that
    handles multiple operations and maintains state.
    """
    
    def __init__(self, config: Config):
        """
        Initialize the example manager.
        
        Args:
            config: Configuration object for the manager.
        """
        self.config = config
        self.logger = logging.getLogger(__name__)
        self._items: List[ExampleClass] = []
    
    def add_item(self, item: ExampleClass) -> None:
        """
        Add an item to the manager.
        
        Args:
            item: Item to add to the manager.
        """
        self._items.append(item)
        self.logger.info(f"Added item: {item.name}")
    
    def get_item(self, name: str) -> Optional[ExampleClass]:
        """
        Get an item by name.
        
        Args:
            name: Name of the item to retrieve.
            
        Returns:
            Item if found, None otherwise.
        """
        for item in self._items:
            if item.name == name:
                return item
        return None
    
    def list_items(self) -> List[ExampleClass]:
        """
        Get all items in the manager.
        
        Returns:
            List of all items.
        """
        return self._items.copy()
    
    def save_to_file(self, filename: str) -> None:
        """
        Save items to a JSON file.
        
        Args:
            filename: Name of the file to save to.
            
        Raises:
            IOError: If file cannot be written.
        """
        try:
            data = [item.to_dict() for item in self._items]
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            self.logger.info(f"Saved {len(self._items)} items to {filename}")
        except IOError as e:
            self.logger.error(f"Failed to save to {filename}: {e}")
            raise


def main() -> None:
    """
    Main function demonstrating the usage of the example classes.
    
    This function shows how to use the example classes and functions
    in a complete, working example.
    """
    # Setup logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Create configuration
    config = Config()
    
    # Create manager
    manager = ExampleManager(config)
    
    # Create and add items
    item1 = ExampleClass(name="Item 1", description="First item")
    item2 = ExampleClass(name="Item 2", description="Second item")
    
    manager.add_item(item1)
    manager.add_item(item2)
    
    # Demonstrate function usage
    result = example_function("test", 42)
    print(f"Function result: {result}")
    
    # List all items
    items = manager.list_items()
    print(f"Total items: {len(items)}")
    
    # Save to file
    manager.save_to_file("example_output.json")
    
    print("Example completed successfully!")


if __name__ == "__main__":
    main() 