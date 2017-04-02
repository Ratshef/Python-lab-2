#!/usr/bin/python
# -*- coding: UTF-8 -*-
# C:\Users\Пользователь\Desktop\Python\__lab2\zd2-6\reorganize.py --source "D:\TestDir" --days 2 --size 4096


import sys
import argparse
import time
import datetime

import os
import shutil
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--source',default="D:\TestDir")
    parser.add_argument ('-d', '--days', type=int, default=5)
    parser.add_argument ('-s', '--size', type=int, default=2000)
 
    return parser

 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    print (namespace)
 
    print ("Параметр --source, {}!".format (namespace.source) )
    print ("Параметр --days, {}!".format (namespace.days) )
    print ("Параметр --size, {}!".format (namespace.size) )
    time.sleep(5)

def make_dir_copy(dirtest,namedir,namefile):
    # dirtest='D:\TestDir'  namedir='Small'
    dirtestfull=dirtest+'\\'+namedir
    namedirR='r'+namedir
    if os.path.isdir(dirtestfull):
        shutil.copy(namefile, namedir)
    else:
        os.chdir(dirtest)  #смена текущей директории.
        os.makedirs(namedir)
        os.chdir(dirtest)
        shutil.copy(namefile, namedir)
    
    

tday=datetime.date.today()
print('Сегодня дата: ',tday)
tdelta=datetime.timedelta(days=namespace.days)
td=tday-tdelta
print('Для архива дата: ',td)


dir = namespace.source
names = os.listdir(dir)   # список файлов и поддиректорий в данной директории


#формируем директорию SMALL
for name in names:
    fullname = os.path.join(dir, name)  # получаем полное имя
    if os.path.isfile(fullname):        # если это файл...
        print (fullname)                  # делаем что-нибудь с ним
        sizefile=os.path.getsize(fullname)
        print ('{} bytes'.format(sizefile))
       
        if (sizefile<namespace.size):
            make_dir_copy(namespace.source,'Small',name)           
        time.sleep(5)


#формируем директорию ARCHIV
from datetime import datetime 
print('\n сегодня',tday,' список файлов для архива на дату',td)
for name in names:
    fullname = os.path.join(dir, name)  # получаем полное имя
    if os.path.isfile(fullname):        # если это файл...
        stat = os.stat(fullname)
        last_mod_file =datetime.fromtimestamp(stat.st_mtime).date()
##        print(last_mod_file)
        if (last_mod_file<td):
            print (fullname,'  ',last_mod_file)
            make_dir_copy(namespace.source,'ARCHIV',name)           
        time.sleep(5)
       
