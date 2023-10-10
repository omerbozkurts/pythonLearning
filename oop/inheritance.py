class Person():
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname
        print('insan sinifi calistirildi')
        print(f'merhaba {self.name} {self.surname}')

    def whoAmI(self):
        print('i am a person')

    def eat(self):
        print('i am eat')


class Student(Person):
    def __init__(self,name,surname,stdNo):
        Person.__init__(self,name,surname)
        self.stdNo=stdNo
        print('ogrenci sinifi calistirildi')

    def whoAmI(self):
        print('i am a student')


class Teacher(Person):
    def __init__(self,name,surname,branch):
        super().__init__(name,surname)
        print('teacher sinifi calistirildi')
        self.branch=branch


p1=Person('ali','yilmaz')
s1=Student('zeynep','korkmaz',3513)

p1.whoAmI()
s1.whoAmI()
p1.eat()
s1.eat()

print(f'{s1.name} {s1.surname} {s1.stdNo}')

t1=Teacher('ayse','durmaz','math')
t1.eat()
t1.whoAmI()

print('{} {} {}'.format(t1.name,t1.surname,t1.branch))
