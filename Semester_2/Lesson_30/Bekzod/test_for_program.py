import unittest
import purchase


class TestForLogin(unittest.TestCase):
    
    def test_for_not_given_email_and_password(self):
        result=purchase.Store.login(None,None)
        self.assertEqual(result,"Empty values were given.")

    def test_for_cheking_pas_and_email(self):
        result=purchase.Store.login("behruz@gmail.com","234fjfdsd",)
        self.assertTrue(result)

    def test_for_cheking_pas_and_email(self):
        result=purchase.Store.login("behruz@gmail.com", "234fjfdsd")
        self.assertNotEqual(result,"Wrong email or password")



class Test_for_Register(unittest.TestCase):
    def test_for_paasing_string(self):
        name="Behruz"
        email='behruz@gmail.com'
        password= '234fjfdsd'
        card_code='3647583465734283'
        balance=1000
        result=purchase.Store.register(name,email,password,card_code,balance)
        self.assertEqual(result,"Пользователь с такими данными уже есть.")

    def test_for_cheking_Not_all_in_register(self):
        result=purchase.Store.register(None,None,None,None,None)
        self.assertEqual(result,'Empty values were given.')

    def test_for_passing_value(self):
        name="Bekzod"
        email='bekzod@gmail.com'
        password= 'rbd1321'
        card_code='3647583465734290'
        balance=2000
        result=purchase.Store.register(name,email,password,card_code,balance)
        self.assertNotEqual(result,'Wrong credentials!')


class Test_for_Purchase_with_using_register(unittest.TestCase):
    def test_for_cheking_product_not_in_Products(self):
        product="kola"
        result=purchase.Store.purchase(self,product)
        self.assertIsInstance(result,AttributeError)
    def test_for_checking_product_in_PRODUCTS(self):
        result=purchase.Store.purchase(self,'sweater')
        self.assertTrue(result)

if  __name__=="__main__":
    unittest.main()
