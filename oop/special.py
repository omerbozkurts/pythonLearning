listA=[0,2,3]

class Movie():
    def __init__(self,title,director,duration):
        self.title=title
        self.director=director
        self.duration=duration
        print('movie objesi olusturuldu')

    def __str__(self):
        return f'film adi {self.title} yonetmen {self.director}'

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print(f'{self.title} adli film silindi')

m1=Movie('godfather','ford',175)

print(str(listA))
print(str(m1))

print(len(listA))
print(len(m1))

del(m1)
