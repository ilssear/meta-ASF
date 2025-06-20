# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Test case template.

import pytest
from typing import Dict, List, Optional

def test_function_with_valid_input(sample_data: Dict):
    """Test function with valid input data.
    
    Args:
        sample_data: Sample data fixture
    """
    # Arrange
    input_data = sample_data
    
    # Act
    result = process_data(input_data)
    
    # Assert
    assert result is not None
    assert result['id'] == input_data['id']
    assert result['name'] == input_data['name']

def test_function_with_invalid_input():
    """Test function with invalid input data."""
    # Arrange
    invalid_data = {'id': 'invalid'}
    
    # Act & Assert
    with pytest.raises(ValueError):
        process_data(invalid_data)

def test_function_with_empty_input():
    """Test function with empty input data."""
    # Arrange
    empty_data = {}
    
    # Act & Assert
    with pytest.raises(ValueError):
        process_data(empty_data)

def test_function_with_none_input():
    """Test function with None input."""
    # Arrange
    none_data = None
    
    # Act & Assert
    with pytest.raises(TypeError):
        process_data(none_data) 