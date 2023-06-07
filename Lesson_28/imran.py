# # 1
# staff = {
#     'Austin': {
#         'floor managers': 1,
#         'sales associates': 5
#     },
#     'Melbourne': {
#         'floor managers': 0,
#         'sales associates': 8
#     },
#     'Beijing': {
#         'floor managers': 2,
#         'sales associates': 5
#     },
# }
# def print_staff_report(location, staff_dict):
#     managers = staff_dict['floor managers']
#     sales_people = staff_dict['sales associates']
    
#     try: 
#         ratio = sales_people / managers
#     except ZeroDivisionError: 
#         print('Ratio is undefined.')
#         return
        
#     print('Instrument World ' + location + ' has:')
#     print(str(sales_people) + ' sales employees')
#     print(str(managers) + ' floor managers')
#     print('The ratio of sales people to managers is ' + str(ratio))
#     print()
# try:
#     for location, staff in staff.items():
#         # Write your code below:
#         print_staff_report(location, staff)
# except KeyError:
#     print('Invalid key used.')


# 2
# inventory = {
#     'Piano': 3,
#     'Lute': 1,
#     'Sitar': 2
# }

# class OutOfStockError(Exception):
#     def __init__(self, supply):
#         self.supply = supply
#     def __str__(self): 
#         return 'We dont have ' + str(self.supply) + ' in stock'

# def submit_order(instrument, quantity):
#     # ! Нет обработки исключения KeyError
#     supply = inventory[instrument] # ! supply = instrument
    
#     if quantity > supply: # ! if quantity > inventory[instrument]
#         raise OutOfStockError(supply)

#     inventory[instrument] -= quantity
#     print('Successfully placed order! Remaining supply: ' + str(inventory[instrument]))

# instrument = 'Piano'
# quantity = 5
# submit_order(instrument, quantity)

# 3
# import re

# titles = ["Middle JavaScript Developer",
#           "Middle JavaScript Developer (AngularJS 9)",
#           "Middle JavaScript Developer (React)",
#           "Senior JavaScript Developer (Angular)",
#           "middle JavaScript angularjs "]

# skills = re.compile(r"(javascript|nodejs)", flags=re.I) # ! flags = re.IGNORECASE
# for title in titles:
#     result = re.findall(skills, title)
#     if result != []:
#         print(result)

# # ! Проверяет только наличие подстрок javascript и nodejs