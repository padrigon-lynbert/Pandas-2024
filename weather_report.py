import pandas as pd
from icecream import ic

df = pd.read_csv("Data/nyc_weather.csv")
print(df)

# print(len(df["Temperature"]))