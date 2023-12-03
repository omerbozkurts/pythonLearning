listA=[2,4,1,5,6]

iterator=iter(listA)

print(next(iterator))
print(next(iterator))
print(next(iterator))

flag=1
iterator=iter(listA)

while flag==1:
    try:
        print(next(iterator))
    except StopIteration as a:
        flag=-1
        print('end of the list')


class MyNumber:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.end:
            x=self.start
            self.start+=1
            return x
        else:
            raise StopIteration
        
listB= MyNumber(10,20)

for i in listB:
    print(i)