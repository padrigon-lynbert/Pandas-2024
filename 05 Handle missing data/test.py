import pandas as pd
from icecream import ic 

df = pd.read_csv('05 Handle missing data\weather_data.csv', parse_dates=['day'])
df = df.set_index('day')

dt = pd.date_range('2017-01-01', '2017-01-11')
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)

df = round((df.interpolate(method='time')), 2)

average_temperature = df.temperature.mean()
print(df)

# df.to_csv('new_data')