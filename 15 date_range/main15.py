import pandas as pd

df = pd.read_csv('15 date_range/appl.csv')
df.head()

rng = pd.date_range(start='6/1/2017', end='6/30/2017',freq='B')
df.set_index(rng, inplace=True)
df