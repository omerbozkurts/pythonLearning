import os
import datetime

# print(dir(os))

print(os.name)

print(os.getcwd())

# os.mkdir('file')

os.chdir('file')

print(os.getcwd())

# os.makedirs('file/file')

# os.rename('file','file2')

# os.chdir('file/file2')

print(os.getcwd())

# os.remove('file')

# print(os.listdir())

# print(os.listdir('file'))

# for file in os.listdir('file'):
#     if file.endswith('le'):
#         print(file)


print(os.stat('file2'))

stFile = os.stat('file2')

print(stFile.st_size)

print(stFile.st_ctime)

print(datetime.datetime.fromtimestamp(stFile.st_ctime)) # creating time

print(datetime.datetime.fromtimestamp(stFile.st_atime)) # last using 

print(datetime.datetime.fromtimestamp(stFile.st_mtime)) # last changing

# os.system('notepad.exe')


os.chdir('..')

print(os.path.abspath('osModule.py'))

print(os.path.dirname(os.path.abspath('osModule.py')))

print(os.path.exists('osModule.py'))

print(os.path.isdir('osModule.py'))

print(os.path.isfile('osModule.py'))

os.path.join('C:\\','anotherFile','anotherFile2')

print(os.path.split('file'))

print(os.path.splitext('osModule.py'))