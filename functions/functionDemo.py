#q1 write the given word to the screen with the given number

def printScreen(a,b):
    for x in range(0,b):
        print(a)

printScreen('ali',5)

#q2 write a function that converts an unlimited number of parameters sent to it into a list

listA=[]

def makeList(list,*number):
    for n in number:
        listA.append(n)
    return listA

makeList(4,5,1,5,6,6,1,34,21,6)
print(listA)

#q3 find all prime numbers between two numbers sent

def primeNums(a,b):
    for x in range(a,b):
        flag=0
        for y in range(2,x):
            if x%y==0:
                flag+=1
        if flag==0:
            print(x)

primeNums(10,20)

#q4 return a list of all occurrences of the given number

listB=[]

def occNum(num):
    for x in range(1,num+1):
        if num%x==0:
            listB.append(x)
    
    return listB

print(occNum(30))