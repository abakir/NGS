import pandas as pd
import re
from datetime import datetime
import datetime as DT
import yaml

with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

df = pd.read_csv(cfg['root']+cfg['data']+cfg["orders"],low_memory=False)

df = df[['Name', 'Fulfillment Status', 'Created at']]

#get date
def getDate(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    return matchobj.group(1)
df['Created at'] = df.apply(lambda x: getDate(x['Created at']), axis=1)
    
#take last item of the total order
df1 = df.drop_duplicates(cols='Name', take_last=False)
df1 = df1.reset_index().drop('index', 1)

#get todays date
today = DT.date.today()
dt = today - DT.timedelta(days=8) #Wednesday date
df1['Yes'] = df1.apply(lambda x: datetime.strptime(x['Created at'], '%Y-%m-%d').date() > dt, axis = 1) #update rows by comparing dates

df2 = df1.loc[df1['Yes'] == True] #get orders within last week

df2 = df2[['Name', 'Fulfillment Status', 'Created at']]

df2['All'] = 1
df2['Unfulfilled'] = df2.apply(lambda x: 1 if x['Fulfillment Status'] == 'unfulfilled' else 0 , axis = 1) #update column based on fulfillement status

df2 = df2.groupby(['Created at'], axis=0, as_index=False).sum() #count total unfulfilled orders
df2['% Unfulfilled'] = df2.apply(lambda x: x['Unfulfilled']*100/float(x['All']), axis = 1)

df2.to_csv(cfg['root']+cfg['output']+cfg['unfulfilled'], index = False)