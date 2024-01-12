import pandas as pd

df = pd.read_excel('12 Stack Unstack/stocks.xlsx', header=([0,1]))
df_stacked = df.stack()
df_stacked

df = pd.read_excel('12 Stack Unstack/stocks_3_levels.xlsx', header=[0,1,2])
df.stack(level=2)