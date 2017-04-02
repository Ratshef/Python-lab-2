#Работа с файловой системой и ОС

import os
os.getcwd()
print ('Название рабочей директории: ',os.getcwd())

try:
    os.mkdir('--source')
    os.makedirs(r'--source\Archive')
    os.makedirs(r'--source\Small')

    # получить список только папок:
    folders = [entry for entry in os.listdir(os.getcwd())
                     if os.path.isdir(entry)]
    print (folders)
    
except Exception as err:
    print(err)
    


