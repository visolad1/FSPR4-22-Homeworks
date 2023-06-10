import unittest
import hw29

class TestUpperLetter(unittest.TestCase):
    def test_upper_letter(self): 
        test_str = 'mama'
        result = hw29.upper_letter(test_str)
        self.assertEqual(result, 'MAMA')

    def test_upper_letter_1(self): 
        test_str = 100
        result = hw29.upper_letter(test_str)
        self.assertIsInstance(result, AttributeError)

    
unittest.main()

# ====================================================

class TestNumDivision(unittest.TestCase):
    def test_num_division(self): 
        test_num = 10
        result = hw29.num_division(test_num)
        self.assertEqual(result, 5)

    def test_num_division_1(self): 
        test_num = "a"
        result = hw29.num_division(test_num)
        self.assertIsInstance(result, TypeError)

    def test_num_division_2(self): 
        test_num = 6
        result = hw29.num_division(test_num)
        self.assertEqual(result, 2) # self.assertEqual(result, 3)

unittest.main()

# ! Названия тестов