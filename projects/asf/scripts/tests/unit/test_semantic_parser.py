#!/usr/bin/env python3
# Copyright (c) 2025, Jaime Moraga (jmoraga@mines.edu)

"""
Unit tests for the semantic parser that properly understands SPECIFICATIONS.md structure.
"""

import unittest
from pathlib import Path
import tempfile
import sys

# Add script directory to path for lib imports
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from lib.semantic_parser import SemanticSpecParser, Section, FileSpec, FileStatus

class TestSemanticParser(unittest.TestCase):
    """Test cases for the semantic parser."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.mkdtemp()
        self.specs_file = Path(self.temp_dir) / "SPECIFICATIONS.md"
        
    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def create_test_spec(self, content):
        """Helper to create a test SPECIFICATIONS.md file."""
        self.specs_file.write_text(content, encoding='utf-8')
        return SemanticSpecParser(Path(self.temp_dir))
    
    def test_parse_section_header_basic(self):
        """Test parsing basic section headers."""
        content = """
### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/README.md', sections)
        self.assertEqual(sections['docs/README.md'].status, FileStatus.REQUIRED)
    
    def test_parse_section_header_with_multi_digit_number(self):
        """Test parsing section headers with multi-digit numbers."""
        content = """
### Documentation Generation
000. Documentation Overview (/docs/)
   - README.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/README.md', sections)
        self.assertEqual(sections['docs/README.md'].status, FileStatus.REQUIRED)
    
    def test_parse_nested_structure(self):
        """Test parsing nested directory structure."""
        content = """
### Documentation Generation
1. Framework Documentation (/docs/framework/)
   - methodology/
     - AGILE_SPECFIRST.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/framework/methodology/AGILE_SPECFIRST.md', sections)
        self.assertEqual(sections['docs/framework/methodology/AGILE_SPECFIRST.md'].status, FileStatus.REQUIRED)
    
    def test_parse_multiple_sections(self):
        """Test parsing multiple sections."""
        content = """
### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
1. Framework Documentation (/docs/framework/)
   - methodology/
     - AGILE_SPECFIRST.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/README.md', sections)
        self.assertIn('docs/framework/methodology/AGILE_SPECFIRST.md', sections)
    
    def test_parse_optional_files(self):
        """Test parsing optional files."""
        content = """
### Documentation Generation
1. Framework Documentation (/docs/framework/)
   - best_practices/
     - specification_guide.md (OPTIONAL)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/framework/best_practices/specification_guide.md', sections)
        self.assertEqual(sections['docs/framework/best_practices/specification_guide.md'].status, FileStatus.OPTIONAL)
    
    def test_parse_with_descriptions(self):
        """Test parsing ignores description lines."""
        content = """
### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
     * Overview and navigation guide
     * Directory organization
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/README.md', sections)
        # Should not create any files for description lines
    
    def test_parse_complex_structure(self):
        """Test parsing complex nested structure."""
        content = """
### Documentation Generation
4. Default Configurations (/docs/defaults/)
   - templates/
     - copyright/
       - project_level.py (REQUIRED)
       - documentation.md (REQUIRED)
     - config/
       - config.json.template (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/defaults/templates/copyright/project_level.py', sections)
        self.assertIn('docs/defaults/templates/copyright/documentation.md', sections)
        self.assertIn('docs/defaults/templates/config/config.json.template', sections)
    
    def test_parse_invalid_section_ignored(self):
        """Test that invalid sections are ignored."""
        content = """
### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md (REQUIRED)
Invalid section without number
   - some_file.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertIn('docs/README.md', sections)
        self.assertNotIn('docs/some_file.md', sections)
    
    def test_parse_empty_specifications(self):
        """Test parsing empty specifications file."""
        content = ""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        self.assertEqual(len(sections), 0)
    
    def test_parse_missing_specifications_file(self):
        """Test handling missing SPECIFICATIONS.md file."""
        parser = SemanticSpecParser(Path(self.temp_dir))
        sections = parser.parse_documentation_files()
        
        self.assertEqual(len(sections), 0)
    
    def test_parse_malformed_section_header(self):
        """Test parsing malformed section headers."""
        content = """
### Documentation Generation
Invalid section header
   - README.md (REQUIRED)
1. Valid Section (/docs/)
   - README.md (REQUIRED)
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        # Should only parse the valid section
        self.assertIn('docs/README.md', sections)
        self.assertEqual(len(sections), 1)
    
    def test_parse_file_without_status(self):
        """Test parsing files without explicit status (should be ignored by parser)."""
        content = """
### Documentation Generation
0. Documentation Overview (/docs/)
   - README.md
"""
        parser = self.create_test_spec(content)
        sections = parser.parse_documentation_files()
        
        # Files without explicit status should not be parsed
        self.assertNotIn('docs/README.md', sections)
        self.assertEqual(len(sections), 0)

if __name__ == '__main__':
    unittest.main() 