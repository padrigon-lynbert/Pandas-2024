import pandas as pd
from icecream import ic

df = pd.read_csv("02 dataframe basics/weather_data.csv")

# ic(df.head(3), df.tail(3))

# data = {
#     "name": ["Lynbert Steeve", "Padrigon", "Orilla"],
#     "type" : ["first name", "lastname", "middle name"]
# }; data = (pd.DataFrame(data)); ic(data)

# col, row = data.shape

# ic(df[2:5])
# print(df.columns); ic(df.day) # df['day']

# only certain or specified column(s)
# print(df[['event', 'day']])



# dataframe operations
# print(df.temperature.max())
# print(df.temperature.std(), "\n\n")
# print(round(df.temperature.describe(), 2))

# ic(df[["day", 'temperature' ]][df.temperature >= 30])

import numpy as np 
# var = list(pd.Series(np.random.default_rng().integers(1,100,100)))


# var = list(pd.Series(np.random.randint(1,100,100)))
# less_ten = [index for i, index in enumerate(var) if(index<10)]



# print(df.index)

ic(df.set_index('day'), "\n")
ic(df.set_index(df.day))

df.set_index('day', inplace=True)
# print(df.loc['1/5/2017'])

ic(df)

df.reset_index(inplace=True)

ic(df)