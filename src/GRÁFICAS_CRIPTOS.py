import pandas as pd
import requests
import csv

import matplotlib.pyplot as plt


""" A continuación vamos a crear una función para crear gráficos desde la Api de la famosa página de Binance."""

symbol = 'BTCUSDT'

tick_interval = '1d'


def obtener_velas(start='', symbol='BTCUSDT', tick_interval='1d', limit=1000):
    
    base_url = 'https://api.binance.com/'
    endpoint = 'api/v3/klines?'
    
    if start:
        query = 'symbol=' + symbol + '&interval=' + tick_interval + '&startTime=' + str(start) +'&limit='+str(limit)
    else:
        query = 'symbol=' + symbol + '&interval=' + tick_interval +'&limit='+str(limit)
        
    velas = requests.get(base_url + endpoint + query).json()
    
    return velas, velas[-1][6]


def obtener_velas_inicio(symbol, tick_interval):  # Devuelve una lista de velas, cada vela es una lista tb
    
    start=1502942400000  # 17 de agosto de 2017
    _, last_time = obtener_velas(start='', symbol=symbol , tick_interval=tick_interval, limit=1)
    
    velas = []
    while start < last_time:
        i_velas, next_hop = obtener_velas(start, symbol, tick_interval)
        velas = velas + i_velas
        start = next_hop
        
    return velas


""" Sacamos la gráfica del BITCOIN """


velas = obtener_velas_inicio(symbol, tick_interval)
columns=['open_time','open', 'high', 'low','close','volume','close_time','quote','trades',
         'takers_buy_base','takers_buy_quote','ignore']
bitcoin = pd.DataFrame(velas, columns=columns)

bitcoin = bitcoin.sort_values('close_time')
bitcoin.drop_duplicates(keep='last')
bitcoin = bitcoin.astype(float)
bitcoin.info()

bitcoin['close_time'] = pd.to_datetime(bitcoin['close_time'], unit='ms')
bitcoin['close_time'] = bitcoin['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
bitcoin = bitcoin.set_index('close_time')

bitcoin.drop('ignore', axis=1, inplace=True)

bitcoin['close'].plot(figsize=(20,8), label='BTCUSDT')
plt.title('Precio de BTC/USDT')
plt.legend()
plt.grid()

""" Sacamos la gráfica del CARDANO """

symbol = 'ADAUSDT'

cardano = pd.DataFrame(velas, columns=columns)

cardano = cardano.sort_values('close_time')
cardano.drop_duplicates(keep='last')
cardano = cardano.astype(float)
cardano.info()

cardano['close'].plot(figsize=(20,8), label='ADAUSDT')
plt.title('Precio de ADA/USDT')
plt.legend()
plt.grid()

cardano['close_time'] = pd.to_datetime(cardano['close_time'], unit='ms')
cardano['close_time'] = cardano['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
cardano = cardano.set_index('close_time')

cardano.drop('ignore', axis=1, inplace=True)

cardano['close'].plot(figsize=(20,8), label='ADAUSDT')
plt.title('Precio de ADA/USDT')
plt.legend()
plt.grid()

""" Sacamos la gráfica del BNB """

symbol = 'BNBUSDT'

bnb = pd.DataFrame(velas, columns=columns)

bnb = bnb.sort_values('close_time')
bnb.drop_duplicates(keep='last')
bnb = bnb.astype(float)
bnb.info()

bnb['close'].plot(figsize=(20,8), label='BNBUSDT')
plt.title('Precio de BNB/USDT')
plt.legend()
plt.grid()


bnb['close_time'] = pd.to_datetime(bnb['close_time'], unit='ms')
bnb['close_time'] = bnb['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
bnb = bnb.set_index('close_time')

bnb.drop('ignore', axis=1, inplace=True)

""" Sacamos la gráfica del ETHEREUM """

symbol = 'ETHUSDT'

ethereum = pd.DataFrame(velas, columns=columns)

ethereum = ethereum.sort_values('close_time')
ethereum.drop_duplicates(keep='last')
ethereum = ethereum.astype(float)
ethereum.info()

ethereum['close'].plot(figsize=(20,8), label='BNBUSDT')
plt.title('Precio de BNB/USDT')
plt.legend()
plt.grid()

ethereum['close_time'] = pd.to_datetime(ethereum['close_time'], unit='ms')
ethereum['close_time'] = ethereum['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
ethereum = ethereum.set_index('close_time')

ethereum.drop('ignore', axis=1, inplace=True)

""" Sacamos la gráfica del AVA """

symbol = 'AVAUSDT'

ava = pd.DataFrame(velas, columns=columns)

ava = ava.sort_values('close_time')
ava.drop_duplicates(keep='last')
ava = ava.astype(float)
ava.info()

ava['close'].plot(figsize=(20,8), label='BNBUSDT')
plt.title('Precio de BNB/USDT')
plt.legend()
plt.grid()

ava['close_time'] = pd.to_datetime(ava['close_time'], unit='ms')
ava['close_time'] = ava['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
ava = ava.set_index('close_time')

ava.drop('ignore', axis=1, inplace=True)

""" Sacamos la gráfica del GALA """

symbol = 'AVAUSDT'

gala = pd.DataFrame(velas, columns=columns)

gala = gala.sort_values('close_time')
gala.drop_duplicates(keep='last')
gala = gala.astype(float)
gala.info()

gala['close'].plot(figsize=(20,8), label='BNBUSDT')
plt.title('Precio de BNB/USDT')
plt.legend()
plt.grid()

gala['close_time'] = pd.to_datetime(gala['close_time'], unit='ms')
gala['close_time'] = gala['close_time'].dt.tz_localize('utc').dt.tz_convert('Europe/Madrid')
gala = gala.set_index('close_time')

gala.drop('ignore', axis=1, inplace=True)

