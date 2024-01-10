import pandas as pd

df1 = pd.DataFrame({
    "city": ["new york","chicago","san francisco"],
    "temperature": [21,14,35,66],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando", 'baltimore'],
    "humidity": [65,68,75,78],
})

df3 = pd.merge(df1, df2, on='city') # will only merge the common city(elements between two sets) inner merge(default)
df4 = pd.merge(df1, df2, on='city', how="outer") #get union or outer merge
# others right, left, read documentations

df5 = pd.merge(df1, df2, on='city', how="outer", indicator=True) # see where in venn diagram

df6 = pd.merge(df4, df5, on='city', how="outer", suffixes=('left','_right'))
df6