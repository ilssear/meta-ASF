#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Test Suite Template for SpecFirst Framework Projects.

This template provides a comprehensive test suite structure following TDD principles
and the framework's testing patterns. It includes unit tests, integration tests,
and security tests with proper organization and documentation.
"""

import pytest
import unittest
from unittest.mock import Mock, patch, MagicMock
from typing import Dict, List, Any, Optional
import json
import tempfile
import os
from pathlib import Path

# Import modules and classes to be tested
from your_module import UserManager, ProductManager, ApiService


class BaseTestSuite:
    """Base test suite with common setup and utilities."""
    
    @classmethod
    def setUpClass(cls):
        """Set up test class with common configuration."""
        cls.test_data_dir = Path(__file__).parent / "test_data"
        cls.test_data_dir.mkdir(exist_ok=True)
        
        # Common test configuration
        cls.config = {
            "test_mode": True,
            "database": "test.db",
            "log_level": "DEBUG"
        }
    
    @classmethod
    def tearDownClass(cls):
        """Clean up test class resources."""
        # Clean up test data
        if cls.test_data_dir.exists():
            for file in cls.test_data_dir.glob("*"):
                file.unlink()
            cls.test_data_dir.rmdir()
    
    def setUp(self):
        """Set up individual test case."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_data = self._create_test_data()
    
    def tearDown(self):
        """Clean up individual test case."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def _create_test_data(self) -> Dict[str, Any]:
        """Create test data for the test case."""
        return {
            "user": {
                "id": 1,
                "name": "Test User",
                "email": "test@example.com",
                "role": "user"
            },
            "admin": {
                "id": 2,
                "name": "Admin User",
                "email": "admin@example.com",
                "role": "admin"
            }
        }


class UnitTestSuite(BaseTestSuite):
    """Unit test suite for individual components."""
    
    def test_component_initialization(self):
        """Test component initialization with valid parameters."""
        # Arrange
        expected_name = "Test Component"
        expected_version = "1.0.0"
        
        # Act
        component = self._create_test_component(name=expected_name, version=expected_version)
        
        # Assert
        assert component.name == expected_name
        assert component.version == expected_version
        assert component.is_active is True
    
    def test_component_validation(self):
        """Test component validation with invalid parameters."""
        # Arrange
        invalid_name = ""
        invalid_version = "invalid"
        
        # Act & Assert
        with pytest.raises(ValueError, match="Name cannot be empty"):
            self._create_test_component(name=invalid_name)
        
        with pytest.raises(ValueError, match="Invalid version format"):
            self._create_test_component(version=invalid_version)
    
    def test_component_methods(self):
        """Test component method functionality."""
        # Arrange
        component = self._create_test_component()
        test_input = "test data"
        
        # Act
        result = component.process_data(test_input)
        
        # Assert
        assert result is not None
        assert isinstance(result, str)
        assert "processed" in result.lower()
    
    def test_component_error_handling(self):
        """Test component error handling."""
        # Arrange
        component = self._create_test_component()
        
        # Act & Assert
        with pytest.raises(RuntimeError, match="Processing failed"):
            component.process_data(None)
    
    def _create_test_component(self, **kwargs) -> Any:
        """Create a test component instance."""
        # Mock component for testing
        component = Mock()
        component.name = kwargs.get("name", "Test Component")
        component.version = kwargs.get("version", "1.0.0")
        component.is_active = True
        
        # Mock methods
        component.process_data = Mock(side_effect=self._mock_process_data)
        
        return component
    
    def _mock_process_data(self, data: Any) -> str:
        """Mock data processing method."""
        if data is None:
            raise RuntimeError("Processing failed")
        return f"processed: {data}"


class IntegrationTestSuite(BaseTestSuite):
    """Integration test suite for component interactions."""
    
    def test_component_integration(self):
        """Test integration between multiple components."""
        # Arrange
        component_a = self._create_component_a()
        component_b = self._create_component_b()
        
        # Act
        result = self._integrate_components(component_a, component_b)
        
        # Assert
        assert result is not None
        assert result["status"] == "success"
        assert "data" in result
    
    def test_api_integration(self):
        """Test API integration with external services."""
        # Arrange
        api_client = self._create_api_client()
        test_data = {"key": "value"}
        
        # Act
        with patch.object(api_client, 'post') as mock_post:
            mock_post.return_value.status_code = 200
            mock_post.return_value.json.return_value = {"success": True}
            
            response = api_client.post("/api/test", json=test_data)
        
        # Assert
        assert response.status_code == 200
        assert response.json()["success"] is True
        mock_post.assert_called_once_with("/api/test", json=test_data)
    
    def test_database_integration(self):
        """Test database integration."""
        # Arrange
        db_connection = self._create_db_connection()
        test_record = {"name": "Test", "value": 123}
        
        # Act
        with patch.object(db_connection, 'execute') as mock_execute:
            mock_execute.return_value.rowcount = 1
            
            result = db_connection.insert_record("test_table", test_record)
        
        # Assert
        assert result is True
        mock_execute.assert_called_once()
    
    def _create_component_a(self) -> Any:
        """Create test component A."""
        component = Mock()
        component.process = Mock(return_value={"data": "processed_a"})
        return component
    
    def _create_component_b(self) -> Any:
        """Create test component B."""
        component = Mock()
        component.process = Mock(return_value={"data": "processed_b"})
        return component
    
    def _integrate_components(self, comp_a: Any, comp_b: Any) -> Dict[str, Any]:
        """Integrate two components."""
        result_a = comp_a.process()
        result_b = comp_b.process()
        
        return {
            "status": "success",
            "data": {
                "a": result_a["data"],
                "b": result_b["data"]
            }
        }
    
    def _create_api_client(self) -> Any:
        """Create test API client."""
        client = Mock()
        client.post = Mock()
        return client
    
    def _create_db_connection(self) -> Any:
        """Create test database connection."""
        connection = Mock()
        connection.execute = Mock()
        return connection


class SecurityTestSuite(BaseTestSuite):
    """Security test suite for vulnerability assessment."""
    
    def test_authentication_security(self):
        """Test authentication security measures."""
        # Arrange
        auth_service = self._create_auth_service()
        valid_credentials = {"username": "user", "password": "password123"}
        invalid_credentials = {"username": "user", "password": "wrong"}
        
        # Act
        valid_result = auth_service.authenticate(valid_credentials)
        invalid_result = auth_service.authenticate(invalid_credentials)
        
        # Assert
        assert valid_result["success"] is True
        assert "token" in valid_result
        assert invalid_result["success"] is False
        assert "error" in invalid_result
    
    def test_input_validation_security(self):
        """Test input validation security."""
        # Arrange
        validator = self._create_input_validator()
        malicious_inputs = [
            "<script>alert('xss')</script>",
            "'; DROP TABLE users; --",
            "../../../etc/passwd",
            "{{7*7}}"
        ]
        
        # Act & Assert
        for malicious_input in malicious_inputs:
            with pytest.raises(ValueError, match="Invalid input"):
                validator.validate(malicious_input)
    
    def test_authorization_security(self):
        """Test authorization security controls."""
        # Arrange
        auth_service = self._create_auth_service()
        user_token = auth_service.authenticate({"username": "user", "password": "password123"})["token"]
        admin_token = auth_service.authenticate({"username": "admin", "password": "admin123"})["token"]
        
        # Act
        user_access = auth_service.check_permission(user_token, "admin:read")
        admin_access = auth_service.check_permission(admin_token, "admin:read")
        
        # Assert
        assert user_access is False
        assert admin_access is True
    
    def _create_auth_service(self) -> Any:
        """Create test authentication service."""
        service = Mock()
        
        def mock_authenticate(credentials):
            if credentials["password"] in ["password123", "admin123"]:
                return {
                    "success": True,
                    "token": f"token_{credentials['username']}"
                }
            return {"success": False, "error": "Invalid credentials"}
        
        def mock_check_permission(token, permission):
            if "admin" in token and "admin:" in permission:
                return True
            return False
        
        service.authenticate = Mock(side_effect=mock_authenticate)
        service.check_permission = Mock(side_effect=mock_check_permission)
        return service
    
    def _create_input_validator(self) -> Any:
        """Create test input validator."""
        validator = Mock()
        
        def mock_validate(input_data):
            malicious_patterns = [
                "<script>",
                "DROP TABLE",
                "../",
                "{{",
                "javascript:"
            ]
            
            for pattern in malicious_patterns:
                if pattern in str(input_data):
                    raise ValueError("Invalid input")
            
            return True
        
        validator.validate = Mock(side_effect=mock_validate)
        return validator


class PerformanceTestSuite(BaseTestSuite):
    """Performance test suite for system performance validation."""
    
    def test_response_time(self):
        """Test API response time."""
        import time
        
        # Arrange
        api_client = self._create_api_client()
        max_response_time = 1.0  # seconds
        
        # Act
        start_time = time.time()
        response = api_client.get("/api/test")
        end_time = time.time()
        
        response_time = end_time - start_time
        
        # Assert
        assert response.status_code == 200
        assert response_time < max_response_time
    
    def test_memory_usage(self):
        """Test memory usage under load."""
        import psutil
        import os
        
        # Arrange
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Act
        large_data = ["x" * 1000 for _ in range(1000)]
        
        # Assert
        current_memory = process.memory_info().rss
        memory_increase = current_memory - initial_memory
        
        # Memory increase should be reasonable (less than 100MB)
        assert memory_increase < 100 * 1024 * 1024
    
    def _create_api_client(self) -> Any:
        """Create test API client."""
        client = Mock()
        client.get = Mock(return_value=Mock(status_code=200))
        return client


# Test configuration and utilities
class TestConfig:
    """Test configuration and utilities."""
    
    @staticmethod
    def create_test_user(**kwargs) -> Dict[str, Any]:
        """Create a test user with default values."""
        default_user = {
            "id": 1,
            "name": "Test User",
            "email": "test@example.com",
            "role": "user",
            "is_active": True
        }
        default_user.update(kwargs)
        return default_user
    
    @staticmethod
    def create_test_data(size: int = 100) -> List[Dict[str, Any]]:
        """Create test data of specified size."""
        return [
            {
                "id": i,
                "name": f"Item {i}",
                "value": i * 10,
                "category": f"Category {i % 5}"
            }
            for i in range(size)
        ]


# Test fixtures for pytest
@pytest.fixture
def test_user():
    """Fixture for test user data."""
    return TestConfig.create_test_user()


@pytest.fixture
def test_data():
    """Fixture for test data."""
    return TestConfig.create_test_data(10)


@pytest.fixture
def mock_api_client():
    """Fixture for mock API client."""
    client = Mock()
    client.get = Mock(return_value=Mock(status_code=200, json=lambda: {"success": True}))
    client.post = Mock(return_value=Mock(status_code=201, json=lambda: {"id": 1}))
    return client


# Main test execution
if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])


class TestUserManagerSuite:
    """
    Test suite for the UserManager class.
    
    This suite covers all aspects of user management, including creation,
    retrieval, updating, and deletion of users.
    """
    
    @pytest.fixture(autouse=True)
    def setup_method(self, mock_database: Mock):
        """
        Setup method for the UserManager test suite.
        
        This method is called before each test in this suite and
        sets up a clean UserManager instance with a mocked database.
        """
        self.user_manager = UserManager(db_connection=mock_database)
        self.mock_db = mock_database
    
    def test_create_user_success(self, sample_user_data: Dict[str, Any]):
        """
        Test successful creation of a user.
        
        This test verifies that a new user can be created with valid
        data and is correctly stored in the database.
        """
        # Arrange
        self.mock_db.add.return_value = sample_user_data
        
        # Act
        new_user = self.user_manager.create_user(sample_user_data)
        
        # Assert
        assert new_user['name'] == sample_user_data['name']
        self.mock_db.add.assert_called_once_with(sample_user_data)
        self.mock_db.commit.assert_called_once()
    
    def test_get_user_by_id(self, sample_user_data: Dict[str, Any]):
        """
        Test retrieving a user by ID.
        
        This test verifies that an existing user can be retrieved
        from the database by their ID.
        """
        # Arrange
        user_id = sample_user_data['id']
        self.mock_db.query.return_value.filter_by.return_value.first.return_value = sample_user_data
        
        # Act
        user = self.user_manager.get_user(user_id)
        
        # Assert
        assert user is not None
        assert user['id'] == user_id
        self.mock_db.query.assert_called_once()
    
    def test_get_user_not_found(self):
        """
        Test retrieving a non-existent user.
        
        This test verifies that getting a non-existent user
        returns None and does not raise an error.
        """
        # Arrange
        self.mock_db.query.return_value.filter_by.return_value.first.return_value = None
        
        # Act
        user = self.user_manager.get_user(999)
        
        # Assert
        assert user is None
    
    def test_update_user_email(self, sample_user_data: Dict[str, Any]):
        """
        Test updating a user's email address.
        
        This test verifies that a user's email can be updated
        and the changes are committed to the database.
        """
        # Arrange
        user_id = sample_user_data['id']
        new_email = "new.email@example.com"
        self.mock_db.query.return_value.filter_by.return_value.first.return_value = sample_user_data
        
        # Act
        updated_user = self.user_manager.update_user(user_id, {'email': new_email})
        
        # Assert
        assert updated_user['email'] == new_email
        self.mock_db.commit.assert_called_once()
    
    def test_delete_user(self, sample_user_data: Dict[str, Any]):
        """
        Test deleting a user.
        
        This test verifies that a user can be deleted and the
        changes are committed to the database.
        """
        # Arrange
        user_id = sample_user_data['id']
        self.mock_db.query.return_value.filter_by.return_value.first.return_value = sample_user_data
        
        # Act
        result = self.user_manager.delete_user(user_id)
        
        # Assert
        assert result is True
        self.mock_db.delete.assert_called_once_with(sample_user_data)
        self.mock_db.commit.assert_called_once()


@pytest.mark.integration
class TestProductManagerSuite:
    """
    Integration test suite for the ProductManager class.
    
    This suite tests the ProductManager's interaction with a real
    (or test) database and external services.
    """
    
    @pytest.fixture(autouse=True)
    def setup_method(self, real_database_connection):
        """
        Setup method for the ProductManager test suite.
        
        This method uses a real database connection for integration
        testing purposes.
        """
        self.product_manager = ProductManager(db_connection=real_database_connection)
    
    def test_add_product_to_database(self, sample_product_data: Dict[str, Any]):
        """
        Test adding a product to the database.
        
        This test verifies that a new product can be added to the
        database and retrieved correctly.
        """
        # Act
        new_product = self.product_manager.add_product(sample_product_data)
        retrieved_product = self.product_manager.get_product(new_product['id'])
        
        # Assert
        assert retrieved_product is not None
        assert retrieved_product['name'] == sample_product_data['name']
    
    def test_update_product_price(self, sample_product_data: Dict[str, Any]):
        """
        Test updating a product's price in the database.
        
        This test verifies that a product's price can be updated
        and the change is reflected in subsequent queries.
        """
        # Arrange
        new_product = self.product_manager.add_product(sample_product_data)
        new_price = 129.99
        
        # Act
        self.product_manager.update_product(new_product['id'], {'price': new_price})
        updated_product = self.product_manager.get_product(new_product['id'])
        
        # Assert
        assert updated_product['price'] == new_price


class TestApiServiceSuite:
    """
    Test suite for the ApiService class.
    
    This suite tests the interaction of the ApiService with
    external APIs using mocked responses.
    """
    
    @pytest.fixture(autouse=True)
    def setup_method(self, mock_api_client: Mock):
        """
        Setup method for the ApiService test suite.
        
        This method sets up a clean ApiService instance with a
        mocked API client for each test.
        """
        self.api_service = ApiService(api_client=mock_api_client)
        self.mock_api = mock_api_client
    
    def test_get_data_from_endpoint(self):
        """
        Test getting data from an external API endpoint.
        
        This test verifies that the service can correctly parse
        and return data from a mocked API response.
        """
        # Arrange
        endpoint = "/test-data"
        mock_response = {'data': [{'id': 1}, {'id': 2}]}
        self.mock_api.get.return_value.json.return_value = mock_response
        
        # Act
        data = self.api_service.get_data(endpoint)
        
        # Assert
        assert len(data) == 2
        assert data[0]['id'] == 1
        self.mock_api.get.assert_called_once_with(endpoint)
    
    def test_post_data_to_endpoint(self):
        """
        Test posting data to an external API endpoint.
        
        This test verifies that the service can successfully post
        data and handle the API response.
        """
        # Arrange
        endpoint = "/create-item"
        payload = {'name': 'New Item'}
        self.mock_api.post.return_value.status_code = 201
        
        # Act
        success = self.api_service.post_data(endpoint, payload)
        
        # Assert
        assert success is True
        self.mock_api.post.assert_called_once_with(endpoint, json=payload)


# Helper fixtures for the test suites
@pytest.fixture
def mock_database() -> Generator[Mock, None, None]:
    """Provide a mock database connection for tests."""
    with patch('your_module.DatabaseConnection') as mock_db_class:
        mock_db_instance = mock_db_class.return_value
        yield mock_db_instance

@pytest.fixture
def mock_api_client() -> Generator[Mock, None, None]:
    """Provide a mock API client for tests."""
    with patch('your_module.ApiClient') as mock_api_class:
        mock_api_instance = mock_api_class.return_value
        yield mock_api_instance

@pytest.fixture
def sample_user_data() -> Dict[str, Any]:
    """Provide sample user data."""
    return {'id': 1, 'name': 'Test User', 'email': 'test@example.com'}

@pytest.fixture
def sample_product_data() -> Dict[str, Any]:
    """Provide sample product data."""
    return {'id': 1, 'name': 'Test Product', 'price': 99.99}

@pytest.fixture(scope="module")
def real_database_connection():
    """Provide a real database connection for integration tests."""
    # This would set up a connection to a test database
    # For this example, we'll just return a mock
    db_conn = Mock()
    # Setup in-memory database or test container here
    yield db_conn
    # Teardown database connection
    
# These are mock classes that would be in your_module.py
class UserManager:
    def __init__(self, db_connection):
        self.db = db_connection
    def create_user(self, data):
        self.db.add(data)
        self.db.commit()
        return data
    def get_user(self, user_id):
        return self.db.query().filter_by(id=user_id).first()
    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        for key, value in data.items():
            user[key] = value
        self.db.commit()
        return user
    def delete_user(self, user_id):
        user = self.get_user(user_id)
        self.db.delete(user)
        self.db.commit()
        return True

class ProductManager:
    def __init__(self, db_connection):
        self.db = db_connection
    def add_product(self, data):
        # In a real scenario, this would interact with the database
        return data
    def get_product(self, product_id):
        # In a real scenario, this would query the database
        return {'id': product_id, 'name': 'Test Product'}
    def update_product(self, product_id, data):
        pass

class ApiService:
    def __init__(self, api_client):
        self.api_client = api_client
    def get_data(self, endpoint):
        response = self.api_client.get(endpoint)
        return response.json()['data']
    def post_data(self, endpoint, payload):
        response = self.api_client.post(endpoint, json=payload)
        return response.status_code == 201 