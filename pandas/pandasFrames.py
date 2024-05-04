import pandas as pd

s1 = pd.Series([3,2,5,1])
s2 = pd.Series([0,3,1,6])

data = dict(apples = s1, oranges = s2)

df = pd.DataFrame(data)

print(df)

df = pd.DataFrame()
print(df)

df = pd.DataFrame([1,2,3,4])
print(df)

df = pd.DataFrame([['ahmet',30],['ali',50],['ayse',70]])
print(df)

data = [['ahmet',30],['ali',50],['ayse',70]]

df = pd.DataFrame(data,columns=['name','grade'],index=[2,1,3])
print(df)

dict = {'name': ['ahmet','ali','ayse','fatma'],'grade':[30,10,60,90]}

df = pd.DataFrame(dict)
print(df)