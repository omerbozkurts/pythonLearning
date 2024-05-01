import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

html=requests.get(url,headers=headers).content

soup = BeautifulSoup(html,'html.parser')

movList = soup.find('ul',{'class':'ipc-metadata-list'}).find_all('li',limit=20)

for listElement in movList:
    movName = listElement.find('h3',{'class':'ipc-title__text'}).text
    point = listElement.find('span',{'class':'ipc-rating-star'}).text
    print(movName,point)

