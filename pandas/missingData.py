import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)

df= pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])


df = df.reindex(['a','b','c','d','e','f','g','h'])

#print(df)

#print(df.isnull())

#print('\n',df.notnull())


#print(df.dropna())

#print(df.dropna(axis = 1))

#print(df.dropna(how = 'any'))

#print(df.dropna(how= 'all'))

print(df.dropna(subset= ['column1','column2'],how='all'))
print(df.dropna(subset= ['column1','column2'],how='any'))

print(df.dropna(thresh=2))

print(df.fillna('veri yok'))

df = df.fillna(value = 0)

print(df.sum())
print(df.sum().sum())
print(df.size)