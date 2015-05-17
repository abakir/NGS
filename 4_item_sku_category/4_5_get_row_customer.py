import pandas as pd

location ="C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\count_category.csv"
df = pd.read_csv(location)
df = df.dropna()
df = df.reset_index()
df = df.drop('index', 1)

ls=[]
for i in range(0, max(df.index)+1):
    ls.append(df.loc[i, 'Category'])
s=['Email']

for i in ls:
    if i not in s:
        s.append(i)
        
s.append('Total')

df1 = pd.DataFrame(columns=s)
df1 = df1.fillna(0)
for i in range(0,max(df.index)+1):
    df1.loc[i,'Email'] = df.loc[i, 'Email']
df1 = df1.drop_duplicates()
df1 = df1.reset_index()
df1 = df1.drop('index', 1)


for i in range(0,max(df1.index)+1):
    for j in df1.columns:
        if (pd.isnull(df1.loc[i,j])):
            df1.loc[i,j] = 0


for i in range(0, max(df1.index)+1):
    for j in range(0, max(df.index)+1):
        if (df1.loc[i, 'Email'] == df.loc[j, 'Email']):
            df1.loc[i, df.loc[j,'Category']] = df.loc[j, 'Count']


for i in range(0, max(df1.index)+1):
    df1.loc[i, 'Total'] = 0
    

q=[]
for i in ls:
    if i not in q:
        q.append(i)
        
        
for i in range(0, max(df1.index)+1):
    total = 0
    for j in q:
        total = total + df1.loc[i, j]
    df1.loc[i, 'Total']=total
    

df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\customer_row.csv",sep=",",index=False)