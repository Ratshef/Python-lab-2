import os
import hashlib

#функция для вычисления контрольной суммы файла
def md5_file(name_file):
    m=hashlib.md5()
    fl=open(name_file,'r')
    s=fl.read()
    m.update(s.encode('utf-8'))
    fl.close()
    return m.hexdigest()

try:
    #dir = 'dublicate'
    dir = input('Введите директорию: ')
    print(os.listdir(dir)) #список файлов и директорий в папке.

    #создаем пустые словари
    dubl={}
    diff={}
    print('Файлы директории dublicate:  ')
    for root, dirs, files in os.walk(dir): # пройти по директории рекурсивно
         for name in files:
            fullname = os.path.join(root, name) # получаем полное имя файла
            print (fullname)
            
            md5=md5_file(fullname)
            print(md5+'\n')

            #поиск дубликатов при помощи словарей
            filename=str(fullname)
            if md5 in diff.keys():
                dubl[md5]=str(filename+'; '+diff[md5])
            diff[md5]=filename

    print('\n Файлы-дубликаты:   ')
    #вывод словаря на экран
    for key in dubl:
        print(dubl[key],' ',key)

except(FileNotFoundError,OSError, UnicodeEncodeError):
    print('Директория введена неверно!')
