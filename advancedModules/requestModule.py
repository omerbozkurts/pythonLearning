import requests
import json

rGet = requests.get('https://jsonplaceholder.typicode.com/todos')

txt = json.loads(rGet.text)

for t in txt:
    print(t['title'])

