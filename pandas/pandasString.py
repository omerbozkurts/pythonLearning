import pandas as pd

data = pd.read_csv('dataset/MVAV.csv')

# print(data)

data['Month '] = data['Month '].str.lower()

# print(data.head(10))

# data['index'] = data['Month '].str.find("jan")

# data = data['Month '].str.contains('apr')

print(data.head(10))