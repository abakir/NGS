import pandas as pd

location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\price.csv'
df = pd.read_csv(location)

#remove products whose revenue is 0
df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
#get products which make 80% sales
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break

df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv', index=False)

#-----------------------------------------------------------------------------------------------------------

location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\totalrevenue.csv'
df = pd.read_csv(location)

df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break

df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_totalrevenue.csv', index=False)

#-----------------------------------------------------------------------------------------------------------------

location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\itemcount.csv'
df = pd.read_csv(location)

df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break

df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_itemcount.csv', index=False)