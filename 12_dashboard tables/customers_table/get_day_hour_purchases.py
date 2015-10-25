import pandas as pd
from datetime import datetime
import re

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\orders_export.csv")

df = df[['Name','Email', 'Created at']]
df.columns = ['Name','Email', 'Date']

def getDay(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    data = matchobj.group(1)
    return pd.to_datetime(datetime.strptime(data, '%Y-%m-%d')).date().strftime("%A")

def getHours(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    data = matchobj.group(2)
    num = pd.to_datetime(datetime.strptime(data, '%H:%M:%S')).hour
    if(num < 6):
        return 0
    elif((num >= 6) & (num < 12)):
        return 6
    elif((num >= 12) & (num < 18)):
        return 12
    elif(num >= 18):
        return 18
        
df['Day'] = df.Date.apply(getDay)
df['Hours'] = df.Date.apply(getHours)

df = df[['Name', 'Email', 'Day', 'Hours']]

df = df.drop_duplicates().reset_index().drop('index',1)

df1 = pd.DataFrame(columns = ['Email', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 0, 6, 12, 18])
df1['Email'] = df['Email']
df1['Sunday'] = df1['Monday'] = df1['Tuesday'] = df1['Wednesday'] = df1['Thursday'] = df1['Friday'] = df1['Saturday'] = df1[0] = df1[6] = df1[12] = df1[18] = 0

for i in range(0, max(df.index)+1):
    df1.loc[i,(df.iloc[i,2])] = 1
    df1.loc[i,(df.iloc[i,3])] = 1
    
df1 = df1.groupby('Email', axis = 0, as_index=False).sum()

df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customer_days_time.csv", index = False)