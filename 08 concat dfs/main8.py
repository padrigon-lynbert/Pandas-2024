import pandas as pd

ph_weather = pd.DataFrame({
    'city': ['caloocan', 'manila', 'bulacan'],
    'temperature': [36,38,34],
    'humidity': [60,40,80]
})

india_weather = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'banglore'],
    'temperature': [32,45,30],
    'humidity': [80,60,78]
})
india_weather

df = pd.concat([ph_weather, india_weather])
df1 = pd.concat([ph_weather, india_weather], ignore_index=True)
df2 = pd.concat([ph_weather, india_weather], keys=['ph', 'india'])
df2.loc['ph']


#append it as a column not a row

temperature_df = pd.DataFrame({
    'city': ['mumbai', 'delhi', 'banglore'],
    'temperature': [32,45,30]
}, index=[1,2,3])
windspeed_df = pd.DataFrame({
    'city': ['delhi', 'banglore', 'mumbai'],
    'temperature': [8,7,9],
}, index=[2,3,1])

df = pd.concat([temperature_df, windspeed_df], axis=1)

s = pd.Series(['humid','dry','rain'], name='event')
df = pd.concat([df, s], axis=1)
