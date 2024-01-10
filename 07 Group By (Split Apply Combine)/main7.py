import pandas as pd
from icecream import ic

df = pd.read_csv('07 Group By (Split Apply Combine)/weather_by_cities.csv')
grouped = df.groupby('city')

for city in grouped:
    city
#find maximum temp in each of the cities
import pandas as pd
from icecream import ic

df = pd.read_csv('07 Group By (Split Apply Combine)/weather_by_cities.csv')
grouped = df.groupby('city')

for city in grouped:
    city

#find maximum temp in each of the cities
grouped.get_group('paris')
#find average wind speed per city
grouped.max()
grouped.describe()

import matplotlib.pyplot as plt

grouped.plot()
plt.show()

for city, city_df in grouped:
    city; city_df

grouped.get_group('paris').plot()





#find average wind speed per city

