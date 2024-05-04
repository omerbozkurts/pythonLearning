import pandas as pd

customers = {

    'customerId' : [1,3,4,5,9,23],
    'name' : ['ali','ayse','ahmet','fatma','mehmet','zeynep'],
    'surname' : ['demir','yilmaz','duran','kaya','bakan','gunduz'],

}

orders = {

    'orderId' : [32,55,15,53,63,89],
    'customerId' : [9,5,2,1,4,8],
    'orderDate' : ['11.11.2020','12.02.2020','27.09.2020','05.03.2020','20.01.2021','16.8.2020']

}

dfCustomers = pd.DataFrame(customers,columns = ['customerId','name','surname'])
dfOrders = pd.DataFrame(orders, columns=['orderId','customerId','orderDate'])

# print(dfCustomers)
# print(dfOrders)

# mergeTable = pd.merge(dfCustomers,dfOrders,how ='inner')
# mergeTable = pd.merge(dfCustomers,dfOrders,how = 'left')
mergeTable = pd.merge(dfCustomers,dfOrders,how = 'outer')

print(mergeTable)