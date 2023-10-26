file=open('file.txt','r',encoding='utf-8')

for i in file:
    print(i)

file.seek(0)

for x in file:
    print(x,end='')

print('\n')
file.seek(0)

txt=file.read()
print(txt)

file.seek(0)

txt=file.read(5)
print(txt)

file.seek(0)

txt=file.readline()
print(txt)

file.seek(0)

txt=file.readline()
print(txt,end='')

file.seek(0)

txt=file.readline(2)
print(txt)

file.seek(0)

listA=file.readlines()
print(listA)
print(listA[2],end='')