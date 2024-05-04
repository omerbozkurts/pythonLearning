import pandas as pd
import numpy as np

playerDataSet = pd.read_csv('dataset/players.csv')



print(playerDataSet)

playerDataSet['salary'] = pd.DataFrame(np.random.randint(15000,250000,3921))

playerDataSet.to_csv('dataset/Players.csv',index=False)

print(playerDataSet.head(10))

print(playerDataSet.count())

print(len(playerDataSet.index))

print(playerDataSet['salary'].sum())

print(playerDataSet['salary'].mean())

print(playerDataSet['salary'].max())

print(playerDataSet[playerDataSet['salary']==playerDataSet['salary'].max()]['Player'])

print(playerDataSet[(2024-playerDataSet['born'])<=30][['Player','born']])

print(playerDataSet[playerDataSet['Player']=='John Hargis']['collage'])

print(playerDataSet.groupby('collage')['salary'].agg(np.mean))

print(playerDataSet['collage'].nunique())

print(playerDataSet['collage'].value_counts())

playerDataSet = playerDataSet.dropna()

print(playerDataSet[playerDataSet['Player'].str.contains('and')])