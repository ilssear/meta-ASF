# End-to-End Testing in SpecFirst

## Overview
End-to-end (E2E) testing in SpecFirst validates complete user workflows and system behavior from the user's perspective. This guide outlines the approach, tools, and best practices for implementing effective E2E tests.

## Key Principles

### 1. User-Centric Testing
- Test complete user workflows
- Validate system behavior from user perspective
- Focus on real-world scenarios

### 2. Specification Validation
- Ensure system meets all requirements
- Validate end-to-end functionality
- Test against user stories

### 3. Test Organization
- Group tests by user workflow
- Use clear naming conventions
- Maintain test independence

## Implementation Guidelines

### Test Structure
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

import pytest
from typing import Any, Dict

class TestUserWorkflow:
    """Test suite for user workflow validation."""
    
    def test_complete_workflow(self) -> None:
        """Test a complete user workflow."""
        # Test implementation
        pass

    def test_workflow_variations(self) -> None:
        """Test workflow variations and edge cases."""
        # Variation tests
        pass

    def test_error_recovery(self) -> None:
        """Test error recovery in workflows."""
        # Error recovery tests
        pass
```

### Best Practices
1. Test real user scenarios
2. Use realistic test data
3. Validate complete workflows
4. Test error scenarios
5. Verify system state

### Test Categories
1. **User Workflow Tests**
   - Test complete user journeys
   - Validate business processes
   - Verify system behavior

2. **Scenario Tests**
   - Test common scenarios
   - Validate edge cases
   - Verify error handling

3. **System State Tests**
   - Test system state transitions
   - Validate data persistence
   - Verify cleanup processes

## Tools and Frameworks

### Primary Tools
- pytest for test execution
- selenium for web testing
- playwright for modern web testing
- requests for API testing

### Configuration
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

# pytest.ini
[pytest]
testpaths = tests/e2e
python_files = test_*_e2e.py
python_classes = Test*E2E
python_functions = test_*
addopts = --verbose --cov=src --cov-report=term-missing
```

## Common Patterns

### Web Application Testing
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

import pytest
from playwright.sync_api import Page, expect

def test_user_login(page: Page) -> None:
    """Test user login workflow."""
    page.goto("/login")
    page.fill("#username", "test_user")
    page.fill("#password", "test_pass")
    page.click("#login-button")
    expect(page).to_have_url("/dashboard")
```

### API Testing
```python
# Copyright (c) [Year], [Full Name] ([Email Address])

import pytest
import requests
from typing import Dict, Any

def test_api_workflow() -> None:
    """Test complete API workflow."""
    # Create resource
    response = requests.post("/api/resources", json={"name": "test"})
    assert response.status_code == 201
    resource_id = response.json()["id"]
    
    # Get resource
    response = requests.get(f"/api/resources/{resource_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "test"
```

## Troubleshooting

### Common Issues
1. **Test Stability**
   - Problem: Flaky tests
   - Solution: Use proper waits and assertions

2. **Test Data**
   - Problem: Test data management
   - Solution: Use data factories and cleanup

3. **Environment Setup**
   - Problem: Inconsistent environment
   - Solution: Use docker-compose for setup

## Version History
- v1.0.0 (2025-01-01): Initial release
- v1.1.0 (2025-02-01): Added web testing patterns
- v1.2.0 (2025-03-01): Updated best practices

## References
- [SpecFirst Testing Guide](../framework/best_practices/testing_guide.md)
- [User Workflow Patterns](../framework/patterns/workflow_patterns.md)
- [SpecFirst Methodology](../framework/methodology/AGILE_SPECFIRST.md) 