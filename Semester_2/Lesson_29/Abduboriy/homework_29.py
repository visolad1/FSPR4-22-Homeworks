from random_num import find_num
import unittest
import random

class TestFindNum(unittest.TestCase):
    def test_correct_guess(self):
        x = random.randint(1, 10)
        result = find_num(x, x)
        self.assertTrue(result)

    def test_incorrect_guess(self):
        x = random.randint(1, 10)
        result = find_num(x, x + 1)
        self.assertFalse(result)

    def test_guess_out_of_range(self):
        x = random.randint(1, 10)
        result = find_num(x, 11)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()


# ! class TestFindNum(unittest.TestCase):
# !     def test_correct_guess(self):
# !         result = find_num(5, 'abc')
# !         self.assertTrue(result)



# ! unittest.main()