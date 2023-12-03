def func():
    print('hello')

vrbl=func
print(vrbl)
print(func)

def func2(name):
    print(name)

vrbl2=func2

vrbl2('ali')
func2('ali')

def outerFunc(num):
    print('outer')
    def innerFunc(num2):
        print('inner')

outerFunc(1)
#innerFunc(1) illegal usage

def outerFunc(num):
    print('outer')
    def innerFunc(num):
        print('inner')
    innerFunc(num)

outerFunc(1)


def factorial(num):
    if not isinstance(num,int):
        raise TypeError('unexpected value entered')
    if not num>=0:
        raise ValueError('number must be greater than 0')
    def innerFactorial(num):
        if num==0:
            return 1
        return num*factorial(num-1)
    return innerFactorial(num)

try:
    print(factorial(0))
except Exception as e:
    print(e)