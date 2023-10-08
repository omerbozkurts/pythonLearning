number=int(input('number:'))

flag=0

for x in range(2,number):
    if number%x==0:
        flag+=1

if number<=1:
    print(f'{number} is not prime')

elif flag==0:
    print(f'{number} is prime')

else:
    print(f'{number} is not prime')