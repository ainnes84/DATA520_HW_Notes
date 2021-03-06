import unittest
import average as avg
class test_average(unittest.TestCase):
    """Tests for average."""

    def test_empty(self):
        """Test an empty list."""
        argument = []
        expected = []
        avg.average(argument)
        self.assertEqual(expected, argument, "The list is empty.")

    def test_one_item(self):
        """Test a list with one item."""
        argument = [20]
        expected = [20]
        avg.average(argument)
        self.assertEqual(expected, argument, "The list has one item")

    def test_one(self):
        """Test a list with 'None'."""
        argument = None
        expected = None
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list has one 'None'.")

    def test_normal(self):
        """Test a list with multiple numbers."""
        argument = [20, 30]
        expected = 25.0
        argument = avg.average(argument)
        self.assertEqual(expected, argument, "The list has multiple numbers.")

    def test_normal_none(self):
        """Test a list with multiple numbers and 'None'."""
        argument = [None, 20, 30]
        expected = 25.0
        avg.average(argument)
        self.assertEqual(expected, argument, "The list has multiple numbers and one 'None'.")

unittest.main()
        
