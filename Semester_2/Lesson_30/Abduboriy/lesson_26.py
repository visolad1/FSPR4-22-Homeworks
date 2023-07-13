'''
    Character Meaning
    'r' - open for reading (default)
    'w' - open for writing, truncating the file first (создает новый, если его нет)
    'x' - create a new file and open it for writing
    'a' - open for writing, appending to the end of the file if it exists
    'b' - binary mode
    't' - text mode (default)
    '+' - open a disk file for updating (reading and writing)
    'U' - universal newline mode (deprecated)
'''


# my_file = open('test.txt', 'r')
# print(my_file)
# print(my_file.read(), '\nWorked')

# my_file.seek(0)
# print(my_file.read(10))


# readline
# line_1 = my_file.readline()

# print(repr(line_1)) # \n
# print(my_file.readline())
# print(my_file.readline())
# print(repr(my_file.readline()))

# my_file = open('test.txt', 'w')

# age = 12
# name = 'Abduboriy'
# # my_file.write(f"My name's {name} and I'm {age} yrs old")

# my_file = open('write.txt', 'a')
# my_file.write(f"My name's {name} and I'm {age} yrs old")

# my_file.close()


# Contex manager: __enter__ | __exit__
# with open('test.txt', mode='r') as file:
    # print(file.read())
    # print(file.readline())
    # print(file.readlines())
#     for row in file.readlines():
#         print(row.strip())

# try:
#     my_file = open('write.txt', 'a')
#     # code
# except Exception as err:
#     print(err)
# finally:
#     my_file.close()

# with open('test.txt', mode='w') as file:
#     file.write(f'Some random data!')

# with open('test.txt', mode='a') as file:
#     for i in range(10):
#         file.write(f'\nSome random data {i}!')

# import csv


# with open("addresses.csv", newline="") as addresses_csv:
#     address_reader = csv.DictReader(addresses_csv, delimeter= ";")
#     for row in address_reader:
#         if row['Name'] == "Jennifer Barnet":
#             print(row(["Address"]))
#             break


import csv


USERS = [
    {
        'name': 'Behruz',
        'password': '234fjfdsd',
        'email': 'behruz@gmail.com',
        'purchases': [],
        'card': {'code': '3647583465734283', 'balance': 1000}
    }
]
# PRODUCTS = {
#     'key': 3,
#     'wear': 200,
# }
PRODUCTS = [
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "type": "black",
    },
    {
        "product_name": "sweater",
        "count": 10,
        "price": 100,
        "color": "black",
    }
]


class StoreOwner:
    pass


class Store:
    purchases = []

    def __init__(self, name, email, password, card_code, card_balance):
        self.name = name
        self.email = email
        self.password = password
        self.card_code = card_code
        self.card_balance = card_balance

    @classmethod
    def login(cls, email, password):
        if not (email and password):
            return 'Empty values were given.'
        for user in USERS:
            if user['email'] == email and user['password'] == password:
                return cls(user['name'], email, password, user['card']['code'], user['card']['balance'])
        return 'Wrong email or password'

    @classmethod
    def register(cls, name, email, password, card_code, card_balance):
        users_data = []
        user_keys = ""
        with open('users.csv') as users:
            user_reader = csv.DictReader(users, delimiter=';')
            user_keys = user_reader.fieldnames
            for row in user_reader:
                users.data.append(
                    {
                        "id": row['id'],
                        "name": row['name'],
                        "password": row['pasword'],
                        "email": row['email'],
                        "purchases": row['purchases'],
                        "card_code": row['card_code'],
                        "card_balance": row['card_balance']
                    }
                )

        # comment        
        for user in users_data:
            if user['email'] == email and user['password'] == password:
                return "Пользователь с такими данными уже есть."

        if not (name and email and password and card_code and card_balance):
            return 'Empty values were given.'
        
        if (
            name.isalpha() 
            and '@' in email 
            and len(password) >= 6 
            and len(card_code) == 16 
            and card_balance >= 0
            ):
            USERS.append(
                {
                    'name': name,
                    'password': password,
                    'email': email,
                    'purchases': [],
                    'card': {'code': card_code, 'balance': card_balance}
                }
            )
            return cls(name, email, password, card_code, card_balance)
        else:
            return 'Wrong credentials!'

    def purchase(self, product):
        if product not in PRODUCTS.keys():
            return 'Not available!'
        if self.card_balance <= 0:
            return "Not enough money!"

        for key, val in PRODUCTS.items():
            if key == product and self.card_balance - val >= 0:
                self.card_balance -= val
                self.purchases.append(product)
                for id, user in enumerate(USERS):
                    if user["email"] == self.email:
                        USERS[id]['purchases'].append(product)
                PRODUCTS.pop(key)
                return f'\nSuccesfully bought {product} and added into purchases!\nBalance: {self.card_balance}\nYour purchases: {self.purchases}'

        return f'{self.name} | {self.card_balance}: Not enough money.'
    
ss = Store.login(email='behruz@gmail.com', password='234fjfdsd')
print(ss)