from pandas import read_csv
import pandas as pd
import re

location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv'
df = pd.read_csv(location)
location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_totalrevenue.csv'
df1 = pd.read_csv(location)

t12=0
t13=0
t14=0
for i in range(0,max(df1.index)+1):
    for j in range(1,13):
        t12=t12+df1.iloc[i,j]
    for k in range(13,25):
        t13=t13+df1.iloc[i,k]
    for l in range(25,37):
        t14=t14+df1.iloc[i,l]
        
t12=t12/12
t13=t13/12
t14=t14/12

df2=df.drop('Revenue',axis=1)

df2.loc[max(df2.index)+1,'Product']='SeasonalIndex'

for j in range(1,13):
    t=0
    for i in range(0,max(df1.index)):
        t=t+df1.iloc[i,j]
    df2.iloc[max(df2.index),j]=t/t12
for j in range(13,25):
    t=0
    for i in range(0,max(df1.index)):
        t=t+df1.iloc[i,j]
    df2.iloc[max(df2.index),j]=t/t13
for j in range(25,37):
    t=0
    for i in range(0,max(df1.index)):
        t=t+df1.iloc[i,j]
    df2.iloc[max(df2.index),j]=t/t14
    
df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_seasonalindex.csv', index=False)