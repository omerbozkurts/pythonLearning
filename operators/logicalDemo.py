#q1 is the entered number between 0 and 100

number=int(input('number:'))
isBetween=number>0 and number<100
print(f'{number} is between 0 and 100: {isBetween}')

#q2 is the entered number a positive even

number=int(input('number:'))
isPositiveEven=number>0 and number%2==0
print(f'{number} is positive and even: {isPositiveEven}')

#q3 checked the mail and password 

mail='mail@gmail.com'
password='123'
usrMail=str(input('mail:'))
usrPass=str(input("password:"))
isMailTrue=mail==usrMail
isPassTrue=password==usrPass
isTrue= (isMailTrue) and (isPassTrue)
print('{} is : {} and {} is : {} login is success: {}'.format(usrMail,isMailTrue,usrPass,isPassTrue,isTrue))

#q4 compare the three numbers entered with each other

number1=int(input("number1: "))
number2=int(input('number2: '))
number3=int(input("number3: "))

comp1=number1>number2 and number1>number3
comp2=number2>number1 and number2>number3
comp3=number3>number1 and number3>number2
comp4=number1==number2 and number2==number3

print('number1({}) is greater: {}'.format(number1,comp1))
print('number2({}) is greater: {}'.format(number2,comp2))
print('number3({}) is greater: {}'.format(number3,comp3))
print('they are equal({},{},{}):{}'.format(number1,number2,number3,comp4))

#q5 get midterm (40%) and final (60%) values from user and calculate average if avarage upper the 50 print successful else print failed
    #q5a if final is lower than 50 student is unsuceed
    #q5b if final is greater than 70 average is not important

midterm=int(input('midterm:'))
final=int(input('final:'))
average=(midterm*0.4)+(final*0.6)

isPass=(average>50) and (final>50)
isPass= (isPass==True) or (final>=70)

print(f'average is {average} student is suceed:{isPass}')

#q6 take the personal info and calculate the bmi
'''
    bmi         = weight/(height)^2
    0-18.4      => underweight
    18.5-24.9   => normal weight
    25-29.9     => overweight
    30-34.9     => obesity
'''    

weight=int(input('weight:'))
height=float(input('height:'))

bmi=weight/ (height**2)
bmi=round(bmi,2)
underweight= (bmi>=0) and (bmi<=18.4)
normalweight= (bmi>=18.5) and (bmi<=24.9)
overweight= (bmi>=25) and (bmi<=29.9)
obesity= (bmi>=30) and (bmi<=34.9)

print(f'bmi is:{bmi} \nunderweight:{underweight} \nnormalweight:{normalweight} \noverweight:{overweight} \nobesity:{obesity}')

