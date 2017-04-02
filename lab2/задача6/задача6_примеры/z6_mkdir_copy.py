import os
import datetime
import shutil

def makedir(dirtest,namedir,namefile):   #dirtest=d:/z6,namedir=small,namefile=name
    dir_test_full=dirtest+'/'+namedir
    if os.path.isdir(dir_test_full):
        shutil.copy(namefile, namedir)
    else:
        os.chdir(dirtest) #смена текущей директории.
        os.mkdir(namedir)
        os.chdir(dirtest)
        shutil.copy(namefile, namedir)

dir='d:\z6'  #os.mkdir('d:/z6') #создаем директорию
names=os.listdir(dir)  #список файлов и директорий в папке.
for name in names:
    fullname=os.path.join(dir,name) #полное имя файла, объедтиняет путь и имя файла
    if os.path.isfile(fullname): #является ли путь файлом
        print(fullname)
        sizefile=os.path.getsize(fullname)
        print('{} bytes'.format(sizefile)) #нашел файл, определил байты
        data=os.path.getctime(fullname) #время создания файла (Windows), время последнего изменения файла (Unix).
        dd=datetime.datetime.fromtimestamp(data)
        print(dd, '\n')
    if (sizefile<2000):
        makedir('d:/z6','small',name)
        
