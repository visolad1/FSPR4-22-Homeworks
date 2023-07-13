# Husan:

# 1. Не выводит ошибку. Методы класса Store при неправильном вводе данных возвращают ошибку.
# 2. Нет обработки исключений. Если файл(users.csv или products.csv) пустой, программа возвращает ошибку 
# user_id = int(list(get_csvdata("users.csv"))[-1]["id"]) + 1
# 	IndexError: list index out of range

# Husan

# elif
if method.lower() == "register":
    user_2 = Store.register(
        "Bill", "bill@john.com", "dfsfsafsdfasdf", "4657675849586758", 12000, False
    )
    print(user_2.add_product("laptop", 10, 90, "black"))
    s = time.time()
    print(user_2.purchase("sweater", 1), f"{time.time()-s:8f}")


# 
# elif 
if  method.lower() == "register":
    user_2 = Store.register(
        "Bill", "bill@john.com", "dfsfsafsdfasdf", "4657675849586758", 12000, False
    )
    if type(user_2) != type(Store):
        print(user_2)
    
    else:
        print(user_2.add_product("laptop", 10, 90, "black"))
        s = time.time()
        print(user_2.purchase("sweater", 1), f"{time.time()-s:8f}")


# IndexError

# Husan

user_id = int(list(get_csvdata("users.csv"))[-1]["id"]) + 1

# 
try: list(get_csvdata("users.csv"))[-1]["id"]
except IndexError: user_id = 1
else: user_id = int(list(get_csvdata("users.csv"))[-1]["id"]) + 1


# 2

# 1. Вывести на экран имена всех пользователей из файла passwords.csv и записать их в список compromised_users 
# 
with open("passwords.csv", encoding="utf-8") as passwords:
    reader = csv.DictReader(passwords)

    for row in reader:
        compromised_users.append(row)

# 

with open("passwords.csv", encoding="utf-8") as passwords:
    reader = csv.DictReader(passwords)

    for row in reader:
        print(f"Username: {row['Username']}. Password: {row['Password']}\n") 
        compromised_users.append(row)