with open('file.txt','r+',encoding='utf-8') as file:
    file.write('updating')
    file.seek(0)
    print(file.read())
    print('\n{}'.format(file.tell()))

with open('file.txt','a',encoding='utf-8') as file:
    file.write('\nupdating2')

with open('file.txt','r',encoding='utf-8') as file:
    print(file.read())

with open('file.txt','r+',encoding='utf-8') as file:
    content=file.read()
    content='upUpdate\n' + content
    file.seek(0)
    file.write(content)

with open('file.txt','r',encoding='utf-8') as file:
    print(file.read())

print('\n')

with open('file.txt','r+',encoding='utf-8') as file:
    listA=file.readlines()
    listA.insert(2,'sortUpdate\n')
    file.seek(0)
    for i in listA:
        file.write(i)
    file.seek(0)
    print(file.read())