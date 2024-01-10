import pandas as pd

# pivot summarize/aggregate data inside a dataframe

df = pd.read_csv('10 Pivot table/weather.csv')
df.pivot(index='date', columns='city')
df.pivot(index='date', columns='city', values='humidity')

df = pd.read_csv('10 Pivot table/weather2.csv')
df.pivot_table(index='city', columns='date', aggfunc='count') #aggregated (provide numpy functions(just search) on aggfunc) mean is default
df.pivot_table(index='city', columns='date', margins=True)

df = pd.read_csv('10 Pivot table/weather3.csv')
df['date'] = pd.to_datetime(df['date'])
df.pivot_table(index=pd.Grouper(freq='M', key='date'), columns='city')
