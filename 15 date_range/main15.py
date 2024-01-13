import pandas as pd

df = pd.read_csv('15 date_range/appl.csv')
df.head()

rng = pd.date_range(start='6/1/2017', end='6/30/2017',freq='B')
df.set_index(rng, inplace=True)
df
import matplotlib.pyplot as plt
df.Close.plot()
plt.show()

df["2017-06-01":"2017-06-15"].Close.mean()
df.asfreq('W', method="pad")

rng = pd.date_range('6-1-2004', periods=20, freq='D')

import numpy as np
np.random.randint(1,10,len(rng))
ts = pd.Series(np.random.randint(1,10,len(rng)), index=rng)
ts