#q1 which of the two numbers entered is larger

number1=int(input())
number2=int(input())
comparison=number1>number2
print(f'number1: {number1} is greater than number2: {number2} = {comparison}')

#q2 get midterm (40%) and final (60%) values from user and calculate average if avarage upper the 50 print successful else print failed

number1=int(input('midterm:'))
number2=int(input('final:'))
average=number1*0.4+number2*0.6
comparison=average>50
print(f'average is {average} Student succeed:{comparison}')

#q3 print whether the entered number is odd or even

number=int(input('number:'))
odd=number%2==0
print(f'{number} is odd:{odd}')

#q4 print whether the entered number is positive or negative

number=int(input('number:'))
positive=number>0
print('{} is postive: {}'.format(number,positive))

#q5 get password and email information and check its accuracy

password='deneme123'
mail='admin@mail.com'
inpMail=str(input('mail:'))
inpPass=str(input('password:'))
trueMail=mail==inpMail
truePass=password==inpPass
print('mail is:{} password is:{}'.format(trueMail,truePass))
