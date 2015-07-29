from pandas import read_csv
import pandas as pd

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\groupedprod.csv'

df = pd.read_csv(location)

df2 = df.sort('Revenue',ascending = False)
df2 = df2.reset_index().drop('index', 1)

colnames = ['Product']
df_new = pd.DataFrame(columns=colnames)
df_new = df_new.fillna(0)

sum = 0
min = math.ceil(df2[['Revenue']].sum()*0.8)
for i in range(0, max(df2.index)+1):
    if(sum < min):
        sum = sum + df2.loc[i, 'Revenue']
    else:
        df_new = df2[0:i-1]
        break
        
        
df_new.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\\imp_products.csv",sep=",",index=False)
