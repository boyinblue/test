import requests
import json
import matplotlib.pyplot as plt

days = list(range(10))
url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&count=10"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)

st_python = json.loads(response.text)

#print(response.text)
#print(st_python)

def select_opening_price(abc):
    return abc['opening_price']
    
def select_high_price(abc):
    return abc['high_price']

def select_low_price(abc):
    return abc['low_price']

def select_trade_price(abc):
    return abc['trade_price']

def select_date_time_utc(abc):
    return abc['candle_date_time_utc']
    
opening_price=list(map(select_opening_price, st_python))
high_price=list(map(select_high_price, st_python))
low_price=list(map(select_low_price, st_python))
trade_price=list(map(select_trade_price, st_python))
candle_date_time_utc=list(map(select_date_time_utc, st_python))

plt.plot(days, opening_price)
plt.plot(days, high_price)
plt.plot(days, low_price)
plt.plot(days, trade_price)

print(candle_date_time_utc)

plt.savefig(candle_date_time_utc[0] + ".png")

plt.show()
