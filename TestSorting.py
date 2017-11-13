import unittest
class TestSorting(unittest.TestCase):
    """Tests for is is_sorted."""

    def test_empty(self):
        """Test an empty list."""
        argument = is_sorted([])
        expected = True
        self.assertEqual(expected, argument, "The list is empty.")

    def test_running_one_item(self):
        """Test a one-item list."""
        argument = is_sorted([5])
        expected = True
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_running_two_items(self):
        """Test a two-item list."""
        argument = is_sorted([2, 5])
        expected = True
        self.assertEqual(expected, argument, "The list contains two items.")

    def test_duplicate_items(self):
        """Tests duplicate items in list."""
        argument = is_sorted([2, 3, 3, 5])
        expected = True
        self.assertEqual(expected, argument, "The list has duplicate values.")

    def test_not_sorted_list(self):
        """Tests items in an unsorted list."""
        argument = is_sorted([3, 2, 5])
        expected = False
        self.assertEqual(expected, argument, "The list is unsorted.")

unittest.main()
