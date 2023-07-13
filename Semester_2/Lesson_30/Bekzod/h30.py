import re

name='Bekzod'
pattern_name=r"(^[A-Za-z0-9$#@%]{,8}$)" # ! r"(^[A-Z][A-Za-z]+$)"
result_2=re.fullmatch(pattern_name,name)
print(result_2)


email='bekzodr73.@gmail.com'
pattern_email=r"(^[a-zA-z0-9.@]{,20}[a-zA-z]$)" # ! r"^[a-zA-Z0-9_.+-]+\.+@[a-zA-Z-0-9-.]+$"
result=re.fullmatch(pattern_email,email)
print(result)


pattern=r"(^[a-zA-Z0-9$#@%]{6,16}$)"  # ! r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$])[a-zA-Z0-9@#$]{6,16}$"
password='bekr123#123'
result=re.fullmatch(pattern,password)
print(result)


card_code='3647583465734283'
pattern_card_code=r"(^[0-9]{,16}[0-9]$)" # ! r"^\d{16}$"
result=re.fullmatch(pattern_card_code,card_code)
print(result)