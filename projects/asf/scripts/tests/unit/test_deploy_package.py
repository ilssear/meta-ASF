"""
Unit tests for deploy_package.py

Tests the deployment package creation functionality.
"""

import os
import tempfile
import shutil
import zipfile
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock
import logging

# Import the module to test
from scripts.deploy_package import DeployPackage


class TestDeployPackage:
    """Test cases for DeployPackage class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.project_root = Path(self.temp_dir) / "test_project"
        self.project_root.mkdir()
        
        # Create minimal project structure
        (self.project_root / "docs").mkdir()
        (self.project_root / "docs" / "README.md").write_text("# Docs README")
        (self.project_root / "defaults").mkdir()
        (self.project_root / "LICENSE").write_text("GPL 3.0 License")
        (self.project_root / "README.md").write_text("# Test Project")
        (self.project_root / ".cursorrules").write_text("# Cursor Rules")
        (self.project_root / "defaults" / "gpl-3.0.txt").write_text("GPL 3.0 License")
        
        self.deploy = DeployPackage(self.project_root)

    def teardown_method(self):
        """Clean up test fixtures."""
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_init_with_valid_project_root(self):
        """Test initialization with valid project root."""
        assert self.deploy.project_root == self.project_root
        assert self.deploy.package_name == "test_project_deployment"

    def test_init_with_custom_package_name(self):
        """Test initialization with custom package name."""
        deploy = DeployPackage(self.project_root, package_name="custom_name")
        assert deploy.package_name == "custom_name"

    def test_get_generated_files(self):
        """Test getting list of generated files."""
        files = self.deploy.get_generated_files()
        
        # Should include core generated files
        assert "docs/" in files
        assert "README.md" in files
        assert ".cursorrules" in files
        assert "LICENSE" in files
        
        # Should not include source files
        assert "SPECIFICATIONS.md" not in files
        assert "specifications.txt" not in files
        assert "scripts/" not in files

    def test_validate_files_exist(self):
        """Test validation that required files exist."""
        # Should not raise exception when files exist
        self.deploy.validate_files_exist()

    def test_validate_files_exist_missing_file(self):
        """Test validation fails when required file is missing."""
        # Remove a required file
        (self.project_root / "README.md").unlink()
        
        with pytest.raises(FileNotFoundError, match="Missing required files: README.md"):
            self.deploy.validate_files_exist()

    def test_create_package_directory(self):
        """Test creating package directory."""
        package_dir = self.deploy.create_package_directory()
        
        assert package_dir.exists()
        assert package_dir.is_dir()
        assert package_dir.name == "test_project_deployment"

    def test_copy_files_to_package(self):
        """Test copying files to package directory."""
        package_dir = self.deploy.create_package_directory()
        self.deploy.copy_files_to_package(package_dir)
        
        # Check that files were copied
        assert (package_dir / "docs").exists()
        assert (package_dir / "README.md").exists()
        assert (package_dir / ".cursorrules").exists()
        assert (package_dir / "LICENSE").exists()

    def test_create_zip_archive(self):
        """Test creating zip archive."""
        package_dir = self.deploy.create_package_directory()
        self.deploy.copy_files_to_package(package_dir)
        
        zip_path = self.deploy.create_zip_archive(package_dir)
        
        assert zip_path.exists()
        assert zip_path.suffix == ".zip"
        
        # Verify zip contents
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            file_list = zip_file.namelist()
            assert "docs/" in file_list or any(f.startswith("docs/") for f in file_list)
            assert "README.md" in file_list
            assert ".cursorrules" in file_list
            assert "LICENSE" in file_list

    def test_cleanup_package_directory(self):
        """Test cleaning up package directory."""
        package_dir = self.deploy.create_package_directory()
        self.deploy.cleanup_package_directory(package_dir)
        
        assert not package_dir.exists()

    def test_create_package_success(self):
        """Test successful package creation."""
        zip_path = self.deploy.create_package()
        
        assert zip_path.exists()
        assert zip_path.suffix == ".zip"
        assert zip_path.name == "test_project_deployment.zip"

    def test_create_package_with_verbose_output(self, caplog):
        """Test package creation with verbose output."""
        with caplog.at_level("INFO"):
            self.deploy.create_package(verbose=True)
        # Should log progress messages
        assert any("deployment package creation" in m.lower() or "package created successfully" in m.lower() for m in caplog.text.splitlines())

    def test_create_package_missing_files(self):
        """Test package creation fails when files are missing."""
        # Remove required file
        (self.project_root / "README.md").unlink()
        
        with pytest.raises(FileNotFoundError):
            self.deploy.create_package()

    def test_get_package_info(self):
        """Test getting package information."""
        info = self.deploy.get_package_info()
        
        assert "project_root" in info
        assert "package_name" in info
        assert "generated_files" in info
        assert "total_size" in info

    def test_validate_package_contents(self):
        """Test validating package contents."""
        zip_path = self.deploy.create_package()
        
        # Should not raise exception for valid package
        self.deploy.validate_package_contents(zip_path)

    def test_validate_package_contents_invalid_zip(self):
        """Test validation fails for invalid zip file."""
        invalid_zip = self.project_root / "invalid.zip"
        invalid_zip.write_text("not a zip file")
        
        with pytest.raises(zipfile.BadZipFile):
            self.deploy.validate_package_contents(invalid_zip)


class TestDeployPackageIntegration:
    """Integration tests for DeployPackage."""

    def test_full_deployment_workflow(self):
        """Test complete deployment workflow."""
        with tempfile.TemporaryDirectory() as temp_dir:
            project_root = Path(temp_dir) / "test_project"
            project_root.mkdir()
            
            # Create minimal project structure
            (project_root / "docs").mkdir()
            (project_root / "docs" / "README.md").write_text("# Docs README")
            (project_root / "defaults").mkdir()
            (project_root / "LICENSE").write_text("GPL 3.0 License")
            (project_root / "README.md").write_text("# Test Project")
            (project_root / ".cursorrules").write_text("# Cursor Rules")
            (project_root / "defaults" / "gpl-3.0.txt").write_text("GPL 3.0 License")
            
            deploy = DeployPackage(project_root)
            zip_path = deploy.create_package()
            
            # Verify package was created
            assert zip_path.exists()
            assert zip_path.stat().st_size > 0
            
            # Verify package contents
            with zipfile.ZipFile(zip_path, 'r') as zip_file:
                file_list = zip_file.namelist()
                assert "docs/" in file_list or any(f.startswith("docs/") for f in file_list)
                assert "README.md" in file_list
                assert ".cursorrules" in file_list
                assert "LICENSE" in file_list
                
                # Verify file contents
                readme_content = zip_file.read("README.md").decode()
                assert "# Test Project" in readme_content 