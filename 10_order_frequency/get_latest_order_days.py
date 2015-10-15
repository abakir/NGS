import pandas as pd
from datetime import datetime
import time
df = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\orders_export.csv')

def getDate(data):
    return pd.to_datetime(datetime.strptime(data[:10], '%Y-%m-%d')).date()
    

def diffDates(data):
    return (today - data).days
    
# take required fields
df1=df[['Email', 'Created at' ]]

#let there be only one row for each order
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)
df1.columns = ['Email', 'Date']

df1['Date'] = df1.Date.apply(getDate)

df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

today = pd.to_datetime(datetime.strptime(time.strftime("%Y-%m-%d"), '%Y-%m-%d')).date()

df1['Days'] = df1.Date.apply(diffDates)

df1 = df1.sort(['Email', 'Days'])
df1= df1.reset_index().drop('index',1)
df2 = df1.groupby(['Email'], axis=0, as_index=False).min()

df3 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\customers_export.csv")
df2 = df2.merge(df3, on = ['Email'], how = 'inner')

df2 = df2[['Email', 'Date', 'Days', 'First Name', 'Last Name']]

for i in range(0, max(df2.index)+1):
    df2.loc[i, 'Name'] = df2.loc[i, 'First Name'] + " " + df2.loc[i, 'Last Name']
    
df2 = df2[['Email' , 'Days', 'Name']]
df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\latest_order.csv',index = False)
