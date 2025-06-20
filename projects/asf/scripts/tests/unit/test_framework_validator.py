#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Unit tests for the project validator that handles project stage determination.
"""

import unittest
from pathlib import Path
import tempfile
import sys
import json

# Ensure both lib/ and scripts/ are in sys.path for import flexibility
current_dir = Path(__file__).resolve().parent
scripts_dir = current_dir.parent.parent
lib_dir = scripts_dir / "lib"
sys.path.insert(0, str(lib_dir))
sys.path.insert(0, str(scripts_dir))

from validate_project import ProjectValidator

class TestProjectValidator(unittest.TestCase):
    """Test cases for the project validator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_root = Path(self.temp_dir)
        
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def create_test_file(self, file_path, content=""):
        """Helper to create a test file."""
        full_path = self.project_root / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding='utf-8')
    
    def test_stage_1_no_specifications(self):
        """Test Stage 1: No specifications file."""
        validator = ProjectValidator(str(self.project_root))
        
        # Should raise SystemExit when no specs found
        with self.assertRaises(SystemExit):
            validator.run()
    
    def test_stage_1_specifications_txt_only(self):
        """Test Stage 1: Only specifications.txt exists."""
        self.create_test_file("specifications.txt", "Test content")
        validator = ProjectValidator(str(self.project_root))
        
        # Capture stdout to check output
        import io
        import contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            validator.run()
        output = f.getvalue()
        
        self.assertIn("Stage: 1", output)
        self.assertIn("Ready for Refinement", output)
    
    def test_stage_2_specifications_md_only(self):
        """Test Stage 2: SPECIFICATIONS.md exists but no core structure."""
        # Create the minimal SPECIFICATIONS.md that matches the actual spec
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
        validator = ProjectValidator(str(self.project_root))
        
        # Capture stdout to check output
        import io
        import contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            validator.run()
        output = f.getvalue()
        
        self.assertIn("Stage: 2", output)
        self.assertIn("Ready to Generate", output)
    
    def test_stage_3_core_structure_exists(self):
        """Test Stage 3: Core structure exists but docs incomplete."""
        # Create the minimal SPECIFICATIONS.md that matches the actual spec
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
1. Framework Documentation (/docs/framework/)
   - methodology/
     - AGILE_SPECFIRST.md (REQUIRED)
""")
        # Create core directories but not all required files
        self.create_test_file("docs/README.md", "Test content")
        self.create_test_file("scripts/check_docs.py", "Test content")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        validator = ProjectValidator(str(self.project_root))
        
        # Capture stdout to check output
        import io
        import contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            validator.run()
        output = f.getvalue()
        
        self.assertIn("Stage: 3", output)
        self.assertIn("In Progress", output)
    
    def test_stage_6_complete_and_valid(self):
        """Test Stage 6: Complete and valid with no warnings."""
        # Create the minimal SPECIFICATIONS.md that matches the actual spec
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
        # Create all required files only
        self.create_test_file("README.md", "Test content")
        self.create_test_file(".cursorrules", "Test content")
        self.create_test_file("docs/README.md", "Test content")
        self.create_test_file("scripts/check_docs.py", "Test content")
        # Create required methodology files in the temp directory
        self.create_test_file("methodology/AGILE_SPECFIRST.md", "Test content")
        self.create_test_file("methodology/VIBE_USER_GUIDE.md", "Test content")
        validator = ProjectValidator(str(self.project_root))
        
        # Capture stdout to check output
        import io
        import contextlib
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            validator.run()
        output = f.getvalue()
        
        self.assertIn("Stage: 6", output)
        self.assertIn("Complete and Valid", output)
    
    def test_verbose_output(self):
        """Test verbose output mode."""
        # Create the minimal SPECIFICATIONS.md that matches the actual spec
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
        validator = ProjectValidator(str(self.project_root), verbose=True)
        
        # Capture both stdout and stderr to check output
        import io
        import contextlib
        stdout_f = io.StringIO()
        stderr_f = io.StringIO()
        with contextlib.redirect_stdout(stdout_f), contextlib.redirect_stderr(stderr_f):
            validator.run()
        output = stdout_f.getvalue() + stderr_f.getvalue()
        
        self.assertIn("Stage: 2", output)
        self.assertIn("Project Root:", output)

if __name__ == '__main__':
    unittest.main() 