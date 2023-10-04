number1=int(input('number1:'))
number2=int(input('number2:'))

if number1>number2:
    print(f'{number1} is bigger than {number2}')
elif number1==number2:
    print(f'{number1} equal {number2}')
else:
    print(f'{number2} is bigger than {number1}')


number=int(input('number: '))
if number>0:
    print('number is positive')
elif number<0:
    print('number is negative')
else:
    print('number is zero')