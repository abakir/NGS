import pandas as pd
import os


df = pd.read_csv("../data/orders_export.csv")

df = df[['Name', 'Lineitem name']]
df.columns = ['Name', 'Product']

df['Product'] = df.Product.apply(lambda x: x.upper())
df = df.drop_duplicates().reset_index().drop('index',1)
df = df.groupby([ 'Product'], axis = 0, as_index=False)['Name'].sum()

df['Name'] = df.Name.apply(lambda x: x.split("#"))
df['Name'] = df.Name.apply(lambda x: x[1:])

df1 = pd.DataFrame(columns = ['Product1', 'Product2','Name', 'Count'])

b = []
a = df['Product'].tolist() #create a list of type
for i in range(0, max(df.index)+1): #count of months
    b = b + a
df1['Product1'] = pd.Series(b)

b = []
x = df['Product'].tolist() #create a list of months
for a in x: #take each month
    for i in range(0, max(df.index)+1): #count of types
        b.append(a)
df1['Product2'] = pd.Series(b)

na = []
e = df['Name'].tolist()
for k in e:
    for j in e:
        p = k + j
        na.append(p)
        
df1['Name'] = pd.Series(na)

df1 = df1[df1.Product1 != df1.Product2]

def getUnique(data):
    return len(data) - len(set(data))
    
df1['Count'] = df1.Name.apply(getUnique)

df1 = df1[df1.Count != 0]

def combineProds(name1, name2, count):
    if(name1 < name2):
        return name1 + "," + name2 + "," +count
    else:
        return name2 + "," + name1 + "," +count
        
df1['newcol'] = df1.apply(lambda x: combineProds(x['Product1'], x['Product2'],str(x['Count'])), axis=1)
df1 = df1.drop_duplicates('newcol').reset_index().drop('index',1)

df1 = df1[['Product1', 'Product2', 'Count']]

df1 = df1.sort(['Count'], ascending = False)
df1 = df1.reset_index().drop('index', 1)

df1.to_csv("pair_complete.csv")