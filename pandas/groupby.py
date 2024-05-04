import pandas as pd 
import numpy as np

personeller = {
    'personel':['ali yilmaz','ayse duran','zeynep demir','ahmet parlak','fatma kaya','mehmet duran'],
    'departman':['insan kaynaklari','bilgi islem','satin alma','bilgi islem','muhasebe','yonetim'],
    'yas':['25','35','46','51','41','39'],
    'semt':['kadikoy','tuzla','maltepe','zeytinburnu','maltepe','eminonu'],
    'maas':[54000,45000,52104,49321,43321,65329],
}

df = pd.DataFrame(personeller)

# print(df)

groupDepartmant = df.groupby('departman')

# print(groupDepartmant.groups)

# for name in groupDepartmant:
#     print(name)

# print(df.groupby('semt').get_group('maltepe'))

# print(df.groupby('departmant').sum())

print(df.groupby('departman')['maas'].max()['bilgi islem'])

print(df.groupby('departman')['maas'].agg([np.sum,np.mean,np.max,np.min]))