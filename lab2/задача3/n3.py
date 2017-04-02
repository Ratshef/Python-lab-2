import os

directory='music' #папка с которой работаем
files=os.listdir(directory)
print('Список файлов в каталоге',files)

# чтение строк из файла (с конструкцией with) 
try: 
    with open(r'n3.txt', 'rt') as f: #теперь будем всю эту конструкцию называть f
        lines = f.readlines()
        lines = list(map(lambda x: x.rstrip(), lines))#убрать \n на конце каждой строки с помощью rstrip и мар
    print('Список названий файлов из текстового файла: ',lines)

    for line in lines:
        str=''.join(line) #каждое название файла преобразувуем в строку
        str=str.split()
        print('Имя файла, которое должно совпадать: ',str[1])
        str=str[1]+'.mp3'
        j=files.index(str)
        filepath=directory+'/'+line #формируем путь к файлу с новым названием
        os.rename(directory+'/'+files[j],filepath) #переименовываем файл
except IOError as err: 
    print(err) 
    lines = []
    

