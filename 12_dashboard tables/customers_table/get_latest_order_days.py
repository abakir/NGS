import pandas as pd
from datetime import datetime
import time
df = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\data\orders_export.csv')

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
    
df2 = df2[['Email' , 'Days']]
df2.columns =['Email', 'Days from Last order']
df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\latest_order.csv',index = False)
