class Person:
    adress='no info'
    name='no info'
    age=0

    def __init__(self,name,age):
        self.name=name
        self.age=age


person1=Person('ali',23)
person2=Person('ayse',19)

print(f'{person1.name} {person1.age} {person1.adress}\n{person2.name} {person2.age}')

person1.adress='ankara'

print(f'{person1.name} {person1.age} {person1.adress}\n{person2.name} {person2.age}')

print(type(person1))
print(type(person1.name))