import pandas as pd 
from icecream import ic 

#csv
# df = pd.read_csv("./03 Different ways of creating dataframe//weather_data.csv")
# ic(df)


#excel
# df = pd.read_excel("./03 Different ways of creating dataframe//weather_data.xlsx"); ic(df)

# dictionary
# data = {
#     'name': [7, 'kjndfgdf'],
#      'slot': [1, 'hgjhguyg'],
#      'lksmdfsd': [2, 'kjkjn'],
#      'sdfsd': [3, 'kjub'],
#      '3': [1, 'bsdf']
# }
# ic(pd.DataFrame(data).set_index('name'))

#tuple

# data = [
#     (2017,32,6,'sunny'),
#     (2017,35,7,'sunny')
# ]
# ic(pd.DataFrame(data, columns = ['day','temp','ws','E']).set_index('day'))

# list of dictionaries
data = [
    {'day': '2017-01', 'event':'summy'},
    {'day':'2017-02', 'event': 'rain'}
]
ic(pd.DataFrame(data))
