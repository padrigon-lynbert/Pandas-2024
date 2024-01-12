import pandas as pd

df = pd.read_csv('14 datetimeIndex/appl.csv', parse_dates=['Date'], index_col='Date')

df.Close.mean()

import matplotlib.pyplot as plt

df.Close.resample('M').mean().plot()
df.Close.resample('M').mean().plot(kind='density')
df.Close.plot()
plt.show()

