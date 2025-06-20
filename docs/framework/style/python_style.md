# Python Style Guide - Agile SpecFirst Framework

## 🎯 Core Principles

### 1. Readability First
- Code should be easy to read and understand
- Use clear, descriptive names
- Follow consistent formatting

### 2. Type Safety
- Use type hints consistently
- Validate inputs and outputs
- Handle edge cases explicitly

### 3. Documentation
- Document all public interfaces
- Include examples in docstrings
- Keep documentation up to date

## 💻 Code Standards

### 1. File Structure
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Module description.

This module provides functionality for [purpose].
"""

from typing import List, Optional, Dict
import logging
from datetime import datetime

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Type aliases
UserId = str
UserData = Dict[str, str]

# Logging setup
logger = logging.getLogger(__name__)

# Classes
class ExampleClass:
    """
    Class description.
    """

    def __init__(self, param: str) -> None:
        """
        Initialize the class.

        Args:
            param: Parameter description.
        """
        self.param = param

# Functions
def example_function(param: str) -> Optional[List[str]]:
    """
    Function description.

    Args:
        param: Parameter description.

    Returns:
        Optional[List[str]]: Return value description.

    Raises:
        ValueError: Error description.
    """
    # Implementation
    pass
```

### 2. Naming Conventions
- **Classes**: CamelCase
- **Functions/Methods**: snake_case
- **Variables**: snake_case
- **Constants**: UPPER_SNAKE_CASE
- **Private Members**: _prefix
- **Type Aliases**: PascalCase

### 3. Type Hints
```python
from typing import (
    List,
    Dict,
    Optional,
    Union,
    Tuple,
    Callable,
    TypeVar,
    Generic
)

# Basic types
def process_data(data: List[str]) -> Dict[str, int]:
    pass

# Optional types
def get_user(user_id: Optional[str] = None) -> Optional[Dict[str, str]]:
    pass

# Union types
def handle_value(value: Union[str, int, float]) -> str:
    pass

# Generic types
T = TypeVar('T')
class Container(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value = value
```

### 4. Docstrings
```python
def process_data(
    data: List[str],
    max_items: Optional[int] = None
) -> Dict[str, int]:
    """
    Process a list of data items.

    This function takes a list of strings and processes them according to
    the specified rules. It returns a dictionary mapping each unique item
    to its count.

    Args:
        data: List of strings to process.
        max_items: Maximum number of items to process. If None, process all.

    Returns:
        Dict[str, int]: Dictionary mapping items to their counts.

    Raises:
        ValueError: If data is empty or max_items is negative.
        TypeError: If data contains non-string items.

    Examples:
        >>> process_data(['a', 'b', 'a'])
        {'a': 2, 'b': 1}
        >>> process_data(['a', 'b'], max_items=1)
        {'a': 1}
    """
    pass
```

## 🛠️ Best Practices

### 1. Error Handling
```python
def safe_operation() -> Optional[str]:
    """
    Perform a safe operation with proper error handling.
    """
    try:
        result = perform_operation()
        return result
    except ValueError as e:
        logger.error("Invalid input: %s", e)
        return None
    except Exception as e:
        logger.exception("Unexpected error: %s", e)
        raise
```

### 2. Logging
```python
import logging

logger = logging.getLogger(__name__)

def process_item(item: str) -> None:
    """
    Process an item with proper logging.
    """
    logger.debug("Processing item: %s", item)
    try:
        result = perform_operation(item)
        logger.info("Successfully processed item: %s", item)
    except Exception as e:
        logger.error("Failed to process item %s: %s", item, e)
        raise
```

### 3. Testing
```python
import pytest
from typing import List

def test_process_data():
    """
    Test the process_data function.
    """
    # Arrange
    input_data = ["a", "b", "a"]
    expected = {"a": 2, "b": 1}

    # Act
    result = process_data(input_data)

    # Assert
    assert result == expected

def test_process_data_empty():
    """
    Test process_data with empty input.
    """
    with pytest.raises(ValueError):
        process_data([])
```

## ✅ Code Quality

### 1. Code Organization
- One class per file
- Related functions grouped together
- Clear separation of concerns
- Logical file structure

### 2. Function Design
- Single responsibility
- Clear input/output
- Proper error handling
- Comprehensive documentation

### 3. Class Design
- Clear purpose
- Encapsulated data
- Well-defined interface
- Proper inheritance

## ❌ Common Pitfalls

### 1. Style Issues
- ❌ Inconsistent naming
- ❌ Missing type hints
- ❌ Poor formatting
- ❌ Incomplete docstrings

### 2. Design Issues
- ❌ Overly complex functions
- ❌ Poor error handling
- ❌ Insufficient testing
- ❌ Unclear interfaces

### 3. Performance Issues
- ❌ Inefficient algorithms
- ❌ Unnecessary operations
- ❌ Memory leaks
- ❌ Resource management

## 📚 Examples

### 1. Good Code
```python
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
User data processing module.
"""

from typing import Dict, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class UserData:
    """
    User data container with validation.
    """

    def __init__(self, user_id: str, data: Dict[str, str]) -> None:
        """
        Initialize user data.

        Args:
            user_id: Unique user identifier.
            data: User data dictionary.

        Raises:
            ValueError: If user_id is empty or data is invalid.
        """
        if not user_id:
            raise ValueError("user_id cannot be empty")
        self.user_id = user_id
        self.data = data
        self.timestamp = datetime.now()

    def to_dict(self) -> Dict[str, str]:
        """
        Convert to dictionary.

        Returns:
            Dict[str, str]: User data dictionary.
        """
        return {
            "user_id": self.user_id,
            "data": self.data,
            "timestamp": self.timestamp.isoformat()
        }
```

### 2. Poor Code
```python
class user:
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.time = datetime.now()

    def get_dict(self):
        return {"id": self.id, "data": self.data, "time": self.time}
```

## Version History

### v1.0.0 (2025-01-15)
- Initial style guide
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