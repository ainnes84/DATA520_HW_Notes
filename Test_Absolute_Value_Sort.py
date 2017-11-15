import unittest
import average as avg
 
class TestAverage(unittest.TestCase):
    """Tests for average."""
 
    def test_contains_none(self):
        """Test a list of values that contains None."""
        argument = avg.average([25,30,None,35])
        expected = 30
        self.assertEqual(expected, argument, "The list of values contains None.")
 
    def test_dups(self):
        """Test a list with duplicates."""
        argument = avg.average([25,38,25,30,30])
        expected = 29.6
        self.assertEqual(expected, argument, "The list has duplicates.")
 
    def test_one_item(self):
        """Test a list that contains one item."""
        argument = avg.average([25])
        expected = 25
        self.assertEqual(expected, argument, "The list has one item.")
   
    def test_empty_list(self):
        """Test an empty list."""
        argument = avg.average([])
        expected = None
        self.assertEqual(expected, argument, "The list has no items.")
 
    def test_normal_with_none(self):
        """Test a list that only contains None."""
        argument = avg.average([None])
        expected = None
        self.assertEqual(expected, argument, "The list contains only missing values.")
 
unittest.main()
