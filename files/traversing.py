file=open('file.txt','r',encoding='utf-8')
print(file.read())
file.seek(0)
file.close()

print('\n')

with open('file.txt','r',encoding='utf-8') as file:
    print(file.read(),end='')


with open('file.txt','r',encoding='utf-8') as file:
    file.seek(10)
    print('\n{}'.format(file.tell()))