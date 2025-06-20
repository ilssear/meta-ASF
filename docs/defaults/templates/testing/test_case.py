# Copyright (c) {{YEAR}} {{AUTHOR}}
# All rights reserved.
#
# This file is part of {{PROJECT}}.
# Version: {{VERSION}}
#
# Test case template for unit tests.

import unittest
from typing import Any, Dict, Optional
import logging

class TestCaseTemplate(unittest.TestCase):
    """Template for creating test cases.
    
    This class provides a template for creating test cases with:
    - Proper setup and teardown
    - Test data management
    - Assertion helpers
    - Logging configuration
    """
    
    @classmethod
    def setUpClass(cls) -> None:
        """Set up test class.
        
        This method is called once before all tests in the class.
        """
        cls.logger = logging.getLogger(cls.__name__)
        cls.test_data = {}
    
    def setUp(self) -> None:
        """Set up test case.
        
        This method is called before each test method.
        """
        self.logger.info(f"Setting up test: {self._testMethodName}")
    
    def tearDown(self) -> None:
        """Clean up after test case.
        
        This method is called after each test method.
        """
        self.logger.info(f"Cleaning up test: {self._testMethodName}")
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Clean up test class.
        
        This method is called once after all tests in the class.
        """
        cls.test_data.clear()
    
    def test_example(self) -> None:
        """Example test method.
        
        This method demonstrates proper test structure with:
        - Clear test name
        - Arrange-Act-Assert pattern
        - Proper assertions
        - Error handling
        """
        # Arrange
        test_input = "test"
        expected = "TEST"
        
        # Act
        result = test_input.upper()
        
        # Assert
        self.assertEqual(result, expected)
        self.assertIsInstance(result, str)
    
    def test_example_with_data(self) -> None:
        """Example test method using test data.
        
        This method demonstrates:
        - Using test data
        - Multiple assertions
        - Error handling
        """
        # Arrange
        self.test_data["input"] = [1, 2, 3]
        expected_sum = 6
        
        # Act
        result = sum(self.test_data["input"])
        
        # Assert
        self.assertEqual(result, expected_sum)
        self.assertGreater(result, 0)
        self.assertIsInstance(result, int)

if __name__ == "__main__":
    unittest.main() 