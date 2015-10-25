import pandas as pd

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\bought_together\orders_export.csv")

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

na = []
e = df['Name'].tolist()
for k in e:
    for j in e:
        p = k + j
        na.append(p)
        
df1['Name'] = pd.Series(na)

df1 = df1[df1.Product1 != df1.Product2]
df1 = df1.reset_index().drop('index',1)

def getUnique(data):
    return len(data) - len(set(data))
    
df1['Count'] = df1.Name.apply(getUnique)

df1 = df1[df1.Count != 0]
df1 = df1.reset_index().drop('index',1)

df1 = df1[['Product1', 'Product2', 'Count']]

df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\\bought_together\pair_complete.csv", index = False)