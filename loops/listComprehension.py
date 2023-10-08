for x in range(5):
    print(x)

numbers=[x for x in range(5)]

print(numbers)

numbers=[]

for x in range(5):
    numbers.append(x)

print(numbers)

for x in range(5):
    print(x**2)

numbers=[x**2 for x in range(5)]
print(numbers)

numbers=[x*x for x in range(5) if x%3==0]
print(numbers)


myString='Hello'
myList=[]

for letter in myString:
    myList.append(letter)

print(myList)

myList=[letter for letter in myString]
print(myList)


years=[1943,2004,1993,2013,2009]
ages=[2023-year for year in years]
print(ages)

result=[x if x%2==0 else 'Tek' for x in range(5,10)]
print(result)

result=[x for x in range(10) if x%2==0]
print(result)

listA=[]

for x in range(3):
    for y in range(3):
        listA.append((x,y))

print(listA)
print(len(listA))

listA=[(x,y) for x in range(3) for y in range(3)]
print(listA)