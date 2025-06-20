#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Pytest configuration and common fixtures for scripts tests.
"""

import pytest
import tempfile
import shutil
from pathlib import Path
import sys

# Add script directory to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

@pytest.fixture
def temp_project_dir():
    """Create a temporary project directory for testing."""
    temp_dir = tempfile.mkdtemp()
    project_root = Path(temp_dir)
    
    yield project_root
    
    # Cleanup
    shutil.rmtree(temp_dir)

@pytest.fixture
def sample_specifications_md():
    """Sample SPECIFICATIONS.md content for testing."""
    return """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Test Project Specification

## Project Overview
Test project for validation scripts.

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
     * Overview and navigation guide
     * Directory organization

1. Framework Documentation (/docs/framework/)
   - methodology/
     - AGILE_SPECFIRST.md (REQUIRED)
     - VIBE_USER_GUIDE.md (REQUIRED)
   - best_practices/
     - implementation_guide.md (OPTIONAL)

2. Development Documentation (/docs/development/)
   - setup/
     - README.md (REQUIRED)
   - testing/
     - README.md (REQUIRED)
   - workflow/
     - README.md (REQUIRED)

3. Default Configurations (/docs/defaults/)
   - templates/
     - copyright/
       - project_level.py (REQUIRED)
       - documentation.md (REQUIRED)
     - config/
       - config.json.template (REQUIRED)
   - settings/
     - README.md (REQUIRED)

4. User Documentation (/docs/user/)
   - preferences/
     - README.md (REQUIRED)
   - communication/
     - README.md (REQUIRED)

### Project Artifacts
6. Project Files
   - README.md (REQUIRED)
   - .cursorrules (REQUIRED)
   - SPECIFICATIONS.md (REQUIRED)
"""

@pytest.fixture
def minimal_specifications_md():
    """Minimal SPECIFICATIONS.md content for testing."""
    return """
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

# Minimal Test Project

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
"""

@pytest.fixture
def create_test_project(temp_project_dir, minimal_specifications_md):
    """Create a complete test project structure."""
    def _create_project(complete=True, empty=False):
        if empty:
            # Return truly empty project for Stage 1 testing
            return temp_project_dir
            
        # Create SPECIFICATIONS.md
        specs_file = temp_project_dir / "SPECIFICATIONS.md"
        specs_file.write_text(minimal_specifications_md, encoding='utf-8')
        
        # Create required methodology files
        methodology_dir = temp_project_dir / "methodology"
        methodology_dir.mkdir()
        (methodology_dir / "AGILE_SPECFIRST.md").write_text("Test content", encoding='utf-8')
        (methodology_dir / "VIBE_USER_GUIDE.md").write_text("Test content", encoding='utf-8')
        
        if complete:
            # Create all required files
            (temp_project_dir / "README.md").write_text("Test README", encoding='utf-8')
            (temp_project_dir / ".cursorrules").write_text("Test .cursorrules", encoding='utf-8')
            
            # Create docs structure
            docs_dir = temp_project_dir / "docs"
            docs_dir.mkdir()
            (docs_dir / "README.md").write_text("Docs README", encoding='utf-8')
            
            # Create scripts structure
            scripts_dir = temp_project_dir / "scripts"
            scripts_dir.mkdir()
            (scripts_dir / "check_docs.py").write_text("Test script", encoding='utf-8')
            
            # Create lib directory
            lib_dir = scripts_dir / "lib"
            lib_dir.mkdir()
            (lib_dir / "framework_validator.py").write_text("Test validator", encoding='utf-8')
            (lib_dir / "semantic_parser.py").write_text("Test parser", encoding='utf-8')
        
        return temp_project_dir
    
    return _create_project

@pytest.fixture
def script_paths():
    """Get paths to the main scripts."""
    scripts_dir = Path(__file__).resolve().parent.parent
    return {
        'validate_project': scripts_dir / "validate_project.py",
        'check_docs': scripts_dir / "check_docs.py",
        'check_structure': scripts_dir / "check_structure.py",
        'scripts_dir': scripts_dir
    }

@pytest.fixture
def run_script():
    """Helper function to run scripts with common arguments."""
    def _run_script(script_path, project_root, args=None):
        if args is None:
            args = []
        
        cmd = [sys.executable, str(script_path), "--root-dir", str(project_root)] + args
        
        try:
            import subprocess
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=project_root
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    return _run_script

def pytest_configure(config):
    """Register custom markers to avoid warnings."""
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "e2e: marks tests as end-to-end tests"
    )
    config.addinivalue_line(
        "markers", "slow: marks tests as slow running tests"
    ) 