import pandas as pd
import re
location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\orders_export-10.csv'
df = pd.read_csv(location)

df1=df[['Email', 'Created at' ]]

df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

for i in range(0,max(df1.index)+1):
    (df1.iloc[i,1]) = (df1.iloc[i,1])[:10]
    
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

for i in range(0,max(df1.index)+1):
    df1.loc[i,'Difference'] = -1
    
df1.columns=['Email', 'Date', 'Difference']

df1['Date'] =pd.to_datetime(df1.Date)
df1=df1.sort(['Email', 'Date'])
df1= df1.reset_index().drop('index',1)

for i in range(0,max(df1.index)):
    if(df1.iloc[i,0]==df1.iloc[i+1,0]):
        df1.iloc[i+1,2]=(df1.iloc[i+1,1]-df1.iloc[i,1]).days
            
            
df2=pd.DataFrame(columns=['Email', 'Average'])

j=0
n=1
tot=0
for i in range(0,max(df1.index)):
    if(df1.iloc[i,0]==df1.iloc[i+1,0]):
        n=n+1
        tot=tot+df1.iloc[i+1,2]
    else:
        df2.loc[j,'Email']=df1.iloc[i,0]
        df2.loc[j,'Average']= tot/n
        j=j+1
        tot=0
        n=1
            
            
df2.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\\frequency.csv",index=False)