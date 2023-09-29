x,y,z=2,5,107

numbers=1,5,7,10,6

#q1 subtract the sum x,y,z from the product of two numbers received from the user

#number1=int(input('first number: '))
#number2=int(input("second number: "))
#number1*=number2
#sum=x+y+z
#print('result is: {result}'.format(result=number1-sum))

#q2 calculate the remainder of y over x

print('result is:{r}'.format(r=y//x))

#q3 calculate mod 3 of the sum x,y,z

sum=x+y+z
print(f'result is: {sum%3}')

#q4 calculate the xth power of y

print(f'result is: {y**x}')

#q5 x,*y,z=numbers, what is the third power of z

x,*y,z=numbers
print(f"result is: {z**3}")

#q6 x,*y,z=numbers, What is the sum of the values of y

sum=y[0]+y[1]+y[2]
print(sum)
