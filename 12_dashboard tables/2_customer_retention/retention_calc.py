import pandas as pd
from datetime import datetime, timedelta
import re
import os


df = pd.read_csv("../data/orders_export.csv")

df = df[['Email', 'Created at']] #subset required columns
df.columns = ['Email', 'Date'] #rename columns

def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    return matchobj.group(1)
def convertNewDate(data):
    matchobj = re.match(r'(.*) (.*).*',data)
    return matchobj.group(1)
def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return (d2 - d1).days
    
df['Date'] = df.Date.apply(convertDate) #call function
df = df.drop_duplicates().reset_index().drop('index',1) #remove products with same names in single order

df['YearBefore'] = (str)(datetime.now() - timedelta(days=366)) #366 days from today(Thursday)
df['YearBefore'] = df.YearBefore.apply(convertNewDate) #call function

df['DaysBetween'] = df.apply(lambda x: days_between(x['YearBefore'], x['Date']), axis=1)
df = df[(df.DaysBetween <= 365) & (df.DaysBetween >= 0)]

df1 = df[['Email']]
df1 = df1.drop_duplicates().reset_index().drop('index',1)

df2 = df[['Email', 'Date']]

df['Days30Before'] = (str)(datetime.now() - timedelta(days=31)) #31 days from today(Thursday)
df['Days30Before'] = df.Days30Before.apply(convertNewDate) 

df2['Days20Before'] = (str)(datetime.now() - timedelta(days=21)) #21 days from today(Thursday)
df2['Days20Before'] = df2.Days20Before.apply(convertNewDate) 

df['DaysBetween'] = df.apply(lambda x: days_between(x['Days30Before'], x['Date']), axis=1)
df = df[(df.DaysBetween <= 30) & (df.DaysBetween >= 0)]

df2['DaysBetween'] = df2.apply(lambda x: days_between(x['Days20Before'], x['Date']), axis=1)
df2 = df2[(df2.DaysBetween <= 20) & (df2.DaysBetween >= 0)]

df['Count'] = 1
df = df[['Email', 'Count']]
df = df.groupby(['Email'], axis = 0, as_index=False).sum()

df2['Count'] = 1
df2 = df2[['Email', 'Count']]
df2 = df2.groupby(['Email'], axis = 0, as_index=False).sum()

df = df[(df.Count > 1)]
df = df.drop_duplicates().reset_index().drop('index',1)

df3 = pd.DataFrame(columns = ['Cutomers 30 days', 'Cutomers 20 days', 'Total Count', 'Retention Rate', 'Regular Customers'])
df3.loc[0, 'Cutomers 30 days'] = max(df.index) + 1
df3.loc[0, 'Cutomers 20 days'] = max(df2.index) + 1
df3.loc[0, 'Total Count'] = max(df1.index) + 1
df3.loc[0, 'Retention Rate'] = df3.loc[0, 'Cutomers 30 days']/float(df3.loc[0, 'Total Count'])
df3.loc[0, 'Regular Customers'] = df3.loc[0, 'Cutomers 20 days']/float(df3.loc[0, 'Total Count'])

df3.to_csv("with_retention.csv", index = False)