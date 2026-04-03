# test_smartforgeapi.py
"""
Tests for SmartForgeAPI module.
"""

import unittest
from smartforgeapi import SmartForgeAPI

class TestSmartForgeAPI(unittest.TestCase):
    """Test cases for SmartForgeAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SmartForgeAPI()
        self.assertIsInstance(instance, SmartForgeAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SmartForgeAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
