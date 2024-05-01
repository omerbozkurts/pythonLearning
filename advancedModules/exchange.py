import requests
import json


api_key = '399db66d34fe88db93bd00df'
api_url = 'https://v6.exchangerate-api.com/v6/399db66d34fe88db93bd00df/latest/'


currencyToSell = input('From:')
currenctToBuy = input('To:')
amount = int(input('amount:'))

excValue = requests.get(api_url + currencyToSell)

excValueJson = json.loads(excValue.text)

print(f'1 {currencyToSell} {excValueJson['conversion_rates'][currenctToBuy]} {currenctToBuy}')
print(f'exchange value is {excValueJson['conversion_rates'][currenctToBuy]*amount} {currenctToBuy}')