class Person:
    name='no info'
    adress='no info'
    age=0

    def __init__(self,name,age):
        self.age=age
        self.name=name
    
    def greetings(self):
        print(f'hello {self.name}')

    def calculateBY(self):
        return 2023-self.age
    

person1=Person('ali',35)
person2=Person('ayse',25)

person1.greetings()
print(person1.calculateBY())

person2.greetings()
print(person2.calculateBY())

class Circle:
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

    def calculateCircum(self):
        return 2*self.pi*self.radius
    def calculateArea(self):
        return self.pi*(self.radius**2)
    

circle1=Circle()
circle2=Circle(3)

print(f'circle1 circumference is: {circle1.calculateCircum()} area is: {circle1.calculateArea()}')
print(f'circle2 circumference is: {circle2.calculateCircum()} area is: {circle2.calculateArea()}')        