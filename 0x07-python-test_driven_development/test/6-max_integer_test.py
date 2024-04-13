import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function.
    """
    def test_empty_list(self):
        """
        Test case for an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        """
        Test case for lists with positive integers.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_negative_integers(self):
        """
        Test case for lists with negative integers.
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)

    def test_mixed_integers(self):
        """
        Test case for lists with mixed positive and negative integers.
        """
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([4, -3, 2, -1]), 4)

    def test_one_element(self):
        """
        Test case for lists with only one element.
        """
        self.assertEqual(max_integer([5]), 5)

    def test_duplicate_values(self):
        """
        Test case for lists with duplicate values.
        """
        self.assertEqual(max_integer([1, 2, 3, 3, 3, 2, 1]), 3)

    def test_non_integer_input(self):
        """
        Test case for input that is not a list of integers.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "4"])
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, (4, 5)])

if __name__ == '__main__':
    unittest.main()
