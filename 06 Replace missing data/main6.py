import pandas as pd
from icecream import ic
import numpy as np 

df = pd.read_csv('06 Replace missing data/weather_data.csv')

# new_df = df.replace({
#     'temperature': -99999,
#     'windspeed': -99999,
#     'event': '0'
# }, np.NaN)

# new_df = df.replace({
#     -99999: np.NaN,
#     '0': 'Sunny'
# })
# new_df  
#.interpolate(method='linear')

# with symbols
# regex to replace non-numeric characters

new_df = df.replace({
    'temperature': '[A-Za-z]',
    'windspeed': '[A-Za-z]',
}, '', regex=True)
new_df


#replace list values in a list of values

df = pd.read_csv('06 Replace missing data/grades.csv').replace(['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
df