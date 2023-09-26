fruits={'apple','grape','cherry'}

#print(fruits[0]) the list can't call with index
print(fruits)

fruits.add('banana')
print(fruits)

fruits.update(['mango','orange','watermelon','grape'])
print(fruits)

myList=[8,4,1,2,4,5,6,7,9,0,1,2,4,3]
print(myList)
print(set(myList))

print(fruits)
fruits.remove('mango')
print(fruits)
fruits.discard('apple')
print(fruits)
fruits.pop() #it pops random component
print(fruits)
fruits.clear()
print(fruits) 


