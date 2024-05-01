import json
import os

class User:

    def __init__(self, username, password, email):
        
        self.username = username
        self.password = password
        self.email = email

    

class UserRepository:

    def __init__(self):

        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        self.loadUser()

    def loadUser(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as f:
                users = json.load(f)
                for user in users:
                    user = json.loads(user)
                    nUser = User(user['username'],user['password'],user['email'])
                    self.users.append(nUser)

    def register(self,user : User):
        self.users.append(user)
        self.saveToFile()

    def login(self, username, password):

        for user in self.users:

            if user.username == username and user.password == password:
                
                self.isLoggedIn = True
                self.currentUser = user
                print('login successful')

    def saveToFile(self):

        listA = []

        for user in self.users:
            listA.append(json.dumps(user.__dict__))

        with open('users.json','w') as f:
            json.dump(self.users, f)

    
    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}

        print('logout successful')

    def identiy(self):
        if self.isLoggedIn:
            print(f'username: {self.currentUser.username}')
        else:
            print('user is not logged in')



repo = UserRepository()

isTrue = True

while isTrue:
    print('Menu')
    print('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit')
    choose = input('Enter Your Choose:')

    if choose == '1':
        username = input('username:')
        password = input('password:')
        email = input('email:')
        user = User(username,password,email)
        repo.register(user)
    elif choose == '2':
        username = input('username:')
        password = input('password:')
        repo.login(username,password)
    elif choose == '3':
        repo.logout()
    elif choose == '4':
        repo.identiy()
    elif choose == '5':
        isTrue = False
    
