import pandas as pd
from icecream import ic as print

df = pd.read_csv("01 Intro/nyc_weather.csv").fillna(0)
# df.fillna(0, inplace=True)
# print(df["Temperature"].max())s

precipitation = list(df["EST"] [df["PrecipitationIn"] == "T"])
precipitation_type = list(df["Events"] [df["Events"] != 0])

print(f"Rain == True")
for i in range(len(precipitation)):
    print(f"{i} {precipitation[i]}: {precipitation_type[i]}")

print(f"Humidity Average: {round(df['Humidity'].mean(), 2)}")