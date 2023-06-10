import unittest
from game import find_num

class TestFindNum(unittest.TestCase):
    def test_correct_guess(self):
        result = find_num(5, 5)
        self.assertTrue(result)
    
    def test_incorrect_guess(self):
        result = find_num(7, 3)
        self.assertIsNone(result)

    def test_value_error(self):
        result = find_num(5, 'abc')
        self.assertIsInstance(result, ValueError)

if __name__ == "__main__":
    unittest.main()