import requests

class Github:

    def __init__(self):

        self.apiUrl = 'https://api.github.com'
        self.token = 'token'

    def getUser(self,username):
        response = requests.get(self.apiUrl+'/users/'+username)
        return response.json()    
    def getRepos(self,username):
        response = requests.get(self.apiUrl+'/users/'+username+'/repos')
        return response.json()
    def createRepo(self,name):
        response = requests.post(self.apiUrl+'/user/repos/?access_token='+self.token,json={
            "name" : name,
            "description" : "hello world",
            "homepage" : "https://github.com"
        })
        return response.json()

isExit = False
github = Github()

while not isExit:

    choose = input('1-Find User\n2-Get Repo\n3-Create Repo\n4-Exit\nEnter Your Choose:')

    if choose == '1':
        username = input('username:')
        reqValue = github.getUser(username)
        reqName = reqValue['name']
        reqUserType = reqValue['type']
        print(f'Name:{reqName} Role:{reqUserType}')

    elif choose == '2':
        username = input('username:')
        reqValue = github.getRepos(username)
        for val in reqValue:
            print(val['name'])
    elif choose == '3':
        name = input('name:')
        returnValue = github.createRepo(name)
        print(returnValue)
    elif choose == '4':
        isExit = True
    else:
        print('invalid option')