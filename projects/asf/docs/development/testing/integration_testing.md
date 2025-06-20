# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Integration Testing

## Overview
This document describes integration testing practices and standards for the SpecFirst Development Framework. Integration testing ensures that different components of the application work together as expected.

## Integration Testing Principles

### 1. Specification-Driven Testing
- Tests are based on user workflows and interactions defined in specifications
- Validate data flow and communication between components
- Ensure that integrated components meet functional requirements
- Maintain alignment between tests and specifications

### 2. Isolate External Services
- Mock external services to isolate the application
- Use test doubles for third-party APIs and databases
- Focus on testing the integration points within the application
- Avoid dependencies on external systems

### 3. Incremental Testing
- Test components as they are integrated
- Use a bottom-up or top-down approach
- Identify integration issues early
- Reduce complexity by testing in small increments

### 4. Comprehensive Coverage
- Test all major integration points
- Cover both success and failure scenarios
- Validate data consistency and integrity
- Test performance of integrated components

## Integration Test Structure

### Test File Organization
```
tests/
├── integration/
│   ├── test_auth_service.py
│   ├── test_order_processing.py
│   └── test_api_endpoints.py
├── fixtures/
│   ├── integration_data.py
│   └── mock_services.py
└── conftest.py
```

### Test Function Structure
```python
def test_component_interaction_scenario():
    """
    Test description explaining the integration being tested.
    
    This test verifies that Component A and Component B
    interact correctly under specific conditions.
    """
    # Arrange - Setup integrated components and test data
    component_a = setup_component_a()
    component_b = setup_component_b()
    test_data = create_test_data()
    
    # Act - Trigger the interaction between components
    result = component_a.process(test_data)
    
    # Assert - Verify the outcome and component states
    assert result.is_successful
    assert component_b.state_updated
```

## Test Categories

### 1. API Endpoint Testing
- Test API endpoints with various inputs
- Validate request/response formats
- Check authentication and authorization
- Test error handling and status codes

### 2. Service Integration Testing
- Test interactions between different microservices
- Validate inter-service communication protocols
- Check data consistency between services
- Test resilience and fault tolerance

### 3. Database Integration Testing
- Test interactions with the database
- Validate data storage and retrieval
- Check data integrity and constraints
- Test transaction management

### 4. UI/Backend Integration Testing
- Test interactions between the user interface and backend
- Validate data flow from UI to backend
- Check for proper state management
- Test error handling and user feedback

## Test Writing Guidelines

### Test Scenarios
- Base tests on user stories and workflows
- Test both positive and negative paths
- Include edge cases and boundary conditions
- Use clear, descriptive scenario names

### Test Data
- Use realistic test data
- Ensure data consistency across components
- Clean up test data after tests
- Use factories for complex data setup

### Assertions
- Assert on final outcomes and state changes
- Verify data consistency
- Check for expected side effects
- Use meaningful assertion messages

## Test Framework Setup

### API Testing (e.g., with requests and pytest)
```python
import pytest
import requests

BASE_URL = "http://localhost:8000/api"

def test_create_user_endpoint():
    """Test user creation API endpoint."""
    # Arrange
    user_data = {'username': 'testuser', 'password': 'password123'}
    
    # Act
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    
    # Assert
    assert response.status_code == 201
    assert response.json()['username'] == 'testuser'
```

### Database Testing (e.g., with SQLAlchemy and pytest)
```python
def test_user_creation_in_db(db_session):
    """Test creating a user and storing it in the database."""
    # Arrange
    user = User(username='testdbuser', password='password')
    
    # Act
    db_session.add(user)
    db_session.commit()
    
    # Assert
    retrieved_user = db_session.query(User).filter_by(username='testdbuser').first()
    assert retrieved_user is not None
    assert retrieved_user.username == 'testdbuser'
```

## Mocking External Services

### API Mocking
```python
@patch('requests.post')
def test_service_with_mocked_api(mock_post):
    """Test service interaction with a mocked external API."""
    # Arrange
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {'status': 'success'}
    
    # Act
    result = external_service.create_item({'name': 'test'})
    
    # Assert
    assert result == 'success'
    mock_post.assert_called_once()
```

### Database Mocking
- Use in-memory databases (e.g., SQLite in-memory)
- Use test containers for real database instances
- Mock database connections for specific tests
- Use fixtures to manage database state

## Test Fixtures

### Database Fixtures
```python
@pytest.fixture(scope="session")
def db_engine():
    """Create a test database engine."""
    return create_engine("sqlite:///:memory:")

@pytest.fixture
def db_session(db_engine):
    """Create a test database session."""
    connection = db_engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()
```

### Service Fixtures
```python
@pytest.fixture
def auth_service():
    """Provide an instance of the authentication service."""
    return AuthService()

@pytest.fixture
def payment_service(mock_payment_gateway):
    """Provide a payment service with a mocked gateway."""
    return PaymentService(gateway=mock_payment_gateway)
```

## Test Coverage

### Coverage Goals
- Focus on covering all major integration points
- Test all user workflows and interactions
- Ensure data flows are validated
- Aim for high branch coverage in integration paths

### Coverage Tools
- Use tools like `pytest-cov` to measure coverage
- Generate coverage reports to identify gaps
- Review coverage reports regularly
- Prioritize coverage for critical integration paths

## Test Execution

### Running Tests
```bash
# Run all integration tests
pytest tests/integration

# Run a specific integration test file
pytest tests/integration/test_api_endpoints.py

# Run tests with a specific marker
pytest -m integration

# Exclude integration tests
pytest -m "not integration"
```

### Test Environment
- Use a dedicated test environment
- Ensure environment is consistent and reproducible
- Use Docker or test containers for services
- Reset environment state between test runs

## Best Practices

### Test Design
- Keep tests focused on specific integration points
- Use clear, descriptive test names
- Make tests independent and repeatable
- Document complex test scenarios

### Test Maintenance
- Keep tests up-to-date with application changes
- Refactor tests to improve readability and performance
- Remove obsolete or redundant tests
- Regularly review and improve test suites

### Performance
- Be mindful of test execution time
- Use efficient test data setup and teardown
- Parallelize tests where possible
- Profile slow tests to identify bottlenecks

## Common Patterns

### Data-Driven Tests
```python
@pytest.mark.parametrize("input_data,expected_status", [
    ({'name': 'valid'}, 201),
    ({'name': ''}, 400),
    ({}, 400),
])
def test_create_item_validation(input_data, expected_status):
    """Test item creation with various inputs."""
    response = requests.post(f"{BASE_URL}/items", json=input_data)
    assert response.status_code == expected_status
```

### Workflow Tests
```python
def test_order_processing_workflow(db_session, mock_payment_gateway):
    """Test the complete order processing workflow."""
    # 1. Create a user and product
    user = create_user(db_session)
    product = create_product(db_session)
    
    # 2. Create an order
    order = create_order(db_session, user, product)
    
    # 3. Process payment
    payment_service = PaymentService(gateway=mock_payment_gateway)
    payment_success = payment_service.process_payment(order)
    
    # 4. Verify order status
    assert payment_success
    updated_order = db_session.query(Order).filter_by(id=order.id).first()
    assert updated_order.status == 'paid'
```

## References
- [AGILE_SPECFIRST.md](../../framework/methodology/AGILE_SPECFIRST.md) - Core methodology
- [VIBE_USER_GUIDE.md](../../framework/methodology/VIBE_USER_GUIDE.md) - User guidance
- [CURSOR_INTEGRATION.md](../../framework/methodology/CURSOR_INTEGRATION.md) - IDE integration

## Version Information
- Version: 1.0.0
- Last Updated: 2024-03-19
- Status: Active 