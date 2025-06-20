# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Test fixture template.

import pytest
from typing import Dict, List, Optional

@pytest.fixture
def sample_data() -> Dict:
    """Create sample data for testing.
    
    Returns:
        Dictionary containing sample data
    """
    return {
        'id': 1,
        'name': 'Test Item',
        'description': 'Test Description',
        'tags': ['test', 'example']
    }

@pytest.fixture
def sample_list() -> List[Dict]:
    """Create sample list for testing.
    
    Returns:
        List of dictionaries containing sample data
    """
    return [
        {'id': 1, 'name': 'Item 1'},
        {'id': 2, 'name': 'Item 2'},
        {'id': 3, 'name': 'Item 3'}
    ]

@pytest.fixture
def sample_object():
    """Create sample object for testing.
    
    Returns:
        Sample object instance
    """
    class SampleObject:
        def __init__(self, id: int, name: str):
            self.id = id
            self.name = name
    
    return SampleObject(1, 'Test Object') 