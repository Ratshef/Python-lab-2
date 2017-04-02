import re

str=input('Введите текст: ')
print(str)
str1=re.findall(r'[A-Z]\w+\d{2}|\d{4}', str)
print(str1)
