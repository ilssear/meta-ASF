#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
End-to-end tests for the complete SpecFirst workflow.
"""

import pytest
import subprocess
import sys
from pathlib import Path

@pytest.mark.e2e
class TestFullWorkflow:
    """End-to-end tests for the complete workflow."""
    
    def test_complete_project_lifecycle(self, create_test_project, script_paths, run_script):
        """Test the complete project lifecycle from Stage 1 to Stage 6."""
        # Start with empty project (Stage 1)
        project_root = create_test_project(complete=False, empty=True)
        
        # Test Stage 1
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 1  # Should exit with error for no specs
        assert "Not a SpecFirst project" in stdout
        
        # Add specifications.txt (Stage 1)
        (project_root / "specifications.txt").write_text("Test content", encoding='utf-8')
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 1" in stdout
        assert "Ready for Refinement" in stdout
        
        # Add SPECIFICATIONS.md (Stage 2)
        specs_content = """
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
"""
        (project_root / "SPECIFICATIONS.md").write_text(specs_content, encoding='utf-8')
        
        # Create required methodology files
        (project_root / "methodology").mkdir()
        (project_root / "methodology" / "AGILE_SPECFIRST.md").write_text("Test content", encoding='utf-8')
        (project_root / "methodology" / "VIBE_USER_GUIDE.md").write_text("Test content", encoding='utf-8')
        
        # Test Stage 2
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 2" in stdout
        assert "Ready to Generate" in stdout
        
        # Add core structure (Stage 3)
        (project_root / "docs").mkdir()
        (project_root / "scripts").mkdir()
        (project_root / "scripts" / "check_docs.py").write_text("Test script", encoding='utf-8')
        
        # Test Stage 3
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 3" in stdout
        assert "In Progress" in stdout
        
        # Add all required files (Stage 4)
        (project_root / "docs" / "README.md").write_text("Test content", encoding='utf-8')
        (project_root / "docs" / "framework").mkdir(parents=True)
        (project_root / "docs" / "framework" / "methodology").mkdir(parents=True)
        (project_root / "docs" / "framework" / "methodology" / "AGILE_SPECFIRST.md").write_text("Test content", encoding='utf-8')
        
        # Test Stage 4
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 4" in stdout
        assert "Ready for Finalization" in stdout
        
        # Add final artifacts (Stage 6)
        (project_root / "README.md").write_text("Test content", encoding='utf-8')
        (project_root / ".cursorrules").write_text("Test content", encoding='utf-8')
        
        # Test Stage 6
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 6" in stdout
        assert "Complete and Valid" in stdout
    
    def test_scripts_workflow_integration(self, create_test_project, script_paths, run_script):
        """Test that all scripts work together in a workflow."""
        # Create complete project
        project_root = create_test_project(complete=True)
        
        # Test validate_project.py
        returncode, stdout, stderr = run_script(script_paths['validate_project'], project_root)
        assert returncode == 0
        assert "Project Stage: 6" in stdout
        
        # Test check_docs.py
        returncode, stdout, stderr = run_script(script_paths['check_docs'], project_root)
        assert returncode == 0
        # Should report no missing files for complete project
        
        # Test check_structure.py
        returncode, stdout, stderr = run_script(script_paths['check_structure'], project_root)
        assert returncode == 0
        assert "Project structure is VALID" in stdout
    
    def test_error_handling_workflow(self, temp_project_dir, script_paths, run_script):
        """Test error handling across all scripts."""
        # Test with non-existent directory
        invalid_dir = temp_project_dir / "nonexistent"
        
        for script_name, script_path in script_paths.items():
            if script_name == 'scripts_dir':
                continue
                
            returncode, stdout, stderr = run_script(script_path, invalid_dir)
            assert returncode != 0
            # Check for any error message output
            assert len(stdout) > 0 or len(stderr) > 0
    
    def test_verbose_output_workflow(self, create_test_project, script_paths, run_script):
        """Test verbose output across all scripts."""
        project_root = create_test_project(complete=True)
        
        # Only test scripts that support -v flag
        scripts_with_verbose = ['validate_project', 'check_docs']
        
        for script_name in scripts_with_verbose:
            script_path = script_paths[script_name]
            returncode, stdout, stderr = run_script(script_path, project_root, ["-v"])
            print(f"\n=== {script_name} ===")
            print(f"Return code: {returncode}")
            print(f"Stdout: {stdout}")
            print(f"Stderr: {stderr}")
            assert returncode == 0
            # Should provide more detailed output in verbose mode
    
    def test_help_output_workflow(self, script_paths):
        """Test help output for all scripts."""
        for script_name, script_path in script_paths.items():
            if script_name == 'scripts_dir':
                continue
                
            cmd = [sys.executable, str(script_path), "--help"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            assert result.returncode == 0
            assert "usage" in result.stdout.lower()
            assert "--root-dir" in result.stdout 