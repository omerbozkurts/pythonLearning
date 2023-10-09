def sayHello(name = 'user'):
    print(f'hello {name}')

sayHello('ahmet')

def sayHello(name = 'user'):
    hello='hello '+name
    return hello

print(sayHello('ayse'))
print(sayHello())

def total(num1,num2):
    return num1+num2

print(total(5,2))

def ageCalculate(number):
    age=2023-number
    return age

print(ageCalculate(2002))

def retireCalculate(byear,name):
    '''

        DOCSTRING: calculate the retirement according to birthday year and name information
        INPUT: birthday year and name
        OUTPUT: how much years left to the retirement

    '''
    age=ageCalculate(byear)
    retireYear=65-age
    if retireYear>0:
        print(f'{name} {retireYear} years left to retirements')
    else:
        print(f'{name} are already retired')

retireCalculate(2002,'omer')
retireCalculate(1952,'ayse')
print(help(retireCalculate))