#!/usr/bin/env python3
"""
Deployment Package Creator

Creates a deployment package containing only generated files from a SpecFirst project.
The package includes docs/, README.md, .cursorrules, and LICENSE files.

Usage:
    python deploy_package.py [--root-dir PROJECT_ROOT] [--package-name NAME] [--verbose]

Examples:
    # Create deployment package from current directory
    python deploy_package.py

    # Create deployment package from specific directory
    python deploy_package.py --root-dir /path/to/project

    # Create deployment package with custom name
    python deploy_package.py --package-name my_project_deployment

    # Create deployment package with verbose output
    python deploy_package.py --verbose
"""

import argparse
import logging
import shutil
import sys
import zipfile
from pathlib import Path
from typing import List, Dict, Any


class DeployPackage:
    """
    Creates deployment packages containing only generated files from SpecFirst projects.
    
    Generated files include:
    - docs/ directory (all generated documentation)
    - README.md (generated from specifications)
    - .cursorrules (generated from specifications)
    - LICENSE (GPL 3.0 from defaults/gpl-3.0.txt)
    """

    def __init__(self, project_root: Path, package_name: str = None):
        """
        Initialize the deployment package creator.
        
        Args:
            project_root: Path to the project root directory
            package_name: Custom name for the deployment package (optional)
        """
        self.project_root = Path(project_root).resolve()
        self.package_name = package_name or f"{self.project_root.name}_deployment"
        
        # Set up logging
        self.logger = logging.getLogger(__name__)
        
        # Validate project root exists
        if not self.project_root.exists():
            raise FileNotFoundError(f"Project root does not exist: {self.project_root}")
        
        if not self.project_root.is_dir():
            raise NotADirectoryError(f"Project root is not a directory: {self.project_root}")

    def get_generated_files(self) -> List[str]:
        """
        Get list of files and directories that are considered generated.
        
        Returns:
            List of file/directory paths relative to project root
        """
        generated_files = [
            "docs/",
            "README.md",
            ".cursorrules",
            "LICENSE"
        ]
        
        self.logger.debug(f"Generated files: {generated_files}")
        return generated_files

    def validate_files_exist(self) -> None:
        """
        Validate that all required generated files exist.
        
        Raises:
            FileNotFoundError: If any required file is missing
        """
        missing_files = []
        
        for file_path in self.get_generated_files():
            full_path = self.project_root / file_path.rstrip('/')
            
            if not full_path.exists():
                missing_files.append(file_path)
        
        if missing_files:
            raise FileNotFoundError(
                f"Missing required files: {', '.join(missing_files)}"
            )
        
        self.logger.info("All required files validated successfully")

    def create_package_directory(self) -> Path:
        """
        Create temporary package directory.
        
        Returns:
            Path to the created package directory
        """
        package_dir = self.project_root / self.package_name
        
        if package_dir.exists():
            shutil.rmtree(package_dir)
        
        package_dir.mkdir()
        self.logger.debug(f"Created package directory: {package_dir}")
        
        return package_dir

    def copy_files_to_package(self, package_dir: Path) -> None:
        """
        Copy generated files to package directory.
        
        Args:
            package_dir: Path to the package directory
        """
        for file_path in self.get_generated_files():
            source_path = self.project_root / file_path.rstrip('/')
            dest_path = package_dir / file_path.rstrip('/')
            
            if source_path.is_dir():
                shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
                self.logger.debug(f"Copied directory: {file_path}")
            else:
                shutil.copy2(source_path, dest_path)
                self.logger.debug(f"Copied file: {file_path}")

    def create_zip_archive(self, package_dir: Path) -> Path:
        """
        Create zip archive from package directory.
        
        Args:
            package_dir: Path to the package directory
            
        Returns:
            Path to the created zip file
        """
        zip_path = self.project_root / f"{self.package_name}.zip"
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for item in package_dir.rglob('*'):
                if item.is_file():
                    arc_name = item.relative_to(package_dir)
                    zip_file.write(item, arc_name)
                    self.logger.debug(f"Added to zip: {arc_name}")
        
        self.logger.info(f"Created zip archive: {zip_path}")
        return zip_path

    def cleanup_package_directory(self, package_dir: Path) -> None:
        """
        Clean up temporary package directory.
        
        Args:
            package_dir: Path to the package directory to remove
        """
        if package_dir.exists():
            shutil.rmtree(package_dir)
            self.logger.debug(f"Cleaned up package directory: {package_dir}")

    def get_package_info(self) -> Dict[str, Any]:
        """
        Get information about the deployment package.
        
        Returns:
            Dictionary containing package information
        """
        generated_files = self.get_generated_files()
        total_size = 0
        
        for file_path in generated_files:
            full_path = self.project_root / file_path.rstrip('/')
            if full_path.exists():
                if full_path.is_file():
                    total_size += full_path.stat().st_size
                else:
                    for item in full_path.rglob('*'):
                        if item.is_file():
                            total_size += item.stat().st_size
        
        return {
            "project_root": str(self.project_root),
            "package_name": self.package_name,
            "generated_files": generated_files,
            "total_size": total_size
        }

    def validate_package_contents(self, zip_path: Path) -> None:
        """
        Validate the contents of the created zip file.
        
        Args:
            zip_path: Path to the zip file to validate
            
        Raises:
            zipfile.BadZipFile: If the zip file is corrupted
        """
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            file_list = zip_file.namelist()
            
            # Check that all generated files are present
            expected_files = [f.rstrip('/') for f in self.get_generated_files()]
            
            for expected_file in expected_files:
                if expected_file not in file_list:
                    # For directories, check if any files from that directory are present
                    if expected_file.endswith('/') or expected_file == "docs":
                        dir_files = [f for f in file_list if f.startswith(expected_file)]
                        if not dir_files:
                            raise ValueError(f"Missing directory contents: {expected_file}")
                    else:
                        raise ValueError(f"Missing file: {expected_file}")
        
        self.logger.info("Package contents validated successfully")

    def create_package(self, verbose: bool = False) -> Path:
        """
        Create the complete deployment package.
        
        Args:
            verbose: Enable verbose output
            
        Returns:
            Path to the created zip file
            
        Raises:
            FileNotFoundError: If required files are missing
        """
        if verbose:
            logging.basicConfig(level=logging.INFO)
            self.logger.info("Starting deployment package creation...")
        
        # Validate files exist
        self.validate_files_exist()
        
        # Create package directory
        package_dir = self.create_package_directory()
        
        try:
            # Copy files to package
            self.copy_files_to_package(package_dir)
            
            # Create zip archive
            zip_path = self.create_zip_archive(package_dir)
            
            # Validate package contents
            self.validate_package_contents(zip_path)
            
            if verbose:
                info = self.get_package_info()
                self.logger.info(f"Package created successfully:")
                self.logger.info(f"  - Package: {zip_path}")
                self.logger.info(f"  - Size: {info['total_size']} bytes")
                self.logger.info(f"  - Files: {len(info['generated_files'])}")
            
            return zip_path
            
        finally:
            # Clean up temporary directory
            self.cleanup_package_directory(package_dir)


def main():
    """Main entry point for the deployment package script."""
    parser = argparse.ArgumentParser(
        description="Create deployment package containing only generated files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deploy_package.py
  python deploy_package.py --root-dir /path/to/project
  python deploy_package.py --package-name my_deployment --verbose
        """
    )
    
    parser.add_argument(
        '--root-dir',
        type=Path,
        default=Path.cwd(),
        help='Project root directory (default: current directory)'
    )
    
    parser.add_argument(
        '--package-name',
        type=str,
        help='Custom name for the deployment package'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Set up logging
    if args.verbose:
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s: %(message)s'
        )
    else:
        logging.basicConfig(
            level=logging.WARNING,
            format='%(levelname)s: %(message)s'
        )
    
    try:
        # Create deployment package
        deploy = DeployPackage(args.root_dir, args.package_name)
        zip_path = deploy.create_package(verbose=args.verbose)
        
        print(f"Deployment package created: {zip_path}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main() 