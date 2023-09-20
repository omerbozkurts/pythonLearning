x= input('first number: ')
y= input('second number: ')

total=x+y

print(total)

#output is 1020 because input variables type is string 
#if we want to calculate x+y we need to casting type to integer

a=input("third number: ")
b=input("second number: ")

total=int(a)+int(b)

print(total)


number1=4
number2=5.3
city='Istanbul'
isOnline=False


#int to float
number1= float(number1)
print(number1)


#float to int
number2=int(number2)
print(number2)


#float to string or int to string
result=str(number1)+str(number2)
print(result)


#boolean to string
isOnline=str(isOnline)
print(isOnline)
print(type(isOnline))


#boolean to int
isOnline=int(isOnline)
print(isOnline)