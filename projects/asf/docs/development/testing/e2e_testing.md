# Copyright (c) 2025 Jaime Moraga (jmoraga@mines.edu)
# All rights reserved.
#
# This file is part of Agile SpecFirst for Cursor.
# Version: 1.0.0
#
# End-to-end testing guide.

# End-to-End Testing Guide

## Overview
This guide provides comprehensive end-to-end testing instructions and best practices.

## E2E Testing Structure

### 1. Test Organization
- Test modules
- Test classes
- Test functions
- Test fixtures

### 2. Test Types
- User flow tests
- System tests
- Performance tests
- Security tests

### 3. Test Tools
- Selenium
- Playwright
- Cypress
- Puppeteer

### 4. Test Process
- Test planning
- Test writing
- Test execution
- Test maintenance

## E2E Testing Implementation

### 1. Test Design
- Clear structure
- Logical grouping
- Easy maintenance
- Good documentation

### 2. Test Writing
- Clear naming
- Proper setup
- Good assertions
- Error handling

### 3. Test Execution
- Reliable runs
- Fast execution
- Good coverage
- Clear reporting

### 4. Test Maintenance
- Regular updates
- Version control
- Documentation
- Performance optimization

## Best Practices

### 1. Test Organization
- Clear structure
- Logical grouping
- Easy maintenance
- Good documentation

### 2. Test Implementation
- Clear naming
- Proper setup
- Good assertions
- Error handling

### 3. Test Execution
- Reliable runs
- Fast execution
- Good coverage
- Clear reporting

### 4. Test Maintenance
- Regular updates
- Version control
- Documentation
- Performance optimization

## Examples

### 1. Good E2E Testing
```python
def test_user_registration_flow():
    """Test complete user registration flow."""
    # Arrange
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000')
    
    try:
        # Act - Navigate to registration
        driver.find_element(By.LINK_TEXT, 'Register').click()
        
        # Act - Fill registration form
        driver.find_element(By.NAME, 'username').send_keys('testuser')
        driver.find_element(By.NAME, 'email').send_keys('test@example.com')
        driver.find_element(By.NAME, 'password').send_keys('secure123')
        driver.find_element(By.NAME, 'confirm_password').send_keys('secure123')
        
        # Act - Submit form
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        
        # Assert - Check success message
        success_message = driver.find_element(By.CLASS_NAME, 'alert-success')
        assert 'Registration successful' in success_message.text
        
        # Assert - Check redirect
        assert '/dashboard' in driver.current_url
        
        # Assert - Check user data
        profile_link = driver.find_element(By.LINK_TEXT, 'Profile')
        profile_link.click()
        assert driver.find_element(By.CLASS_NAME, 'username').text == 'testuser'
        
    finally:
        driver.quit()
```

### 2. Poor E2E Testing
```python
def test_registration():
    driver = webdriver.Chrome()
    driver.get('http://localhost:3000/register')
    driver.find_element(By.NAME, 'username').send_keys('test')
    driver.find_element(By.CSS_SELECTOR, 'button').click()
    assert 'success' in driver.page_source
    driver.quit()
```

## Common Pitfalls

### 1. Test Organization
- Missing structure
- Poor grouping
- Hard maintenance
- Bad documentation

### 2. Test Implementation
- Unclear naming
- Bad setup
- Weak assertions
- No error handling

### 3. Test Execution
- Unreliable runs
- Slow execution
- Poor coverage
- Unclear reporting

### 4. Test Maintenance
- No updates
- No version control
- No documentation
- No optimization

## References
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Playwright Guide](https://playwright.dev/python/docs/intro)
- [Cypress Documentation](https://docs.cypress.io/)
- [Testing Best Practices](https://martinfowler.com/articles/practical-test-pyramid.html) 