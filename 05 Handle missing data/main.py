import pandas as pd
from icecream import ic

df = pd.read_csv("05 Handle missing data/weather_data.csv", parse_dates=['day'])
df.set_index('day', inplace=True)

print(df.dropna())
print(df.dropna(how='all'))
print(df.dropna(thresh=1))
dt = pd.date_range('2017-01-01',"2017-01-11")
idx = pd.DatetimeIndex(dt)
df = df.reindex(idx)


#fillna
df = df.fillna(0) #fills entire dataframe
print(df)
#using dictionary
df = df.fillna({
    'temperature': 0.0,
    'windspeed': 0.0,
    'event': 'no event'
})
#carrying values
df = df.fillna(method='ffill')#previous value
df = df.fillna(method='bfill')#next value
#and etc just read documentation bro

#interpolate
df.interpolate()
print(df)
