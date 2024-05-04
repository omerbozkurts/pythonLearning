import pandas as py
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)

df = py.DataFrame(data,columns=['column1','column2','column3','column4','column5'])

print(df)

print('\n',df.head(10))

print('\n',df.tail(10))

print('\n',df['column1'].head())

print('\n',df.query("column1 >= 40 and column2 % 2 == 0"))