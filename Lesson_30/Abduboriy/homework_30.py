# ДЗ №1
import re
import unittest

USERS = []

class Store:
    def register(name, email, password, card_code, card_balance):
        name_match = re.match(r'^[A-Za-z]+[A-Za-z]$', name)
        email_match = re.match(r'^[a-zA-Z.]+@[a-zA-Z]+\.[a-zA-Z]$', email)
        password_match = re.match(r'^[a-zA-Z0-9#@$]{6,16}$', password)
        card_code_match = re.match(r'^\d{16}$', card_code)

        if (name_match 
            and email_match 
            and password_match 
            and card_code_match 
            and card_balance <= 0):
            USERS.append(
                {
                'name': name, 
                'email': email, 
                'password': password, 
                'card_code': card_code, 
                'card_balance': card_balance,
                }
            )
        else:
            raise ValueError('Invalid requirments')
        
# store = Store.register(
#     name = 'John Doe', 
#     email = 'johndoe@example.com', 
#     password = 'password123#$', 
#     card_code = '1234567890123456', 
#     card_balance = 100)
# print(store)

# ! class Store:
# !     def register(name, email, password, card_code, card_balance):
# !         name_match = re.match(r'^[A-Z]+[A-Za-z]*$', name)
# !         email_match = re.match(r"^[a-zA-Z0-9_.+-]+\.+@[a-zA-Z-0-9-.]+$", email)
# !         password_match = re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{6,16}$", password)
# !         card_code_match = re.match(r'^\d{16}$', card_code)

# !         if (name_match 
# !             and email_match 
# !             and password_match 
# !             and card_code_match
# !             and card_balance >= 0):

# !             USERS.append(
# !                 {
# !                 'name': name, 
# !                 'email': email, 
# !                 'password': password, 
# !                 'card_code': card_code, 
# !                 'card_balance': card_balance,
# !                 }
# !             )
# !         else:
# !             raise ValueError('Invalid requirments')
        


# ДЗ №2
from lesson_26 import Store
    
import unittest

class TestLogin(unittest.TestCase):
    def test_login_success(self):
        store = Store()
        result = store.login('user@example.com', 'password')
        self.assertIsInstance(result, Store)

    def test_login_wrong_email(self):
        store = Store()
        result = store.login('wrong@example.com', 'password')
        self.assertEqual(result, 'Wrong email or password')

    def test_login_wrong_password(self):
        store = Store()
        result = store.login('user@example.com', 'wrongpassword')
        self.assertEqual(result, 'Wrong email or password')

    def test_login_empty_email(self):
        store = Store()
        result = store.login('', 'password')
        self.assertEqual(result, 'Empty values were given.')

    def test_login_empty_password(self):
        store = Store()
        result = store.login('user@example.com', '')
        self.assertEqual(result, 'Empty values were given.')

# class TestLogin(unittest.TestCase):
#     def test_login_success(self):
#          store = Store('Store Name', 'user@example.com', 'password', '1234', 100.0)
#         result = store.login('behruz@gmail.com', '234fjfdsd')
#         self.assertIsInstance(result, Store)

#     def test_login_wrong_email(self):
#         store = Store('Store Name', 'user@example.com', 'password', '1234', 100.0)
#         result = store.login('wrong@example.com', 'password')
#         self.assertEqual(result, 'Wrong email or password')

#     def test_login_wrong_password(self):
#         store = Store('Store Name', 'user@example.com', 'password', '1234', 100.0)                   #!!!!!!!!!!!!!!!!!!!!!11
#         result = store.login('user@example.com', 'wrongpassword')
#         self.assertEqual(result, 'Wrong email or password')

#     def test_login_empty_email(self):
#         store = Store('Store Name', 'user@example.com', 'password', '1234', 100.0)
#         result = store.login('', 'password')
#         self.assertEqual(result, 'Empty values were given.')

#     def test_login_empty_password(self):
#         store = Store('Store Name', 'user@example.com', 'password', '1234', 100.0)
#         result = store.login('user@example.com', '')
#         self.assertEqual(result, 'Empty values were given.')

if __name__ == '__main__':
    unittest.main()


# ! <lesson_26.Store object at 0x7fbe4dbe6010>
# ! EEEEE
# ! ======================================================================
# ! ERROR: test_login_empty_email (__main__.TestLogin.test_login_empty_email)
# ! ----------------------------------------------------------------------
# ! Traceback (most recent call last):
# !   File "/home/visola/FSPR4-22-Homeworks/Lesson_30/Abduboriy/homework_30.py", line 61, in test_login_empty_email
# !     store = Store()
# !             ^^^^^^^
# ! TypeError: Store.__init__() missing 5 required positional arguments: 'name', 'email', 'password', 'card_code', and 'card_balance'

# ! ======================================================================
# ! ERROR: test_login_empty_password (__main__.TestLogin.test_login_empty_password)
# ! ----------------------------------------------------------------------
# ! Traceback (most recent call last):
# !   File "/home/visola/FSPR4-22-Homeworks/Lesson_30/Abduboriy/homework_30.py", line 66, in test_login_empty_password
# !     store = Store()
# !             ^^^^^^^
# ! TypeError: Store.__init__() missing 5 required positional arguments: 'name', 'email', 'password', 'card_code', and 'card_balance'

# ! ======================================================================
# ! ERROR: test_login_success (__main__.TestLogin.test_login_success)
# ! ----------------------------------------------------------------------
# ! Traceback (most recent call last):
# !   File "/home/visola/FSPR4-22-Homeworks/Lesson_30/Abduboriy/homework_30.py", line 46, in test_login_success
# !     store = Store()
# !             ^^^^^^^
# ! TypeError: Store.__init__() missing 5 required positional arguments: 'name', 'email', 'password', 'card_code', and 'card_balance'

# ! ======================================================================
# ! ERROR: test_login_wrong_email (__main__.TestLogin.test_login_wrong_email)
# ! ----------------------------------------------------------------------
# ! Traceback (most recent call last):
# !   File "/home/visola/FSPR4-22-Homeworks/Lesson_30/Abduboriy/homework_30.py", line 51, in test_login_wrong_email
# !     store = Store()
# !             ^^^^^^^
# ! TypeError: Store.__init__() missing 5 required positional arguments: 'name', 'email', 'password', 'card_code', and 'card_balance'

# ! ======================================================================
# ! ERROR: test_login_wrong_password (__main__.TestLogin.test_login_wrong_password)
# ! ----------------------------------------------------------------------
# ! Traceback (most recent call last):
# !  File "/home/visola/FSPR4-22-Homeworks/Lesson_30/Abduboriy/homework_30.py", line 56, in test_login_wrong_password
# !    store = Store()
# !           ^^^^^^^
# ! TypeError: Store.__init__() missing 5 required positional arguments: 'name', 'email', 'password', 'card_code', and 'card_balance'

# ! ----------------------------------------------------------------------
# ! Ran 5 tests in 0.002s

# ! FAILED (errors=5)