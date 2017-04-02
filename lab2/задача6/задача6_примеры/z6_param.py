#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
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
    time.sleep(5)
        
##if __name__ == "__main__":
##    print ("Привет, мир!")
##    time.sleep(5)


##import sys
##
##if __name__ == "__main__":
##    for param in sys.argv:
##        print (param)
##        time.sleep(5)


##import sys
##
##if __name__ == "__main__":
##    if len (sys.argv) > 1:
##        print ("Привет, {}!".format (sys.argv[1] ) )
##        time.sleep(5)
##    else:
##        print ("Привет, мир!")
##        time.sleep(5)

##import sys
##
##if __name__ == "__main__":
##    if len (sys.argv) == 1:
##        print ("Привет, мир!")
##        time.sleep(5)
##    else:
##        if len (sys.argv) < 3:
##            print ("Ошибка. Слишком мало параметров.")
##            sys.exit (1)
##            time.sleep(5)
##        if len (sys.argv) > 3:
##            print ("Ошибка. Слишком много параметров.")
##            sys.exit (1)
##            time.sleep(5)
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
##            sys.exit (1)
##            time.sleep(5)
