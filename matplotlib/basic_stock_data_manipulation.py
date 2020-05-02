import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web



style.use('ggplot')
df = pd.read_csv('uso.csv', parse_dates=True, index_col=0)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['20ma'] = df['Adj Close'].rolling(window=20, min_periods=0).mean()
df.to_csv('uso_ma.csv')
df=pd.read_csv('uso_ma.csv', parse_dates=True, index_col=0)
ma100=df['100ma']
ma20=df['20ma']
close=df['Adj Close']
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(close, label='close price')
ax.plot(ma100, '--*', label='100ma')
ax.plot(ma20, '--*', label='20ma')
ax.legend(loc='best')
plt.show()