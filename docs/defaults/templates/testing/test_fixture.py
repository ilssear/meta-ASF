# Copyright (c) {{YEAR}} {{AUTHOR}}
# All rights reserved.
#
# This file is part of {{PROJECT}}.
# Version: {{VERSION}}
#
# Test fixture template for test data and setup.

import pytest
from typing import Any, Dict, Generator, Optional
import logging
import json
from pathlib import Path

@pytest.fixture
def test_data() -> Dict[str, Any]:
    """Provide test data for tests.
    
    Returns:
        Dictionary containing test data
    """
    return {
        "user": {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com"
        },
        "config": {
            "timeout": 30,
            "retries": 3
        }
    }

@pytest.fixture
def test_file(tmp_path: Path) -> Generator[Path, None, None]:
    """Create a temporary test file.
    
    Args:
        tmp_path: pytest fixture providing temporary directory
    
    Yields:
        Path to temporary test file
    """
    test_file = tmp_path / "test.json"
    test_data = {"test": "data"}
    
    with open(test_file, "w") as f:
        json.dump(test_data, f)
    
    yield test_file
    
    # Cleanup
    test_file.unlink()

@pytest.fixture
def logger() -> logging.Logger:
    """Provide a configured logger.
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)
    
    # Add console handler
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

@pytest.fixture
def mock_database() -> Generator[Dict[str, Any], None, None]:
    """Provide a mock database connection.
    
    Yields:
        Dictionary simulating database connection
    """
    # Setup
    db = {
        "connected": True,
        "tables": {},
        "transactions": []
    }
    
    yield db
    
    # Cleanup
    db["connected"] = False
    db["tables"].clear()
    db["transactions"].clear()

@pytest.fixture
def test_config() -> Dict[str, Any]:
    """Provide test configuration.
    
    Returns:
        Dictionary containing test configuration
    """
    return {
        "database": {
            "host": "localhost",
            "port": 5432,
            "name": "test_db"
        },
        "api": {
            "base_url": "http://localhost:8000",
            "timeout": 30
        },
        "logging": {
            "level": "DEBUG",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        }
    } 