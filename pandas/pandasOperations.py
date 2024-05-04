import pandas as pd
import numpy as np

data = {
    'column1' : [1,2,3,4,5,6],
    'column2' : [101,20,20,43,91,53],
    'column3' : ['abac','basdfasca','adfadase','adasdfasdfaf','cgaa','kfddq']
}

df = pd.DataFrame(data, columns=['column1','column2','column3'])

def sqrtM(x):
    return x*x

sqrt2 = lambda x: x*x

print(df)

print(df['column2'].unique())

print(df['column2'].nunique())

print(df['column2'].value_counts())

print(df['column1'].apply(sqrtM))

print(df['column1'].apply(sqrt2))

print(df['column3'].apply(len))


print(df.sort_values('column2'))
