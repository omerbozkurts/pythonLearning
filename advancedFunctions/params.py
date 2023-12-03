def add(a,b):
    return a+b
def subtraciton(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

def calculation(f1,f2,f3,f4,operand,number1,number2):
    if operand=="add":
        return f1(number1,number2)
    elif operand=="subtract":
        return f2(number1,number2)
    elif operand=="multiple":
        return f3(number1,number2)
    elif operand=='divide':
        return f4(number1,number2)
    else:
        return "invalid proccesing" 
    
oprnd="add"
num1=5
num2=6

clc=calculation(add,subtraciton,multiplication,division,oprnd,num1,num2)
print(clc)

oprnd="subtract"
clc=calculation(add,subtraciton,multiplication,division,oprnd,num1,num2)
print(clc)

oprnd="multiple"
clc=calculation(add,subtraciton,multiplication,division,oprnd,num1,num2)
print(clc)

oprnd="divide"
clc=calculation(add,subtraciton,multiplication,division,oprnd,num1,num2)
print(clc)