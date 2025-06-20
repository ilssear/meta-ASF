# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Test case template for the SpecFirst Development Framework.

This template demonstrates the standard structure and formatting for test cases
in the framework, including proper test organization, mocking, and assertions.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, Any, Optional
import json
import tempfile
import os

# Import the module being tested
from your_module import function_to_test, ClassToTest


class TestFunctionToTest:
    """
    Test suite for function_to_test.
    
    This test suite demonstrates various testing patterns including
    success cases, error cases, edge cases, and mocking.
    """
    
    def setup_method(self):
        """Setup method called before each test."""
        self.test_data = {
            'id': 1,
            'name': 'Test Item',
            'description': 'A test item for testing',
            'active': True
        }
    
    def teardown_method(self):
        """Teardown method called after each test."""
        # Clean up any test data or resources
        pass
    
    def test_function_success_case(self):
        """
        Test successful execution of function_to_test.
        
        This test verifies that the function returns the expected
        result when given valid input data.
        """
        # Arrange
        input_data = "valid_input"
        expected_result = "expected_output"
        
        # Act
        result = function_to_test(input_data)
        
        # Assert
        assert result == expected_result
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_function_with_none_input(self):
        """
        Test function behavior with None input.
        
        This test verifies that the function handles None input
        appropriately, either by raising an exception or returning
        a default value.
        """
        # Arrange
        input_data = None
        
        # Act & Assert
        with pytest.raises(ValueError, match="Input cannot be None"):
            function_to_test(input_data)
    
    def test_function_with_empty_string(self):
        """
        Test function behavior with empty string input.
        
        This test verifies that the function handles empty string
        input appropriately.
        """
        # Arrange
        input_data = ""
        expected_result = ""
        
        # Act
        result = function_to_test(input_data)
        
        # Assert
        assert result == expected_result
    
    def test_function_with_special_characters(self):
        """
        Test function behavior with special characters.
        
        This test verifies that the function handles special
        characters correctly.
        """
        # Arrange
        input_data = "test@#$%^&*()_+"
        expected_result = "processed_special_chars"
        
        # Act
        result = function_to_test(input_data)
        
        # Assert
        assert result == expected_result
    
    @pytest.mark.parametrize("input_data,expected", [
        ("hello", "HELLO"),
        ("world", "WORLD"),
        ("test", "TEST"),
        ("", ""),
        ("123", "123"),
    ])
    def test_function_with_various_inputs(self, input_data: str, expected: str):
        """
        Test function with various input values.
        
        This parameterized test verifies that the function
        behaves correctly with different input types.
        """
        # Act
        result = function_to_test(input_data)
        
        # Assert
        assert result == expected


class TestClassToTest:
    """
    Test suite for ClassToTest.
    
    This test suite demonstrates testing class methods, object
    state changes, and constructor behavior.
    """
    
    def setup_method(self):
        """Setup method called before each test."""
        self.test_instance = ClassToTest()
        self.test_data = {
            'id': 1,
            'name': 'Test Object',
            'value': 42
        }
    
    def test_constructor_default_values(self):
        """
        Test constructor with default values.
        
        This test verifies that the constructor initializes
        the object with correct default values.
        """
        # Act
        instance = ClassToTest()
        
        # Assert
        assert instance.name == "default"
        assert instance.value == 0
        assert instance.active is False
    
    def test_constructor_with_parameters(self):
        """
        Test constructor with custom parameters.
        
        This test verifies that the constructor accepts and
        sets custom parameter values correctly.
        """
        # Arrange
        name = "Custom Name"
        value = 100
        active = True
        
        # Act
        instance = ClassToTest(name=name, value=value, active=active)
        
        # Assert
        assert instance.name == name
        assert instance.value == value
        assert instance.active == active
    
    def test_method_success_case(self):
        """
        Test successful execution of a class method.
        
        This test verifies that the method performs its
        intended operation correctly.
        """
        # Arrange
        input_data = "test_input"
        expected_result = "processed_test_input"
        
        # Act
        result = self.test_instance.process_data(input_data)
        
        # Assert
        assert result == expected_result
        assert self.test_instance.last_processed == input_data
    
    def test_method_updates_object_state(self):
        """
        Test that method updates object state correctly.
        
        This test verifies that the method properly updates
        the object's internal state.
        """
        # Arrange
        initial_value = self.test_instance.value
        increment = 5
        
        # Act
        self.test_instance.increment_value(increment)
        
        # Assert
        assert self.test_instance.value == initial_value + increment
    
    def test_method_with_invalid_input(self):
        """
        Test method behavior with invalid input.
        
        This test verifies that the method handles invalid
        input appropriately.
        """
        # Arrange
        invalid_input = -1
        
        # Act & Assert
        with pytest.raises(ValueError, match="Value must be positive"):
            self.test_instance.process_positive_value(invalid_input)


class TestWithMocking:
    """
    Test suite demonstrating mocking patterns.
    
    This test suite shows how to use mocking to isolate
    the unit under test from external dependencies.
    """
    
    @patch('your_module.external_api_call')
    def test_function_with_mocked_api(self, mock_api):
        """
        Test function that uses external API.
        
        This test demonstrates how to mock external API calls
        to test the function in isolation.
        """
        # Arrange
        mock_api.return_value = {'status': 'success', 'data': 'test_data'}
        input_data = "api_input"
        expected_result = "processed_api_data"
        
        # Act
        result = function_using_api(input_data)
        
        # Assert
        assert result == expected_result
        mock_api.assert_called_once_with(input_data)
    
    @patch('your_module.database_connection')
    def test_function_with_mocked_database(self, mock_db):
        """
        Test function that uses database.
        
        This test demonstrates how to mock database operations
        to test the function without requiring a real database.
        """
        # Arrange
        mock_db.query.return_value.filter.return_value.first.return_value = None
        input_data = "db_input"
        expected_result = "no_data_found"
        
        # Act
        result = function_using_database(input_data)
        
        # Assert
        assert result == expected_result
        mock_db.query.assert_called_once()
    
    def test_function_with_mock_object(self):
        """
        Test function with mock object.
        
        This test demonstrates how to create and use mock
        objects for testing.
        """
        # Arrange
        mock_service = Mock()
        mock_service.process.return_value = "mocked_result"
        input_data = "test_input"
        
        # Act
        result = function_using_service(input_data, mock_service)
        
        # Assert
        assert result == "mocked_result"
        mock_service.process.assert_called_once_with(input_data)


class TestWithFixtures:
    """
    Test suite demonstrating fixture usage.
    
    This test suite shows how to use pytest fixtures
    for test data and setup.
    """
    
    def test_with_data_fixture(self, sample_data):
        """
        Test using data fixture.
        
        This test demonstrates how to use a fixture to
        provide test data.
        """
        # Arrange
        expected_name = "Test User"
        
        # Act
        result = process_user_data(sample_data)
        
        # Assert
        assert result['name'] == expected_name
        assert result['processed'] is True
    
    def test_with_mock_fixture(self, mock_external_service):
        """
        Test using mock fixture.
        
        This test demonstrates how to use a fixture to
        provide a mock object.
        """
        # Arrange
        mock_external_service.get_data.return_value = "fixture_data"
        input_data = "test_input"
        
        # Act
        result = function_using_external_service(input_data, mock_external_service)
        
        # Assert
        assert result == "fixture_data"
        mock_external_service.get_data.assert_called_once()


# Fixtures for use in tests
@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        'id': 1,
        'name': 'Test User',
        'email': 'test@example.com',
        'active': True
    }


@pytest.fixture
def mock_external_service():
    """Provide a mock external service for tests."""
    mock_service = Mock()
    mock_service.get_data.return_value = "default_data"
    return mock_service


@pytest.fixture
def temp_file():
    """Provide a temporary file for tests."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('{"test": "data"}')
        temp_file_path = f.name
    
    yield temp_file_path
    
    # Cleanup
    os.unlink(temp_file_path)


# Helper functions for testing
def create_test_data() -> Dict[str, Any]:
    """Create test data for use in tests."""
    return {
        'id': 1,
        'name': 'Test Item',
        'description': 'A test item',
        'value': 42,
        'active': True
    }


def assert_dict_contains(dict_obj: Dict[str, Any], expected_items: Dict[str, Any]):
    """
    Assert that a dictionary contains expected items.
    
    Args:
        dict_obj: The dictionary to check
        expected_items: The items that should be present
    """
    for key, value in expected_items.items():
        assert key in dict_obj, f"Key '{key}' not found in dictionary"
        assert dict_obj[key] == value, f"Value for key '{key}' does not match"


def assert_list_contains(list_obj: list, expected_item: Any):
    """
    Assert that a list contains an expected item.
    
    Args:
        list_obj: The list to check
        expected_item: The item that should be present
    """
    assert expected_item in list_obj, f"Item {expected_item} not found in list"


# Example test functions that would be implemented in the actual module
def function_to_test(input_data: str) -> str:
    """Example function to test."""
    if input_data is None:
        raise ValueError("Input cannot be None")
    return input_data.upper()


def function_using_api(input_data: str) -> str:
    """Example function that uses external API."""
    # This would normally call an external API
    return "processed_api_data"


def function_using_database(input_data: str) -> str:
    """Example function that uses database."""
    # This would normally query a database
    return "no_data_found"


def function_using_service(input_data: str, service) -> str:
    """Example function that uses a service."""
    return service.process(input_data)


def function_using_external_service(input_data: str, service) -> str:
    """Example function that uses external service."""
    return service.get_data()


def process_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Example function that processes user data."""
    result = data.copy()
    result['processed'] = True
    return result


class ClassToTest:
    """Example class to test."""
    
    def __init__(self, name: str = "default", value: int = 0, active: bool = False):
        self.name = name
        self.value = value
        self.active = active
        self.last_processed = None
    
    def process_data(self, data: str) -> str:
        """Process input data."""
        self.last_processed = data
        return f"processed_{data}"
    
    def increment_value(self, increment: int) -> None:
        """Increment the value by the given amount."""
        self.value += increment
    
    def process_positive_value(self, value: int) -> int:
        """Process a positive value."""
        if value <= 0:
            raise ValueError("Value must be positive")
        return value * 2