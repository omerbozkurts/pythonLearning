import pandas as pd


df = pd.read_csv('dataset/MVAV.csv')
print(df)

df = pd.read_json('dataset/data.json')
print(df)

df = pd.read_excel('dataset/data.xlsx')
print(df)