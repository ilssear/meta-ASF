# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)
#
# This file is part of the SpecFirst Development Framework.
# See the LICENSE file for details.

"""
Project-level template for the SpecFirst Development Framework.

This template demonstrates the standard structure for project-level Python files,
including main application entry points, configuration management, and project
initialization.
"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# Import project modules
from config import Config
from utils.logging import setup_logging
from utils.validation import validate_environment


class ProjectManager:
    """
    Main project manager for the SpecFirst Development Framework.
    
    This class handles project initialization, configuration management,
    and coordination of all project components.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the project manager.
        
        Args:
            config_path: Path to configuration file. If None, uses default.
        """
        self.project_root = PROJECT_ROOT
        self.start_time = datetime.now()
        self.config = self._load_config(config_path)
        self.logger = self._setup_logging()
        
        # Validate environment
        self._validate_environment()
        
        # Initialize components
        self._initialize_components()
    
    def _load_config(self, config_path: Optional[str] = None) -> Config:
        """
        Load project configuration.
        
        Args:
            config_path: Path to configuration file.
            
        Returns:
            Loaded configuration object.
            
        Raises:
            FileNotFoundError: If configuration file not found.
            ValueError: If configuration is invalid.
        """
        if config_path is None:
            config_path = self.project_root / "config" / "config.json"
        
        if not Path(config_path).exists():
            raise FileNotFoundError(f"Configuration file not found: {config_path}")
        
        try:
            return Config.from_file(config_path)
        except Exception as e:
            raise ValueError(f"Failed to load configuration: {e}")
    
    def _setup_logging(self) -> logging.Logger:
        """
        Setup project logging.
        
        Returns:
            Configured logger instance.
        """
        logger = logging.getLogger(__name__)
        setup_logging(
            level=self.config.logging.level,
            format=self.config.logging.format,
            handlers=self.config.logging.handlers
        )
        return logger
    
    def _validate_environment(self) -> None:
        """
        Validate the project environment.
        
        Raises:
            RuntimeError: If environment validation fails.
        """
        try:
            validate_environment(self.config)
            self.logger.info("Environment validation passed")
        except Exception as e:
            self.logger.error(f"Environment validation failed: {e}")
            raise RuntimeError(f"Environment validation failed: {e}")
    
    def _initialize_components(self) -> None:
        """
        Initialize project components.
        
        This method initializes all major project components including
        database connections, API endpoints, and background services.
        """
        self.logger.info("Initializing project components...")
        
        # Initialize database
        self._init_database()
        
        # Initialize API
        self._init_api()
        
        # Initialize background services
        self._init_services()
        
        # Initialize monitoring
        self._init_monitoring()
        
        self.logger.info("Project components initialized successfully")
    
    def _init_database(self) -> None:
        """Initialize database connections and migrations."""
        try:
            # Database initialization logic here
            self.logger.info("Database initialized")
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
            raise
    
    def _init_api(self) -> None:
        """Initialize API endpoints and routes."""
        try:
            # API initialization logic here
            self.logger.info("API initialized")
        except Exception as e:
            self.logger.error(f"API initialization failed: {e}")
            raise
    
    def _init_services(self) -> None:
        """Initialize background services and workers."""
        try:
            # Service initialization logic here
            self.logger.info("Background services initialized")
        except Exception as e:
            self.logger.error(f"Service initialization failed: {e}")
            raise
    
    def _init_monitoring(self) -> None:
        """Initialize monitoring and metrics collection."""
        try:
            # Monitoring initialization logic here
            self.logger.info("Monitoring initialized")
        except Exception as e:
            self.logger.error(f"Monitoring initialization failed: {e}")
            raise
    
    def start(self) -> None:
        """
        Start the project and all its components.
        
        This method starts the main application, including the web server,
        background workers, and monitoring services.
        """
        self.logger.info("Starting project...")
        
        try:
            # Start web server
            self._start_web_server()
            
            # Start background workers
            self._start_workers()
            
            # Start monitoring
            self._start_monitoring()
            
            self.logger.info("Project started successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to start project: {e}")
            self.shutdown()
            raise
    
    def _start_web_server(self) -> None:
        """Start the web server."""
        try:
            # Web server startup logic here
            self.logger.info("Web server started")
        except Exception as e:
            self.logger.error(f"Web server startup failed: {e}")
            raise
    
    def _start_workers(self) -> None:
        """Start background workers."""
        try:
            # Worker startup logic here
            self.logger.info("Background workers started")
        except Exception as e:
            self.logger.error(f"Worker startup failed: {e}")
            raise
    
    def _start_monitoring(self) -> None:
        """Start monitoring services."""
        try:
            # Monitoring startup logic here
            self.logger.info("Monitoring services started")
        except Exception as e:
            self.logger.error(f"Monitoring startup failed: {e}")
            raise
    
    def shutdown(self) -> None:
        """
        Shutdown the project and all its components.
        
        This method gracefully shuts down all project components,
        including the web server, background workers, and database connections.
        """
        self.logger.info("Shutting down project...")
        
        try:
            # Shutdown web server
            self._shutdown_web_server()
            
            # Shutdown workers
            self._shutdown_workers()
            
            # Shutdown monitoring
            self._shutdown_monitoring()
            
            # Close database connections
            self._close_database()
            
            self.logger.info("Project shutdown completed")
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
    
    def _shutdown_web_server(self) -> None:
        """Shutdown the web server."""
        try:
            # Web server shutdown logic here
            self.logger.info("Web server shutdown")
        except Exception as e:
            self.logger.error(f"Web server shutdown error: {e}")
    
    def _shutdown_workers(self) -> None:
        """Shutdown background workers."""
        try:
            # Worker shutdown logic here
            self.logger.info("Background workers shutdown")
        except Exception as e:
            self.logger.error(f"Worker shutdown error: {e}")
    
    def _shutdown_monitoring(self) -> None:
        """Shutdown monitoring services."""
        try:
            # Monitoring shutdown logic here
            self.logger.info("Monitoring services shutdown")
        except Exception as e:
            self.logger.error(f"Monitoring shutdown error: {e}")
    
    def _close_database(self) -> None:
        """Close database connections."""
        try:
            # Database connection close logic here
            self.logger.info("Database connections closed")
        except Exception as e:
            self.logger.error(f"Database close error: {e}")
    
    def get_status(self) -> Dict[str, Any]:
        """
        Get the current project status.
        
        Returns:
            Dictionary containing project status information.
        """
        uptime = datetime.now() - self.start_time
        
        return {
            "status": "running",
            "uptime": str(uptime),
            "start_time": self.start_time.isoformat(),
            "config": self.config.to_dict(),
            "version": "1.0.0"
        }


def main() -> None:
    """
    Main entry point for the project.
    
    This function initializes and starts the project manager,
    handling command line arguments and graceful shutdown.
    """
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="SpecFirst Development Framework")
    parser.add_argument(
        "--config",
        help="Path to configuration file",
        default=None
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug mode"
    )
    
    args = parser.parse_args()
    
    # Create and start project manager
    project_manager = None
    
    try:
        project_manager = ProjectManager(config_path=args.config)
        project_manager.start()
        
        # Keep the application running
        import time
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        if project_manager:
            project_manager.shutdown()


if __name__ == "__main__":
    main() 