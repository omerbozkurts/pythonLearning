username='aliyilmaz'
password='deneme123'
usrUsername=str(input('username: '))
usrPass=str(input('password: '))

if username==usrUsername:
    if password==usrPass:
        print('logged in')
    else:
        print('password is not true')
else:
    print('username is not true')