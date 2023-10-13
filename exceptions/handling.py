try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except ZeroDivisionError:
    print('sifira bolunmez')

try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except ValueError:
    print('girilen degerler sayi olmali')

try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except (ZeroDivisionError,ValueError):
    print('bir hata olustu')

try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except ZeroDivisionError as e:
    print(e)

try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except ValueError as e:
    print(e)

try:
    x=int(input('x:'))
    y=int(input('y:'))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print(e)

while True:
    try:
        x=int(input('x:'))
        y=int(input('y:'))
        print(x/y)
    except (ZeroDivisionError,ValueError) as e:
        print(e)
    else:
        break
    finally:
        print('try except bloklari calistirildi')