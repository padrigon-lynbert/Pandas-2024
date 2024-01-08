import pandas as pd
from icecream import ic
import numpy as np 

df = pd.read_csv('06 Replace missing data/weather_data.csv')

new_df = df.replace({
    'temperature': -99999,
    'windspeed': -99999,
    'event': '0'
}, np.NaN)

new_df = df.replace({
    -99999: np.NaN,
    '0': 'Sunny'
})
new_df  
#.interpolate(method='linear') kjlnfg