import pandas as pd
from icecream import ic 

# READ TO CSV

# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv")
#changes(csv)

# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", skiprows=1).set_index('tickers')
# or 
# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", header=1).set_index('tickers')

# changes(csv)
# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", header=None, names=['tickers','eps','revenue','price','people'])

# changes(csv) restored

#specific # of rows
# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", nrows=3)


#any values -> Nan
# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", na_values=['not available','n.a.'])
# df = pd.read_csv("04 Read or write excell and csv files/stock_data.csv", na_values={
#     'eps': ['not available', 'n.a.'],
#     'revenue': ['not available', 'n.a.', -1],
#     'people': ['not available', 'n.a.']
# })
# print(df)


# WRITE TO CSV
# df.to_csv('new.csv', index=None) #copy of df
# df.to_csv('new.csv', columns=['tickers', 'price'], index=None)

# def convert_people_cell(cell):
#     if cell == 'n.a.': return "sam altman"
#     return cell
# def convert_eps_cell(cell):
#     if cell == 'not available': return None
#     return cell
# df = pd.read_excel('04 Read or write excell and csv files/stock_data.xlsx', converters={
#     'people': convert_people_cell,
#     'eps': convert_eps_cell
# })
# df.to_excel('new.xlsx', index=None, startrow=1, startcol=2)

# df_stocks = pd.DataFrame({
#     'tickers': ['GOOGL', 'WMT', 'MSFT'],
#     'price': [845, 65, 64 ],
#     'pe': [30.37, 14.26, 30.97],
#     'eps': [27.82, 4.61, 2.12]
# })
# df_weather =  pd.DataFrame({
#     'day': ['1/1/2017','1/2/2017','1/3/2017'],
#     'temperature': [32,35,28],
#     'event': ['Rain', 'Sunny', 'Snow']
# })

# with pd.ExcelWriter('stocks_weather.xlsx') as writer:
#     df_stocks.to_excel(writer, sheet_name='stonks')
#     df_weather.to_excel(writer, sheet_name='weather')