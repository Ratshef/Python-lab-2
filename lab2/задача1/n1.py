import os

pathFile=input('Введите название файла: ')

#проверка: сущ.ли путь к этому файла и сущ.ли файл
if os.path.exists(pathFile):
    if os.path.isfile(pathFile):
        myfile=open(pathFile, 'r') #r-открытие на чтение
        str=myfile.read()
        print('Данные из файла',str)

        str=str.lower() #S.lower()- Преобразование строки к нижнему регистру

        lst=[]
        for i in range(len(str)):
            if str[i].isalpha():
                lst.append(str[i])
        print('Список букв без спец.символов',lst)

        #делаем из спика строку
        myStr=''.join(lst)
        print('Строка только из букв: ',myStr)


        ##kol=myStr.count('e')
        ##print(kol)

        def fKol(s): 
            letters=set(s) #не повторяющиеся элементы в случайном порядке
            slovar={}
            for letter in letters:
                slovar[letter]=s.count(letter)
            return slovar #вернутся пары - ключ и значение (ассоциативный массив-т.е.словарь)
        f=fKol(myStr)
        print('Символы и их количество',f) #вывели словарь

        def invert_func(d):
            inv=dict() #создать словарь с помощью функции dict
            for key in d:
                val=d[key]
                if val not in inv:inv[val]=[key]
                else:inv[val].append(key)
            return inv
        print(invert_func(f))

pathFile.close()

else:
    print('Объект не найден')
