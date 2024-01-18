import pandas as pd

y = pd.Period('2016')

y.start_time
y.end_time
y.day_of_week

m = pd.Period('2024-01', freq='M')
m = m+1
m.end_time

d = pd.Period('2024-01-18', freq='d')
d+1

h = pd.Period('2024-01-18 20:00', freq='d')
h = h+1
h.end_time
# h+pd.offsets.Hour(1)

q = pd.Period('2027Q1')
q

# idx = pd.period_range('2017','2024', freq='Q-Jan')
idx = pd.period_range('2017', periods=10, freq='Q-Jan')
idx

import numpy as np

rng = np.random.default_rng()

df = rng.integers(1,10,len(idx))
df

ps = pd.Series((df), idx)

pst = ps.to_timestamp()
pst = pst.to_period()
pst

df = pd.read_csv('18 Period and PerionIndex/wmt.csv')
df.set_index('Line Item', inplace=True)
df = df.T
df.index = pd.PeriodIndex(df.index, freq='Q-Jan')

df['start date'] = df.index.map(lambda x: x.start_time)
df