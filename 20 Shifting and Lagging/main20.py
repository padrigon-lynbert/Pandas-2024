import pandas as pd
import numpy as np

df = pd.read_csv('20 Shifting and Lagging/fb.csv', parse_dates=['Date']).set_index('Date')
df.shift(1)
df.shift(-1)
df['prev day price'] = df['Price'].shift(1)
df['1 day change'] = df.Price - df['prev day price']
df['5days return'] = (df['Price'] - df['Price'].shift(5)) *100/df['Price'].shift(5)
df

simplified_df = df['Price']
simplified_df.index = pd.date_range('15-Aug-17', periods=10, freq='B')

d = df.Price
d = pd.Series.to_frame(df.Price)
df.tshift(1)
#tshift() wont work on newer versions of pandas