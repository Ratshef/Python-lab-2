import os


#Каталог из которого будем брать файлы 
#directory="C:\\Users\Пользователь\Desktop\Python\_ _ lab2"
directory="C:/Users/Пользователь/Desktop/Python/_ _ lab2/3_muz_file"


#Получаем список файлов в переменную files 
files=os.listdir(directory)
print('Список файлов в каталоге: ',files)

    #чтение срок - названий файлов из sp_korrect.txt
try: 
    with open(r'sp_korrect.txt', 'rt') as f: 
        lines = f.readlines()
        lines=list(map(lambda x: x.rstrip(), lines))  # убрать \n на конце каждой строки с помощью rstrip и мар 
    print("Список названий файлов из текстового файла",lines)

   
    for i in lines:
        str=''.join(i)
        
        str=str.split()
        #print ('Имя файла, которое должно совпадать :',str[1])

        str=str[1]+'.mp3'
        j=files.index(str)
        
        filepath=directory+'/'+i
##        print (filepath)
##        if os.path.isfile(filepath):
##            print ('yes')
##        else:
##            print ('no')
            
        os.rename(directory+'/'+files[j],filepath)
        str=''
     
except IOError as err: 
        print(err) 
        lines = [] 



