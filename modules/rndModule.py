import random

#print(dir(random))

print(random.random())

print(random.random()*100)

print(int(random.random()*100))

print(random.randint(0,100))

print(random.uniform(10,100))

names=['ali','ayse','fatma','hasan','zeynep','murat']

print(names[random.randint(0,len(names)-1)])

print(random.choices(names))

greetings='hello my name is ali'

print(random.choices(greetings))

listA=list(range(10))
listB=range(10)

print(listA)
print(list(listB))

random.shuffle(listA)
print(listA)

print(random.sample(listA,3))
print(random.sample(listB,2))
