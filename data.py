import pandas as pd
import csv
df=pd.read_csv('final.csv')
print(df.shape)
del df['hyperlink']
print(df.shape)
print (list(df))
df=df.rename({
    "light_years_from_earth":"light_year"
},axis="columns")
print(list(df))
df.to_csv("main.csv")