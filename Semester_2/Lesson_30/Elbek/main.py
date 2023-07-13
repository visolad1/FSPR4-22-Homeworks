import unittest
import Story


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Story.Store

    # Tests for login method in Store class
    def test_store_login_success_user_exists(self):
        login_email = "bahti@gmail.com"
        login_password = "234$fjfdsd"

    def test_store_login_empty_password_error(self):
        login_email = "bahti@gmail.com"
        login_password = None


    def test_store_login_empty_args(self):
        login_email = None
        login_password = None



    def test_store_login_fail(self):
        login_email = "sdlfkjlkdfj@gmail.com"
        login_password = "234$fjfdsd"

if name == "main":
    unittest.main()