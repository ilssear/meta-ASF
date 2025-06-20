# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Test fixture template for the SpecFirst Development Framework.

This template demonstrates how to create and use pytest fixtures for setting up
test data, mock objects, and other resources needed for testing.
"""

import pytest
from unittest.mock import Mock, patch
from typing import Dict, Any, Generator
import json
import tempfile
import os

# Import modules that might be needed for fixtures
from your_module import DatabaseConnection, ApiClient, User, Product


@pytest.fixture(scope="session")
def session_fixture() -> str:
    """
    Example session-scoped fixture.
    
    This fixture is created once per test session and can be
    used to share resources across all tests.
    
    Returns:
        A string indicating the fixture's scope.
    """
    print("Setting up session-scoped fixture...")
    yield "session-data"
    print("Tearing down session-scoped fixture...")


@pytest.fixture(scope="module")
def module_fixture() -> str:
    """
    Example module-scoped fixture.
    
    This fixture is created once per test module.
    
    Returns:
        A string indicating the fixture's scope.
    """
    print("Setting up module-scoped fixture...")
    yield "module-data"
    print("Tearing down module-scoped fixture...")


@pytest.fixture
def sample_user_data() -> Dict[str, Any]:
    """
    Provide sample user data for tests.
    
    This fixture provides a consistent set of user data
    that can be used in multiple tests.
    
    Returns:
        Dictionary containing sample user data.
    """
    return {
        'id': 1,
        'name': 'Test User',
        'email': 'test@example.com',
        'is_active': True,
        'roles': ['user', 'viewer']
    }


@pytest.fixture
def sample_product_data() -> Dict[str, Any]:
    """
    Provide sample product data for tests.
    
    This fixture provides a consistent set of product data
    for use in e-commerce related tests.
    
    Returns:
        Dictionary containing sample product data.
    """
    return {
        'id': 101,
        'name': 'Test Product',
        'price': 99.99,
        'category': 'electronics',
        'in_stock': True
    }


@pytest.fixture
def user_instance(sample_user_data: Dict[str, Any]) -> User:
    """
    Create a User instance from sample data.
    
    This fixture demonstrates how to create model instances
    from data fixtures for testing.
    
    Args:
        sample_user_data: Fixture providing user data.
        
    Returns:
        Instance of the User class.
    """
    return User(**sample_user_data)


@pytest.fixture
def product_instance(sample_product_data: Dict[str, Any]) -> Product:
    """
    Create a Product instance from sample data.
    
    This fixture shows how to create model instances
    for different data types.
    
    Args:
        sample_product_data: Fixture providing product data.
        
    Returns:
        Instance of the Product class.
    """
    return Product(**sample_product_data)


@pytest.fixture
def mock_database() -> Generator[Mock, None, None]:
    """
    Provide a mock database connection for tests.
    
    This fixture uses mocking to simulate a database connection,
    avoiding the need for a real database during tests.
    
    Yields:
        Mocked database connection object.
    """

    with patch('your_module.DatabaseConnection') as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        mock_db_instance.query.return_value.filter.return_value.first.return_value = None
        mock_db_instance.commit.return_value = None
        
        yield mock_db_instance


@pytest.fixture
def mock_api_client() -> Generator[Mock, None, None]:
    """
    Provide a mock API client for tests.
    
    This fixture simulates an external API client, allowing tests
    to run without making real network requests.
    
    Yields:
        Mocked API client object.
    """
    with patch('your_module.ApiClient') as mock_api_class:
        mock_api_instance = mock_api_class.return_value
        mock_api_instance.get.return_value.json.return_value = {'status': 'success'}
        mock_api_instance.post.return_value.status_code = 201
        
        yield mock_api_instance


@pytest.fixture
def temp_config_file() -> Generator[str, None, None]:
    """
    Provide a temporary configuration file for tests.
    
    This fixture creates a temporary JSON configuration file
    that can be used for testing configuration loading.
    
    Yields:
        Path to the temporary configuration file.
    """
    config_data = {
        'database': {'url': 'sqlite:///test.db'},
        'api': {'key': 'test_api_key'},
        'logging': {'level': 'DEBUG'}
    }
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as f:
        json.dump(config_data, f)
        temp_file_path = f.name
    
    yield temp_file_path
    
    # Cleanup the temporary file
    os.unlink(temp_file_path)


@pytest.fixture(params=[
    ("user1", "pass1", True),
    ("user2", "pass2", False),
    ("user3", "pass3", True)
])
def user_credentials(request) -> tuple:
    """

    Provide parameterized user credentials for tests.
    
    This fixture demonstrates how to use parameterization to
    run tests with different sets of data.
    
    Args:
        request: Pytest request object.
        
    Returns:
        Tuple containing username, password, and expected outcome.
    """
    return request.param


# Example usage in a test
def test_login_with_credentials(user_credentials):
    """
    Test login functionality with various credentials.
    
    This test uses the parameterized fixture to test the
    login function with different user inputs.
    """
    username, password, expected_success = user_credentials
    
    # Assume a login function exists
    result = login(username, password)
    
    assert result['success'] == expected_success


# Helper functions to simulate classes being used in fixtures
class User:
    def __init__(self, id, name, email, is_active, roles):
        self.id = id
        self.name = name
        self.email = email
        self.is_active = is_active
        self.roles = roles

class Product:
    def __init__(self, id, name, price, category, in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

def login(username, password):
    if "1" in username:
        return {'success': True}
    return {'success': False}

# These would normally be in `your_module.py`
class DatabaseConnection:
    def query(self, *args, **kwargs):
        pass
    def commit(self, *args, **kwargs):
        pass

class ApiClient:
    def get(self, *args, **kwargs):
        pass
    def post(self, *args, **kwargs):
        pass
		
# Example of how to use the fixtures in a test class
class TestWithFixtures:
    def test_user_creation(self, user_instance: User):
        assert user_instance.name == 'Test User'
        assert user_instance.email == 'test@example.com'

    def test_database_query(self, mock_database: Mock):
        # This function would use the database connection
        result = get_user_from_db(1, mock_database)
        assert result is None
        mock_database.query.assert_called_once()
        
def get_user_from_db(user_id, db_connection):
    return db_connection.query("User").filter(id=user_id).first() 