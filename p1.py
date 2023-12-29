import pandas as pd
from icecream import ic as print

df = pd.read_csv("Data/nyc_weather.csv").fillna(0)
# df.fillna(0, inplace=True)
# print(df["Temperature"].max())
# print(df)
print("Rain == True")
print(df["EST"] [df["PrecipitationIn"] == "T"])
print(f"Humidity Average: {round(df['Humidity'].mean(), 2)}")