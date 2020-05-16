import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web



style.use('ggplot')
df = pd.read_csv('uso.csv', parse_dates=True, index_col=0)
df['200ma'] = df['Adj Close'].rolling(window=200, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()
df.to_csv('uso_ma.csv')
df=pd.read_csv('uso_ma.csv', parse_dates=True, index_col=0)
ma200=df['200ma']
ma50=df['50ma']
close=df['Adj Close']
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(close, label='close price')
ax.plot(ma200, '--*', label='200ma')
ax.plot(ma50, '--*', label='50ma')
ax.legend(loc='best')
plt.show()