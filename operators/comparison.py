password='12345'
username="ali"

a,b,c,d=2,2,5,9
print(a==b,"\0",a==c)

resultUsr=username==chr(input('username:'))
print(resultUsr)
resultPsw=password==chr(input('password:'))
print(resultPsw)