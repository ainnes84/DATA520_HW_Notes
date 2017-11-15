import unittest
import absolute_value_sort as abs_val
class TestAbsoluteValueSort(unittest.TestCase):
    """Tests for absolute_value_sort"""

    def test_abs_val_empty(self):
        """Test an empty list"""
        argument = []
        expected = []
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_abs_val_one_item(self):
        """Test one-item list."""
        argument = [5]
        expected = [5]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contains one item.")

    def test_abs_val_two_items(self):
        """Test a two-item list."""
        argument = [2, 5]
        expected = [2, 5]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_abs_val_multi_zeros(self):
        """Test a list of zeros."""
        argument = [0, 0, 0, 0]
        expected = [0, 0, 0, 0]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_abs_val_multi_neg(self):
        """Test a list of negative values."""
        argument = [-1, -5, -3, -4]
        expected = [-1, -3, -4, -5]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contains only negative values.")

    def test_abs_val_multi_pos(self):
        """Test a list of positive values."""
        argument = [4, 2, 3, 6]
        expected = [2, 3, 4, 6]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contians only positive values.""")

    def test_abs_val_multi_mix(self):
        """Test a list containing mixture of negative values, zeros, and positive values."""
        argument = [4, 0, 2, -5, 0]
        expected = [0, 0, 2, 4, -5]
        abs_val.absolute_value_sort(argument)
        self.assertEqual(expected, argument, "The list contains a mixture of negative values, zeros, and positive values.")
        
unittest.main()

