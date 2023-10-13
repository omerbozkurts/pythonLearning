x=10

if x>5:
    raise Exception('error')

def checkPassword(psw):
    import re
    if len(psw)<8:
        raise Exception('parola 8 karakterden fazla olmalidir')
    elif not re.search('[a-z]',psw):
        raise Exception('parola kucuk harf icermelidir')
    elif not re.search('[A-Z]',psw):
        raise Exception('parola buyuk harf icermelidir')
    elif not re.search('[0-9]',psw):
        raise Exception('parola rakam icermelidir')
    elif re.search('[\s]',psw):
        raise Exception('parola bosluk karakteri icermemelidir')
    

password='1234567aA'

try:
    checkPassword(password)
except Exception as e:
    print(e)
finally:
    print('kontrol tamamlandi')


class Person:
    def __init__(self,name,age):
        if len(name)>10:
            raise Exception('isim 10 karakterden kisa olmalidir')
        else:
            self.name=name



try:
    p1=Person('abdulrezzakk',1923)
except Exception as a:
    print(a)
finally:
    print('procces completed')