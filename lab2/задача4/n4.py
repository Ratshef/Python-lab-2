import os
import re

pathFile=input('Введите название файла: ')

#проверка: сущ.ли путь к этому файла и сущ.ли файл
if os.path.exists(pathFile):
    if os.path.isfile(pathFile):
        try: 
            with open(pathFile, 'rt') as f: #теперь будем всю эту конструкцию называть f
                lines = f.readlines()
                lines = list(map(lambda x: x.rstrip(), lines))#убрать \n на конце каждой строки с помощью rstrip и мар
            print('Список названий файлов из текстового файла: ',lines)


            kolline=0
            for line in lines:
                str=''.join(line)
                result=re.findall(r'\d{2}-\d{2}-\d{4}', str) #Извлечь дату из строки
                #print(result)

                #S.find - Поиск подстроки в строке. Возвращает номер первого вхождения или -1
                str_data=''.join(result)
                pos_data=str.find(str_data)
                if (pos_data!=-1)&(len(str_data)!=0):
                    print('Строка', kolline, ', позиция', pos_data, ': найдено \'', str_data,'\'')
                kolline=kolline+1
                str=''

        except IOError as err: 
            print(err) 
            lines = []

