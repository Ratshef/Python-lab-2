import os
import datetime
import shutil
import time
import sys
import argparse

print(os.getcwd()) 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-s', '--source', default='d:/z6')
    parser.add_argument ('-d', '--days', type=int, default=1)
    parser.add_argument ('-z', '--size', type=int, default=2000)
    return parser
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    print (namespace)
    print('Параметр --source, {}!'.format(namespace.source))
    print('Параметр --days, {}!'.format(namespace.days))
    print('Параметр --size, {}!'.format(namespace.size))
    time.sleep(5)
    


#функция создания директории
def makedir(dirtest,namedir,namefile):   #dirtest=d:/z6,namedir=small,namefile=name
    dir_test_full=dirtest+'/'+namedir
    if os.path.isdir(dir_test_full):
        shutil.copy(namefile, namedir)
    else:
        os.chdir(dirtest) #смена текущей директории.
        os.mkdir(namedir)
        os.chdir(dirtest)
        shutil.copy(namefile, namedir)

dirt=namespace.source  #os.mkdir('d:/z6') #создаем директорию
names=os.listdir(dirt)  #список файлов и директорий в папке.
print(dirt)
for name in names:
    fullname=os.path.join(dirt,name) #полное имя файла, объедтиняет путь и имя файла
    if os.path.isfile(fullname): #является ли путь файлом
        print(fullname)
        sizefile=os.path.getsize(fullname)
        print('{} bytes'.format(sizefile)) #нашел файл, определил байты
        data=os.path.getctime(fullname) #время создания файла (Windows), время последнего изменения файла (Unix).
        dd=datetime.datetime.fromtimestamp(data)
        print(dd, '\n')
    if (sizefile<namespace.size):
        makedir('d:/z6','small',name)
        
