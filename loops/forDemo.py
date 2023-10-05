numbers=[1,3,4,6,9,7,8,12,19,21]

#q1 which numbers in the list of numbers are exactly divisible by 3

for number in numbers:
    if number%3==0:
        print(number)

#q2 what is the sum of the numbers in the list of numbers

sum=0
for number in numbers:
    sum=sum+number
print(sum)

#q3 square the odd numbers in the list of numbers

for number in numbers:
    if number%2==1:
        print(number**2)

cities=['kocaeli','istanbul','ankara','izmir','rize']

#q4 which of the cities has at most five characters

for city in cities:
    if len(city)<=5:
        print(city)

urunler=[{'name':'samsung s6','price':'3000'},
         {'name':'samsung s7','price':'4000'},
         {'name':'samsung s8','price':'5000'},
         {'name':'samsung s9','price':'6000'}
         ]

#q5 what is the sum of the prices of the products

for urun in urunler:
    sum=sum+int(urun['price'])
print(sum)
    

#q6 products with a maximum price of 5000

for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun)