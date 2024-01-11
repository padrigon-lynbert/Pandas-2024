import pandas as pd

df = pd.read_csv('11  Reshape dataframe using melt/weather.csv')
df = pd.melt(df, id_vars=['day'], var_name="city", value_name='temperature')
df
df[df['city']=='chicago']