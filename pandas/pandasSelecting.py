import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index = ['A','B','C'], columns =['column1','column2','column3'])

print(df)

print(df['column1'])

print(df[['column1','column2']])

print(df.loc['A'])

print(df.iloc[2])

print(df.loc['A','column1'])

df['column4'] = pd.Series(randn(3),['A','B','C'])
print("\n",df)

df['column5'] = df['column1'] + df['column3']
print('\n',df)

print('\n',df.drop('column5',axis=1))
print('\n',df)

df.drop('column5',axis=1,inplace=True)
print('\n',df)