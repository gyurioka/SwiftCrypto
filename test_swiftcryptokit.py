# test_swiftcryptokit.py
"""
Tests for SwiftCryptoKit module.
"""

import unittest
from swiftcryptokit import SwiftCryptoKit

class TestSwiftCryptoKit(unittest.TestCase):
    """Test cases for SwiftCryptoKit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwiftCryptoKit()
        self.assertIsInstance(instance, SwiftCryptoKit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwiftCryptoKit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
