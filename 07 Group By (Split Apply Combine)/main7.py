import pandas as pd
from icecream import ic

df = pd.read_csv('07 Group By (Split Apply Combine)/weather_by_cities.csv')
grouped = df.groupby('city')

for city in grouped:
    city
#find maximum temp in each of the cities

#find average wind speed per city

