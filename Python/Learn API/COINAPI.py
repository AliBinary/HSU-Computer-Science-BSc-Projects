import requests
currenciesList = ['USD', 'EUR', 'JPY', 'GBP',
                  'CNY', 'AUD', 'CAD', 'CHF', 'HKD', 'SGD']
cryptoList = ['BTC', 'ETH', 'USDT', 'XRP',
              'BNB', 'USDC', 'ADA', 'DOGE', 'SOL', 'TRX']

kid = "E443155E-FBFA-437E-81E4-5AE5E64E1456"
currency = "USD"
crypto = "BTC"

r = requests.get(
    "https://rest.coinapi.io/v1/exchangerate/%s/%s?apikey=%s" % (crypto, currency, kid)).json()
print(r)
