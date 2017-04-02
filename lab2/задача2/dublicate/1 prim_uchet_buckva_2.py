text = 'hello world'
indecies = set(text)
values = (text.count(letter) for letter in indecies)
analize = dict(zip(indecies, values)) #генератор словарей
print (analize)

# получаем ключи словаря
l=analize.keys()
print(l) #dict_keys(['l', 'e', 'o', 'h', 'd', ' ', 'r', 'w'])

# превращаем его в обычный список
l = list(l) 
print(l) #['l', 'e', 'o', 'h', 'd', ' ', 'r', 'w']

# сортируем список
l.sort()
print(l) #[' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w']

# вывод элементов словаря (ключ - значение) по алфавиту
for i in l: 
    print(i, '-', analize[i], end='; ') #- 1; d - 1; e - 1; h - 1; l - 3; o - 2; r - 1; w - 1;
    


