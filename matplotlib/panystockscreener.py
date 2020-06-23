import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web
import pandas_datareader.tiingo as tiingo
from pathlib import Path
import pandas_datareader.nasdaq_trader as nasdaq

api_key = 'ba3ba238018b549a0b4f1c875617fd703829a5a5'

## 获取股票代码
def getStockSymbols():
    my_file = Path("E:\\trade\\quntityTrade\\matplotlib\\nasdqcode.csv")
    if my_file.is_file():
        sym_list = pd.read_csv('.\\nasdqcode.csv')
        return sym_list['Symbol']
    else:
        symbols = nasdaq.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)
        symbols.to_csv('nasdqcode.csv')
        return symbols['Symbol']
## 
def getStock(stock, start, end):
    df = web.DataReader(name=stock, data_source='yahoo',
    start=start, end=end)
    
    adjClose = df['Adj Close'].mean()
    adjVolume = df['Volume'].mean()
    if (adjClose < 1 or adjClose >= 1 and adjClose <= 4) and adjVolume > 1000000:
        csvStr = "E:\\trade\\quntityTrade\\data\\{}.csv"
        df.to_csv(csvStr.format(stock))
        print(stock)
    
if __name__ == "__main__":
    try:
        print('start to fetch data......')
        startTime =  datetime.today() - timedelta(days=70)
        endTime = datetime.today()
        stockList = getStockSymbols()
        for code in stockList:
            getStock(code, startTime, endTime)
        print('finished!!!!!')
    except Exception as e:
        print('except', e)
    pass