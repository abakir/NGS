import pandas as pd

df = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\orders_export.csv')

# take required fields
df1=df[['Email', 'Created at' ]]

#let there be only one row for each order
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

#getting only date from created at field
df1['Created at'] = df1.apply(lambda x: x['Created at'][:10], axis = 1)
    
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

df1.columns=['Email', 'Date']
df1['Difference'] = 0
df1['Count'] = 0

df1['Date'] =pd.to_datetime(df1.Date)
df1=df1.sort(['Email', 'Date'])
df1= df1.reset_index().drop('index',1)

n = 1
for i in range(0,max(df1.index)):
    if(df1.iloc[i,0]==df1.iloc[i+1,0]):
        n = n + 1
        df1.iloc[i+1,2]=(df1.iloc[i+1,1]-df1.iloc[i,1]).days
        if (i == max(df1.index) - 1):
            df1.iloc[i + 1,3] = n
    else:
        df1.iloc[i,3] = n
        n = 1

df1 = df1.groupby('Email', axis=0, as_index=False).sum()
df1['Average'] = df1.apply(lambda x: x['Difference']/float(x['Count']), axis = 1)

df2 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\customers_export.csv")
df2 = df1.merge(df2, on = ['Email'], how = 'inner')

df2 = df2[['Email', 'Average', 'First Name', 'Last Name']]

for i in range(0, max(df2.index)+1):
    df2.loc[i, 'Name'] = df2.loc[i, 'First Name'] + " " + df2.loc[i, 'Last Name']
    
df2 = df2[['Email' , 'Average', 'Name']]
            
df2.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\\frequency.csv",index=False)