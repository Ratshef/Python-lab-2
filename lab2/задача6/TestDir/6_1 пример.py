#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Источник материала: http://jenyay.net/Programming/Argparse
##import sys
##import time
## #Пример №1. 
## #В команднойс строке ввести:D:\programs\python\Python36-32\6_1.py
## #Результат: Привет, мир!
##if __name__ == "__main__":
##    print ("Привет, мир!")  time.sleep(5)


## #Пример №2. 
## #В команднойс строке ввести:D:\programs\python\Python36-32\6_1.py 6_1.py
## #Результат: D:\programs\python\Python36-32\6_1.py
##import sys
##import time
## #вывод названия файла в консоль
##if __name__ == "__main__":
##    for param in sys.argv:
##        print (param)
##        time.sleep(5)

## #Пример №3. 
 #В команднойс строке ввести:D:\programs\python\Python36-32\6_1.py 6_1.py
 #Результат: D:\programs\python\Python36-32\6_1.py
##import sys
##import time
##if __name__ == "__main__":
##    if len (sys.argv) > 1:
##        print ("Привет, {}!".format (sys.argv[1] ) )
##        time.sleep(15)
##    else:
##        print ("Привет, мир!")
##        time.sleep(15)


###Пример №3. Пуск-Выполнить и в командной строке ввести
### D:\programs\python\Python36-32\6_1.py --name Вася
### Результат будет: Привет, Вася!
##import sys
##import time
##
##
##if __name__ == "__main__":
##    if len (sys.argv) == 1:
##        print ("Привет, мир!")
##        time.sleep(5)
##    else:
##        if len (sys.argv) < 3:
##            print ("Ошибка. Слишком мало параметров.")
##            time.sleep(5)
##            
##            sys.exit (1)
##
##        if len (sys.argv) > 3:
##            print ("Ошибка. Слишком много параметров.")
##            time.sleep(5)
##            sys.exit (1)
##
##        param_name = sys.argv[1]
##        param_value = sys.argv[2]
##
##        if (param_name == "--name" or
##                param_name == "-n"):
##            print ("Привет, {}!".format (param_value) )
##            time.sleep(5)
##        else:
##            print ("Ошибка. Неизвестный параметр '{}'".format (param_name) )
##            time.sleep(5)
##            sys.exit (1)



import sys
import argparse
import time
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-n', '--name')
    parser.add_argument ('-c', '--count', type=int, default=1)
 
    return parser
 
 
if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
 
    print (namespace)
 
    for _ in range (namespace.count):
        print ("Привет, {}!".format (namespace.name) )
        time.sleep(5)
