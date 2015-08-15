from pandas import read_csv
import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-item_count.csv'
df = pd.read_csv(location)

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-total_revenue.csv'
df1 = pd.read_csv(location)

df=df[0:1706]
df1=df1[0:1706]
df2=df1

for i in range(0,max(df.index)+1):
    for j in range(7,43):
        if(df.iloc[i,j] > 0):
            df2.iloc[i,j] = df1.iloc[i,j]/df.iloc[i,j]
            
df2=df2.drop(df2.columns[[43,44,45,46,47]], axis=1)

for i in range(0,max(df2.index)+1):
    flag=0
    for j in range(7,43):
        if(df2.iloc[i,j] == 0):
            flag+=1
        elif ((flag>0) & (df2.iloc[i,j]>0)):
            for k in range(j-flag, j+1):
                df2.iloc[i,k]=df2.iloc[i,j]
            flag=0
        if ((flag>0) & (j==42)):
            y=j-flag
            for k in range(j-flag+1, j+1):
                df2.iloc[i,k]=df2.iloc[i,y]
        
            
df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-price.csv'
, index=False)