import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas_datareader.data as web


plt.style.use('ggplot')
start = dt.datetime(2019, 11, 30)
end = dt.datetime(2020, 5, 1)
df = web.DataReader('USO', 'yahoo', start, end)
df.to_csv('uso.csv')