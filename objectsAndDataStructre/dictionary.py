cities=['adana','ankara','izmir','istanbul','bursa']
cityCodes=[1,6,35,34,16]

print(cityCodes[cities.index('ankara')])
print(cityCodes[cities.index('izmir')])

citiesDictionary={'adana':1, 'ankara':6,'izmir':35,'amasya':5,'tokat':60}
print(citiesDictionary['amasya'])

users={ 'omerbozkurt':
            {
                'age':21,
                'city':'tokat',
                'number':345312,
                'education':'prep school',
                'roles':['admin','user','writer']
            },
       'aliyilmaz':
            {
                'age':27,
                'city':'istanbul',
                'number':39253,
                'education':'licence degree',
                'roles':['user','writer']
            }}

print('omer bozkurt age: {}'.format(users['omerbozkurt']['age']))
print('omer bozkurt is admin: {}'.format(users['omerbozkurt']['roles'][0]) )
print('ali yilmaz city: {} \nali yilmaz roles: {} \nali yilmaz is writer: {}'.format(users['aliyilmaz']['city'],users['aliyilmaz']['roles'],users['aliyilmaz']['roles'][1]))