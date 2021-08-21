import unittest
import cencry_encryption

class TestSum(unittest.TestCase):

    def test_encryption1(self):
        test_input = "2\nbaax\naaa"
        cencry_encryption.get_input(test_input)
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 3)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()