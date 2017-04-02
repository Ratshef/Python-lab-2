try:
    f = open('d:\data.txt')
    f.writelines(s)
except IOError as err:
    print(err)
except:
    print('Something\'s gone wrong...')
else:
    print('File\'s been updated succesfully')    
finally:
    if f:
        f.close()
