numbers=[2,5,6,3,7,0,52,59,92,48]

#q1 display to screen the list

for n in numbers:
    print(n)

#q2 get the start and end values from the user and display all odd numbers in between

start=int(input('enter start value:'))
end=int(input('enter end value:'))

if start<end:
    while start<=end:
        if start%2==1:
            print(start)
    start+=1
else:
    while start>=end:
        if start%2==1 or start%2==-1:
            print(start)
        start-=1

#q3 Display numbers between 1 and 100 in descending order

number=100

while number>0:
    print(number)
    number-=1

#q4 write the 5 numbers you will receive from the user to the screen sequentially

listA=[int(input('number1:')),int(input('number2:')),int(input('number3:')),int(input('number4:')),int(input('number5:'))]

listA=sorted(listA)
print(listA)

#q5 store the product information you will receive from the user in the product list
    
    # ask the user about the number of products
    # make a dictionary and get (name,price)
    # list products when finished adding products

productNum=int(input('product number:'))

i=0
products=[]

while i<productNum:
    name=input('name:')
    price=input('price:')
    products.append({'name':name,'price':price})
    i+=1

for product in products:
    print(product)