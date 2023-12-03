def decorator(func):
    def wrapper():
        print("proccess before function")
        func()
        print("proccess after function")
    return wrapper

def sayHello():
    print("hello")

def sayGreeting():
    print("greeting")

sayHello=decorator(sayHello)
sayHello()

sayGreeting=decorator(sayGreeting)
sayGreeting()

@decorator
def funct():
    print("decorator")

funct()

print("\n")

import math
import time

def calculateTime(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish=time.time()
        print(f"work time = {finish-start}")

    return wrapper

@calculateTime
def power(num1,num2):
    print("{}*{}={}".format(num1,num2,math.pow(num1,num2)))

@calculateTime
def factorial(num):
    print("{}!={}".format(num,math.factorial(num)))

power(5,2)
factorial(5)
