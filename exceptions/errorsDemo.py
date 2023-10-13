listA=['2','5','6a','10b','abc','15','50']

#q1 find the numeric values in the list elements

for x in listA:
    try:
        print(int(x))
    except:
        continue

#q2 make sure that every input received is a numeric value unless the user enters a 'k' value, if it is not a numeric value give an error message

a=1

while a!='q':
    a=input('sayi giriniz:')
    try:
        int(a)
    except ValueError:
        print('sayidan farkli bir deger girildi')
print('q degeri girildigi icin deger alma islemi sonlandirildi')

#q3 give a Turkish character error in the entered password

a=True

while a:
    psw=input('password:')
    import re
    if re.search('[ğ,ü,ş,i,ö,ç]',psw):
        print('turkce karakter girilemez')
    else:
        print('turkce karakter girilmedigi icin sifre basariyla olusturuldu')
        a=False

#q4 create a factorial function and print an error message for incorrect values

def factorial(n):
    if n<0:
        raise ValueError('negatif deger')
    elif n==1:
        return 1
    return n*factorial(n-1)

try:
    print(factorial(-4))
except Exception as e:
    print(e)
