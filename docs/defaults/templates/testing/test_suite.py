# Copyright (c) {{YEAR}} {{AUTHOR}}
# All rights reserved.
#
# This file is part of {{PROJECT}}.
# Version: {{VERSION}}
#
# Test suite template for organizing and running tests.

import unittest
from typing import List, Type
import logging
import sys
from pathlib import Path

class TestSuiteTemplate:
    """Template for creating test suites.
    
    This class provides a template for organizing and running test suites with:
    - Test discovery
    - Suite organization
    - Test execution
    - Result reporting
    """
    
    def __init__(self, test_dir: str = "tests"):
        """Initialize test suite.
        
        Args:
            test_dir: Directory containing test files
        """
        self.test_dir = Path(test_dir)
        self.logger = logging.getLogger(__name__)
        self.suite = unittest.TestSuite()
    
    def discover_tests(self, pattern: str = "test_*.py") -> None:
        """Discover test cases.
        
        Args:
            pattern: Pattern to match test files
        """
        self.logger.info(f"Discovering tests in {self.test_dir}")
        loader = unittest.TestLoader()
        discovered = loader.discover(
            str(self.test_dir),
            pattern=pattern
        )
        self.suite.addTest(discovered)
    
    def add_test_case(self, test_case: Type[unittest.TestCase]) -> None:
        """Add a test case to the suite.
        
        Args:
            test_case: Test case class to add
        """
        self.logger.info(f"Adding test case: {test_case.__name__}")
        self.suite.addTest(unittest.makeSuite(test_case))
    
    def add_test_method(
        self,
        test_case: Type[unittest.TestCase],
        method_name: str
    ) -> None:
        """Add a specific test method to the suite.
        
        Args:
            test_case: Test case class containing the method
            method_name: Name of the test method to add
        """
        self.logger.info(f"Adding test method: {method_name}")
        self.suite.addTest(test_case(method_name))
    
    def run_tests(self, verbosity: int = 2) -> unittest.TestResult:
        """Run the test suite.
        
        Args:
            verbosity: Level of detail in test output
        
        Returns:
            TestResult object containing test results
        """
        self.logger.info("Running test suite")
        runner = unittest.TextTestRunner(verbosity=verbosity)
        return runner.run(self.suite)
    
    def generate_report(self, result: unittest.TestResult) -> None:
        """Generate test report.
        
        Args:
            result: TestResult object from test execution
        """
        self.logger.info("Generating test report")
        
        print("\nTest Report")
        print("===========")
        print(f"Tests run: {result.testsRun}")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
        print(f"Skipped: {len(result.skipped)}")
        
        if result.failures:
            print("\nFailures:")
            for failure in result.failures:
                print(f"\n{failure[0]}")
                print(failure[1])
        
        if result.errors:
            print("\nErrors:")
            for error in result.errors:
                print(f"\n{error[0]}")
                print(error[1])

def main():
    """Run the test suite."""
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    
    # Create and run test suite
    suite = TestSuiteTemplate()
    suite.discover_tests()
    result = suite.run_tests()
    suite.generate_report(result)
    
    # Exit with appropriate status code
    sys.exit(not result.wasSuccessful())

if __name__ == "__main__":
    main() 