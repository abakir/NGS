import pandas as pd
import re
from datetime import datetime
import datetime as DT
import os

df = pd.read_csv("../data/orders_export.csv")
#df.columns
df = df[['Name', 'Fulfillment Status', 'Created at']]

#df2 = pd.DataFrame(columns = df.columns, index = range(0, max(df.index)+1))
for i in range(0, max(df.index)+1):
    matchobj = re.match(r'(.*) (.*) (.*).*',df.iloc[i, 2])
    df.iloc[i, 2] = matchobj.group(1)
    
df1 = df.drop_duplicates(cols='Name', take_last=False)
df1 = df1.reset_index().drop('index', 1)

today = DT.date.today()
dt = today - DT.timedelta(days=8) #Wednesday date
df1['Yes'] = df1.apply(lambda x: datetime.strptime(x['Created at'], '%Y-%m-%d').date() > dt, axis = 1)

df2 = df1.loc[df1['Yes'] == True]

df2 = df2[['Name', 'Fulfillment Status', 'Created at']]

df2['All'] = 1
df2['Unfulfilled'] = df2.apply(lambda x: 1 if x['Fulfillment Status'] == 'unfulfilled' else 0 , axis = 1)

df2 = df2.groupby(['Created at'], axis=0, as_index=False).sum()
df2['% Unfulfilled'] = df2.apply(lambda x: x['Unfulfilled']*100/float(x['All']), axis = 1)

df2.to_csv("unfulfilled.csv", index = False)