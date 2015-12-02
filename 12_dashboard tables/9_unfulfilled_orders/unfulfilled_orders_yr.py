import pandas as pd
import re
from datetime import datetime
import os
import datetime as DT

df = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+"\data\orders_export.csv")
#df.columns
df = df[['Name', 'Fulfillment Status', 'Created at']]
df.columns = ['Name', 'Fulfillment Status', 'Created']

def getDate(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    return matchobj.group(1)

def getMonth(data):
    matchobj = re.match(r'(.*)-(.*).*',data)
    return matchobj.group(1)
    
df['Created'] = df.Created.apply(getDate)
    
df1 = df.drop_duplicates(cols='Name', take_last=False)
df1 = df1.reset_index().drop('index', 1)

today = DT.date.today()
dt = today - DT.timedelta(days=1) 
dt1 = datetime.strptime('2015-01-01', '%Y-%m-%d').date()
df1['Yes'] = df1.apply(lambda x: (datetime.strptime(x['Created'], '%Y-%m-%d').date() <= dt) & (datetime.strptime(x['Created'], '%Y-%m-%d').date() >= dt1), axis = 1)

df2 = df1.loc[df1['Yes'] == True]

df2 = df2[['Name', 'Fulfillment Status', 'Created']]
df2 = df2.reset_index().drop('index', 1)
df2['Created'] = df2.Created.apply(getMonth)    
df2['All'] = 1
df2['Unfulfilled'] = df2.apply(lambda x: 1 if x['Fulfillment Status'] == 'unfulfilled' else 0 , axis = 1)

df2 = df2.groupby(['Created'], axis=0, as_index=False).sum()
df2['% Unfulfilled'] = df2.apply(lambda x: x['Unfulfilled']*100/float(x['All']), axis = 1)

df2.to_csv("unfulfilled_yr.csv", index = False)