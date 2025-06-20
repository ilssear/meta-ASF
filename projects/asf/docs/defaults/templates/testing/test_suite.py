# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# Test suite template.

import pytest
from typing import Dict, List, Optional

class TestDataProcessor:
    """Test suite for DataProcessor class."""
    
    @pytest.fixture
    def processor(self):
        """Create a DataProcessor instance."""
        return DataProcessor()
    
    def test_process_valid_data(self, processor, sample_data: Dict):
        """Test processing valid data.
        
        Args:
            processor: DataProcessor instance
            sample_data: Sample data fixture
        """
        # Arrange
        input_data = sample_data
        
        # Act
        result = processor.process(input_data)
        
        # Assert
        assert result is not None
        assert result['id'] == input_data['id']
        assert result['name'] == input_data['name']
    
    def test_process_invalid_data(self, processor):
        """Test processing invalid data.
        
        Args:
            processor: DataProcessor instance
        """
        # Arrange
        invalid_data = {'id': 'invalid'}
        
        # Act & Assert
        with pytest.raises(ValueError):
            processor.process(invalid_data)
    
    def test_process_empty_data(self, processor):
        """Test processing empty data.
        
        Args:
            processor: DataProcessor instance
        """
        # Arrange
        empty_data = {}
        
        # Act & Assert
        with pytest.raises(ValueError):
            processor.process(empty_data)
    
    def test_process_none_data(self, processor):
        """Test processing None data.
        
        Args:
            processor: DataProcessor instance
        """
        # Arrange
        none_data = None
        
        # Act & Assert
        with pytest.raises(TypeError):
            processor.process(none_data) 