import pandas as pd

df = pd.read_csv('19 Timezones/msft.csv', parse_dates=['Date Time'],header=1); df
df.set_index('Date Time', inplace=True)
df.index
df = df.tz_localize(tz='America/New_York')
df = df.tz_localize(tz='Asia/Manila')
df
from pytz import all_timezones

all_timezones

rng = pd.date_range(start='1/1/2024', periods=10, freq='Q', tz='Asia/Manila')
rng2 = pd.date_range(start='1/1/2024', periods=10, freq='Q', tz='dateutil/Asia/Manila') #date util use all different time zones available in your OS
rng2


rng = pd.date_range(start='1/1/2024', periods=10, freq='30min', tz='Asia/Manila')
s = pd.Series(range(len(rng)), index=rng)

b = s.tz_convert('Europe/Berlin')
p = s.tz_convert('Asia/Manila')

p+b