#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Integration tests for validate_project.py script.
"""

import unittest
from pathlib import Path
import tempfile
import sys
import subprocess
import os

# Add script directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from validate_project import main as validate_main

class TestValidateProjectIntegration(unittest.TestCase):
    """Integration tests for validate_project.py."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_root = Path(self.temp_dir)
        self.script_path = Path(__file__).resolve().parent.parent.parent / "validate_project.py"
        
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def create_test_file(self, file_path, content=""):
        """Helper to create a test file."""
        full_path = self.project_root / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding='utf-8')
    
    def run_script(self, args=None):
        """Helper to run the validate_project.py script."""
        if args is None:
            args = []
        
        cmd = [sys.executable, str(self.script_path), "--root-dir", str(self.project_root)] + args
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=self.project_root
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def test_script_stage_1_no_specifications(self):
        """Test script output for Stage 1: No specifications."""
        returncode, stdout, stderr = self.run_script()
        
        self.assertEqual(returncode, 1)  # Should exit with error
        self.assertIn("Not a SpecFirst project", stdout)
    
    def test_script_stage_1_specifications_txt_only(self):
        """Test script output for Stage 1: Only specifications.txt exists."""
        self.create_test_file("specifications.txt", "Test content")
        returncode, stdout, stderr = self.run_script()
        
        self.assertEqual(returncode, 0)
        self.assertIn("Project Stage: 1", stdout)
        self.assertIn("Ready for Refinement", stdout)
    
    def test_script_stage_2_specifications_md_only(self):
        """Test script output for Stage 2: SPECIFICATIONS.md only."""
        self.create_test_file("SPECIFICATIONS.md", """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Test Project

## Implementation Requirements

### Framework Scripts
The framework includes essential scripts in the `scripts/` directory:
- `check_docs.py`: Documentation validation tool
  * Validates documentation structure
  * Checks required files
  * Verifies cross-references
  * Ensures documentation standards
  * Maintains documentation quality

#### Documentation Synchronization Paths
- methodology/AGILE_SPECFIRST.md
- methodology/VIBE_USER_GUIDE.md

### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
""")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        
        returncode, stdout, stderr = self.run_script()
        
        self.assertEqual(returncode, 0)
        self.assertIn("Project Stage: 2", stdout)
        self.assertIn("Ready to Generate", stdout)
    
    def test_script_stage_6_complete(self):
        """Test script output for Stage 6: Complete project."""
        # Create complete project structure
        self.create_test_file("SPECIFICATIONS.md", """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Test Project

## Implementation Requirements

### Framework Scripts
The framework includes essential scripts in the `scripts/` directory:
- `check_docs.py`: Documentation validation tool
  * Validates documentation structure
  * Checks required files
  * Verifies cross-references
  * Ensures documentation standards
  * Maintains documentation quality

#### Documentation Synchronization Paths
- methodology/AGILE_SPECFIRST.md
- methodology/VIBE_USER_GUIDE.md

### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
""")
        self.create_test_file("README.md", "Test content")
        self.create_test_file(".cursorrules", "Test content")
        self.create_test_file("docs/README.md", "Test content")
        self.create_test_file("scripts/check_docs.py", "Test content")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        
        returncode, stdout, stderr = self.run_script()
        
        self.assertEqual(returncode, 0)
        self.assertIn("Project Stage: 6", stdout)
        self.assertIn("Complete and Valid", stdout)
    
    def test_script_verbose_output(self):
        """Test script verbose output."""
        self.create_test_file("SPECIFICATIONS.md", """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Test Project

## Implementation Requirements

### Framework Scripts
The framework includes essential scripts in the `scripts/` directory:
- `check_docs.py`: Documentation validation tool
  * Validates documentation structure
  * Checks required files
  * Verifies cross-references
  * Ensures documentation standards
  * Maintains documentation quality

#### Documentation Synchronization Paths
- methodology/AGILE_SPECFIRST.md
- methodology/VIBE_USER_GUIDE.md

### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
""")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        
        returncode, stdout, stderr = self.run_script(["-v"])
        
        self.assertEqual(returncode, 0)
        self.assertIn("Project Stage: 2", stdout)
        self.assertIn("Project Root:", stdout)
    
    def test_script_invalid_root_dir(self):
        """Test script with invalid root directory."""
        invalid_dir = self.project_root / "nonexistent"
        
        cmd = [sys.executable, str(self.script_path), "--root-dir", str(invalid_dir)]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        self.assertNotEqual(result.returncode, 0)
        # Check for any error message (not just the word "error")
        self.assertTrue(len(result.stdout) > 0 or len(result.stderr) > 0)
    
    def test_script_missing_root_dir_argument(self):
        """Test script without root directory argument (should succeed if run in a valid project root)."""
        # Create a minimal valid project root
        self.create_test_file("specifications.txt", "Test content")
        cmd = [sys.executable, str(self.script_path)]
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=self.project_root
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn("Project Stage:", result.stdout)

    def test_script_invalid_cwd(self):
        """Test script run in an invalid/empty directory (should fail)."""
        import tempfile, shutil, os
        with tempfile.TemporaryDirectory() as tmpdir:
            cwd = os.getcwd()
            os.chdir(tmpdir)
            try:
                cmd = [sys.executable, str(self.script_path)]
                result = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertTrue("Not a SpecFirst project" in result.stdout or "Not a SpecFirst project" in result.stderr)
            finally:
                os.chdir(cwd)
    
    def test_script_help_output(self):
        """Test script help output."""
        cmd = [sys.executable, str(self.script_path), "--help"]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        self.assertEqual(result.returncode, 0)
        self.assertIn("usage", result.stdout.lower())
        self.assertIn("--root-dir", result.stdout)
    
    def test_script_with_malformed_specifications(self):
        """Test script with malformed SPECIFICATIONS.md."""
        self.create_test_file("SPECIFICATIONS.md", "Invalid content without proper structure")
        
        returncode, stdout, stderr = self.run_script()
        
        # Should still run without crashing
        self.assertEqual(returncode, 0)
        self.assertIn("Project Stage:", stdout)
    
    def test_script_exit_codes(self):
        """Test script exit codes for different scenarios."""
        # Stage 1 (no specs) - should exit 1
        returncode, stdout, stderr = self.run_script()
        self.assertEqual(returncode, 1)
        
        # Stage 6 (complete) - should exit 0
        self.create_test_file("SPECIFICATIONS.md", """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Test Project

## Implementation Requirements

### Framework Scripts
The framework includes essential scripts in the `scripts/` directory:
- `check_docs.py`: Documentation validation tool
  * Validates documentation structure
  * Checks required files
  * Verifies cross-references
  * Ensures documentation standards
  * Maintains documentation quality

#### Documentation Synchronization Paths
- methodology/AGILE_SPECFIRST.md
- methodology/VIBE_USER_GUIDE.md

### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
""")
        self.create_test_file("README.md", "Test content")
        self.create_test_file(".cursorrules", "Test content")
        self.create_test_file("docs/README.md", "Test content")
        self.create_test_file("scripts/check_docs.py", "Test content")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        
        returncode, stdout, stderr = self.run_script()
        self.assertEqual(returncode, 0)

if __name__ == '__main__':
    unittest.main() 