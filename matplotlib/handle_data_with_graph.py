import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import pandas_datareader.data as web


df = pd.read_csv('uso.csv', parse_dates=True, index_col=0)
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(df['Volume'], label='volume')
plt.show()