import re

class Store:
    def register(self, name, email, password, card_code, card_balance):
        name_regex = r"^[A-Z][a-zA-Z]*$"
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z-0-9-.]+$"
        password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{6,16}$"
        card_code_regex = r"^\d{16}$"

        if re.match(name_regex, name) and re.match(email_regex, email) and re.match(password_regex, password) and re.match(card_code_regex, card_code) and card_balance >= 0:
            return True
        else:
            return False

user = Store()
name = 'Name'
email = 'email@gmail.com'
password = 'passLword56@'
card_code = '1346134613461346'
card_balance = 1000

# print(user.register(name, email, password, card_code, card_balance))
