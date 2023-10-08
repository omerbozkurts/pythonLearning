for item in range(5):
    print(item)

print('\n')

for item in range(10,15):
    print(item)

print('\n')

for item in range(20,50,10):
    print(item)

print('\n')

greeting='hello'
index=0

for letter in greeting:
    print(f'{index} {letter}')
    index+=1

for letter in enumerate(greeting):
    print(letter)

for index,letter in enumerate(greeting):
    print(f'index is: {index} letter is :{letter}')

print('\n')

listA=[0,1,2,3,4,5]
listB=['a','b','c','d','e','f']
listC=['A','B','C','D','E','F']

print(list(zip(listA,listB)))

for item in list(zip(listA,listB,listC)):
    print(item)

for a,b,c in list(zip(listA,listB,listC)):
    print(f'index: {a} letter: {b} {c}')