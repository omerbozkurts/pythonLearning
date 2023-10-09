def changeName(n):
    n='ali'

name='ahmet'
changeName(name)
print(name)

listA=[0,2,4,1]

def change(a):
    a[2]=15

change(listA)
print(listA)

cities=['ankara','izmir','amasya']

def changeCity(c):
    c[1]='istanbul'

print(cities)
changeCity(cities)
print(cities)

cities=['ankara','izmir','amasya']
listB=cities
listB[2]='sivas'
print(cities)

cities=['ankara','izmir','amasya']
listC=cities[:]
listC[1]='kayseri'
print(cities)
print(listC)

def add(a,b,c=0):
    return sum((a,b,c))

print(add(2,5))
print(add(4,3,5))

def sumParams(*params):
    return sum((params))

print(sumParams(4,6,2))
print(sumParams(4,6,2,4,5,6))
print(sumParams(4,6))
print(sumParams(4,6,2,23,37,74,1,43,45,12,31,23))

def sumParams2(*params):
    sum=0
    for n in params:
        sum=sum+n
    return sum

print(sumParams2(4,3,5))


def displayUser(**args):
    for key,value in args.items():
        print(f'{key} is {value}')

displayUser(name='ali',age=19)
displayUser(name='ahmet',age=23,city='ankara')
displayUser(name='zeynep',age=21,city='manisa',phone='23421',mail='zeynep@mail.com')

def args(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

args(3,2,5.7,1,4,2.3,5,'ankara','amasya',city='adana',adress='province',email='abc@mail.com')