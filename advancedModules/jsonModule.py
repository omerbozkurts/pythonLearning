import json

#json loads

person = {'name': 'Ali Yilmaz','languages': ['python','java','c']}

personJSON = "{'name': 'Ali Yilmaz','languages': ['python','java','c']}"


# with open('person.json') as f:
#     data = json.load(f)
#     print(data)

with open('person.json','w') as f:
    json.dump(person,f)
     