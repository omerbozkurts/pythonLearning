import requests

class Movie:

    def __init__(self):
        self.apiUrl = 'https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1'
        self.apiKey = '8088a2208ebe1743316e9ab87d9486eb'
        
    
    def getMovies(self):

        headers = {"accept": "application/json",
                   "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4MDg4YTIyMDhlYmUxNzQzMzE2ZTlhYjg3ZDk0ODZlYiIsInN1YiI6IjY1ZTM3NDU3Yzk5ODI2MDE3YjYxY2IwZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.primlbJn1uvVLhi11xexmbO_Ds25YUDCfAleNeNB2XE"
        }   
        response = requests.get(self.apiUrl, headers=headers)
        return response.json()

movie = Movie()     

isExit = False

while not isExit:

    choose = input('1-Get Movie With Name\n2-Get Movie With Director\n3-Most Popular Films\n4-Film in Theaters\n5-Exit\nEnter Your Choose:')

    if choose == '1':
        name = str(input('name:'))
        movies = movie.getMovies()
        for movie in movies['results']:
            if movie['title'] == name:
                print(movie['title'])
                print(movie['original_language'])
                print(movie['vote_average'])
                print(movie['overview'])
    
    elif choose == '2':
        pass
    
    elif choose == '3':
        pass
    
    elif choose == '4':
        pass

    elif choose == '5':
        isExit = True
    else:
        print('invalid option')