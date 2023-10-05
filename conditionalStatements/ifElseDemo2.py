#q1 is the entered number between 0 and 100

number=int(input('number:'))
if number>=0 and number<=100:
 print(f'{number} is between 0 and 100')
elif number>100:
 print(f'{number} greater than 100')
else:
 print(f'{number} less than 0')

#q2 is the entered number a positive even

number=int(input('number:'))
if number>0:
    if number%2==0:
        print('number is positive and even')
    else:
        print('number is positive and odd')
elif number==0:
    print('0 is neither positive or negative and even')
elif number%2==0:
   print('number is negative and even')
else:
   print('number is negative and odd')

#q3 checked the mail and password 

mail='mail@gmail.com'
password='123'
usrMail=str(input('mail:'))
usrPass=str(input("password:"))
if mail==usrMail:
    if password==usrPass:
      print('login is success')
    else:
      print('mail is correct but password is wrong')
elif password==usrPass:
   print('mail is wrong but password is correct')
else:
   print('mail and password is wrong')

#q4 compare the three numbers entered with each other

number1=int(input("number1: "))
number2=int(input('number2: '))
number3=int(input("number3: "))

if number1>number2 and number1>number3:
   print(f'number1({number1}) is greater')
elif number2>number3 and number2>number1:
   print(f'number2({number2}) is greater')
else:
   print(f'number3({number3}) is greater')


#q5 get midterm (40%) and final (60%) values from user and calculate average if avarage upper the 50 print successful else print failed
    #q5a if final is lower than 50 student is unsuceed
    #q5b if final is greater than 70 average is not important

midterm=int(input('midterm:'))
final=int(input('final:'))
average=(midterm*0.4)+(final*0.6)

if (average>50) and (final>50):
   print(f'average is {average} student is suceed')
elif final>=70:
   print(f"average is {average} and final is {final} student is suceed")
else:
   print(f'average is {average} student is failed')

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

if bmi<=18.4 and bmi>=0:
   print(f'bmi is:{bmi} underweight')
elif bmi<0:
   print('incorrect data entered')
elif bmi<=24.9:
   print(f'bmi is:{bmi} normalweight')
elif bmi<=29.9:
   print(f'bmi is:{bmi} overweight')
elif bmi<=34.9:
   print(f'bmi is:{bmi} obesity')
else:
   print('incorrect data entered')

