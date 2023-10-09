def square(num):
    return num**2

print(square(2))

def square2(num): return num**2

print(square2(3))

numbers=[0,2,4,1,3,6]

listA=[]

def square3(list):
    for a in list:
        listA.append(a**2)
    return listA

print(square3(numbers))

print(map(square2,numbers))

print(list(map(square2,numbers)))

print(list(map(lambda num: num**2,numbers)))

sqr=lambda num: num**2

print(list(map(sqr,numbers)))

print(sqr(3))

def checkEven(num):
    return num%2==0

print(list(filter(checkEven,numbers)))

print(list(filter(lambda num:num%2==0,numbers)))

chckEven=lambda num: num%2==0

print(list(filter(checkEven,numbers)))