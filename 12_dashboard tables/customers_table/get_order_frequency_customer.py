import pandas as pd

df = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\data\orders_export.csv')

# take required fields
df1=df[['Name','Email', 'Created at' ]]

#let there be only one row for each order
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

#getting only date from created at field
df1['Created at'] = df1.apply(lambda x: x['Created at'][:10], axis = 1)
    
df1=df1.drop_duplicates()
df1= df1.reset_index().drop('index',1)

df1.columns=['Name','Email', 'Date']
df1['Difference'] = 0
df1['Total orders'] = 0

df1['Date'] =pd.to_datetime(df1.Date)
df1=df1.sort(['Email', 'Date'])
df1= df1.reset_index().drop('index',1)

n = 1
for i in range(0,max(df1.index)):
    if(df1.iloc[i,1]==df1.iloc[i+1,1]):
        n = n + 1
        df1.iloc[i+1,3]=(df1.iloc[i+1,2]-df1.iloc[i,2]).days
        if (i == max(df1.index) - 1):
            df1.iloc[i + 1,4] = n
    else:
        df1.iloc[i,4] = n
        n = 1

df1 = df1.groupby('Email', axis=0, as_index=False).sum()
df1['Average days between orders'] = df1.apply(lambda x: x['Difference']/float(x['Total orders']), axis = 1)
df2 = df1[['Email', 'Total orders', 'Average days between orders']]

            
df2.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\\frequency.csv",index=False)