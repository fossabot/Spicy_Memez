import unittest
import sys
sys.path.insert(0, '..')  # Python directory imports workaround
from src.sub_ints import subtract_ints


class TestAddInts(unittest.TestCase):

    def test_ints(self):
        """Both x,y are small ints"""
        self.assertEqual(subtract_ints(10, 5)[0], 5)
        self.assertEqual(subtract_ints(-5, 5)[0], -10)
        self.assertEqual(subtract_ints(-5, -5)[0], 0)
        self.assertEqual(subtract_ints(0, 0)[0], 0)
        self.assertEqual(subtract_ints(10, 0)[0], 10)
        self.assertEqual(subtract_ints(0, 10)[0], -10)

    def test_other_types(self):
        """Test with floats, complex, ints and errors"""
        self.assertEqual(subtract_ints(10.5, 5.8)[0], 5)
        self.assertIsInstance(subtract_ints("int", 1.2), ValueError)
        self.assertIsInstance(subtract_ints(5j+3, 3.14159265), TypeError)
        self.assertIsInstance(subtract_ints(ValueError, "Hi Mom!"), TypeError)

    def test_type_bounds(self):
        """Testing for largest or smallest int wont do it in python since it has no boundaries on number size but this is added for completion."""
        self.assertAlmostEqual(subtract_ints(2147483647, 2147483647)[0], 0)
        self.assertAlmostEqual(subtract_ints(9223372036854775807, 92233720368547758079223372036854775807)[
                               0], -92233720368547758070000000000000000000)


if __name__ == '__main__':
    unittest.main()
