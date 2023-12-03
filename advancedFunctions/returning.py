def pow(number):
    def inner(power):
        return number**power
    return inner


two=pow(2)
print(two) #it returns the inner function
three=two(3)
print(three)

def roleCheck(page):
    def inner(role):
        if role=="admin":
            return str(role) + " can access " + str(page) 
        else:
            return str(role) + " can't access " + str(page) 
    return inner


page="admin editor"
user1='admin'
user2='ali'

check=roleCheck(page)
check=check(user2)
print(check)

def calculate(operand):
    def add(*args):
        num=0
        for n in args:
            num=num+n
        return num
    def multiplication(*args):
        num=1
        for n in args:
            num*=n
        return num
    if operand=="add":
        return add
    elif operand=="multiplication":
        return multiplication
    
clcAdd=calculate('add')
clcAdd=clcAdd(2,3,5,1,5)
print(clcAdd)

clcMlt=calculate('multiplication')
clcMlt=clcMlt(5,2,3,5)
print(clcMlt)