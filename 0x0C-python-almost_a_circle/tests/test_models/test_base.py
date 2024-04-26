import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_auto_id(self):
        """Test that IDs are automatically assigned correctly."""
        Base._Base__nb_objects = 0  # Reset object count for consistent testing
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_manual_id(self):
        """Test that manually assigned IDs are saved correctly."""
        b3 = Base(89)
        self.assertEqual(b3.id, 89)

    def test_to_json_string_none(self):
        """Test JSON string representation of None."""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_to_json_string_empty(self):
        """Test JSON string representation of an empty list."""
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")

    def test_to_json_string_list(self):
        """Test JSON string representation of a list of dictionaries."""
        json_str = Base.to_json_string([{'id': 12}])
        self.assertIn('{"id": 12}', json_str)

    def test_from_json_string_empty(self):
        """Test conversion of JSON string '[]' to list."""
        result = Base.from_json_string("[]")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty(self):
        """Test conversion of JSON string with data to list."""
        result = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(result, [{'id': 89}])

# Add more tests for Rectangle and Square based on their specific methods and attributes.

if __name__ == '__main__':
    unittest.main()

