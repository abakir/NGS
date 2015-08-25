import pandas as pd

location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv'
df = pd.read_csv(location)
location='C:\Users\saisree849\AppData\Roaming\Skype\My Skype Received Files\\vend-total_revenue-sales_summary-by-month-2.csv'
df1 = pd.read_csv(location)

#creating column names 
col=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ind = [0,1,2,3]

df2=pd.DataFrame(index=ind,columns=col)

t12=0
t13=0
t14=0
p12=0
p13=0
p14=0
#adding all positive revenues
for i in range(1,13):
    if(df1.iloc[0,i]>0):
        p12=p12+1
        t12=t12+df1.iloc[0,i]
for i in range(13,25):
    if(df1.iloc[0,i]>0):
        p13=p13+1
        t13=t13+df1.iloc[0,i]
for i in range(25,37):
    if(df1.iloc[0,i]>0):
        p14=p14+1
        t14=t14+df1.iloc[0,i]
    
#getting monthly average
t12=t12/p12
t13=t13/p13
t14=t14/p14

#creating seasonal index for each year
for i in range(1,13):
    df2.iloc[0,i-1]=df1.iloc[0,i]/t12
for i in range(13,25):
    df2.iloc[1,i-13]=df1.iloc[0,i]/t13
for i in range(25,37):
    df2.iloc[2, i-25]=df1.iloc[0,i]/t14
    
#getting average SI for each month
for i in range(0,12):
    t=0
    p=0
    for j in range(0,max(df2.index)):
        if(df2.iloc[j,i]>0):
            p=p+1
        t=t+df2.iloc[j,i]
    df2.iloc[max(df2.index), i] = t/p
    
df=df.drop('Revenue',axis=1)
df.loc[max(df.index)+1,'Product']='SeasonalIndex'

k=4
for j in range(1,37):
    df.iloc[max(df.index), j] = df2.loc[3,k]
    k=k+1
    if(k==13):
        k=1
        
df.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_seasonalindex.csv', index=False)