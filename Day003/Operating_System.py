import os
from datetime import datetime

#To get the current working directory
operating = os.getcwd()
print(operating)


os.getcwd()
os.chdir('/Users/sony/Documents/')
chdir = os.getcwd()
print(chdir)

# Used to change directory
os.chdir('/Users/sony/Documents/100DaysPython')


# st_mtime --> modefication time 
day_stat = os.stat('Day20').st_mtime
#print(os.listdir())
print(datetime.fromtimestamp(day_stat))


'''
# The walk() function takes three arguements. Its a directory tree generators
for dirpath, dirnames, filenames in os.walk('/Users/sony/Documents/'):
    print('current Path: ', dirpath)
    print('Directories Name: ', dirnames)
    print('Files: ', filenames)
    print()
'''


# os.environ statement --> Used to get the list of all home directories
# the get() helps get a specific directories i.e Home dir
print(os.environ.get('Home'))



#Used the join() here to combine the home directory with a file name
file_path = os.path.join(os.environ.get('Home'), 'text.txt')
print(file_path)


#Split() --> separates the file text from the extention .txt
file_path = os.path.split('/tmp/text.txt')
print(file_path)






