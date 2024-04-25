#!/usr/bin/python3
"""Unit tests for the Base class.

Tests the functionality of the Base class including the correct assignment of
automatic ids and the JSON string conversion functionalities.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """Tests the functionality of the Base class."""
    
    def test_auto_id_assignment(self):
        """Test automatic id assignment increments properly."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_manual_id_assignment(self):
        """Test manual id assignment works correctly."""
        b3 = Base(10)
        self.assertEqual(b3.id, 10)

    def test_json_string_conversion(self):
        """Test JSON string conversion handles empty list correctly."""
        self.assertEqual(Base.to_json_string([]), "[]")

if __name__ == "__main__":
    unittest.main()
