# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
import time
from flask import jsonify

# url = 'https://www.google.com/search?q=bitcoin+price+usd'
# HTML = requests.get(url)
# soup = BeautifulSoup(HTML.text, 'html.parser')
# text = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text
def get_crypto_price(url):
    # url = 'https://www.google.com/search?q=litecoin+price+usd'

    HTML = requests.get(url)

    soup = BeautifulSoup(HTML.text, 'html.parser')

    text = soup.find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs = {'class': 'BNeawe iBp4i AP7Wnd'}).text
    return text

def getCrypto():
    bitcoin = get_crypto_price('https://www.google.com/search?q=bitcoin+price+usd')
    litecoin = get_crypto_price('https://www.google.com/search?q=litecoin+price+usd')
    bitcoinCash = get_crypto_price('https://www.google.com/search?q=bitcoin+cash+price+usd')
    ethereum = get_crypto_price('https://www.google.com/search?q=ethereum+price+usd')
    prices = {
        "bitcoin": bitcoin,
        "litecoin": litecoin,
        "bitcoinCash": bitcoinCash,
        "ethereum": ethereum
    }
    return jsonify(prices = prices)

def getCryptoLKR():
    bitcoin = get_crypto_price('https://www.google.com/search?q=bitcoin+price+lkr')
    litecoin = get_crypto_price('https://www.google.com/search?q=litecoin+price+lkr')
    bitcoinCash = get_crypto_price('https://www.google.com/search?q=bitcoin+cash+price+lkr')
    ethereum = get_crypto_price('https://www.google.com/search?q=ethereum+price+lkr')
    prices = {
        "bitcoin": bitcoin,
        "litecoin": litecoin,
        "bitcoinCash": bitcoinCash,
        "ethereum": ethereum
    }
    return jsonify(prices = prices)

def getMoneyValue():
    LKR = get_crypto_price('https://www.google.com/search?q=usd+price+lkr')
    IR = get_crypto_price('https://www.google.com/search?q=usd+price+ir')
    AuD = get_crypto_price('https://www.google.com/search?q=usd+price+aud')
    Yuan = get_crypto_price('https://www.google.com/search?q=usd+price+yuan')
    Euro = get_crypto_price('https://www.google.com/search?q=usd+price+euro')
    SD = get_crypto_price('https://www.google.com/search?q=usd+price+singapore')
    Yen = get_crypto_price('https://www.google.com/search?q=usd+price+JAPAN')
    
    prices = {
        "LKR": LKR,
        "IR": IR,
        "AuD": AuD,
        "Yuan": Yuan,
        "Euro": Euro,
        "SD": SD,
        "Yen": Yen
    }
    return jsonify(prices = prices)

# def getCryptoPrice():
#     #python -m pip install requests
#     headers = {
#     'Accepts': 'application/json',
#     'X-CMC_PRO_API_KEY': '77aab18d-a932-454c-8423-ab051e388a06',
#     }

#     params = {
#         'start': '1',
#         'limit': '5',
#         'convert': 'USD'
#     }

#     url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

#     json = requests.get(url, params = params, headers = headers).json()
#     # print(json)
#     coins = json['data']
#     array = []
#     for x in coins:
#         array.append([x['symbol'], round(x['quote']['USD']['price'],2)])
#     print(array)