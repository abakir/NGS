import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\products_export-3.csv'
df = pd.read_csv(location)
df=df[['Handle','Title','Type']]
df.columns=['Sku','Product','Type']
df = df[pd.notnull(df['Product'])]
df= df.reset_index().drop('index',1)
for i in range(0, max(df.index)+1):
    df.loc[i, 'Product'] = df.loc[i, 'Product'].upper()

df=df.sort('Product')
df1= df.reset_index().drop('index',1)
for i in range(0,max(df1.index)+1):
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(",","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("(","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(")","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("&","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("/","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("-","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("'","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("_","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(" ","")
    
df2=df1

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\orders_export-10.csv'
df = pd.read_csv(location)

df=df[['Email','Lineitem quantity', 'Lineitem name','Lineitem price']]
df.columns=['Email', 'Quantity','Product','Price']
df = df[pd.notnull(df['Product'])]
df= df.reset_index().drop('index',1)
for i in range(0, max(df.index)+1):
    df.loc[i, 'Product'] = df.loc[i, 'Product'].upper()

df=df.sort('Product')
df1= df.reset_index().drop('index',1)

for i in range(0,max(df1.index)+1):
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(",","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("(","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(")","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("&","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("/","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("-","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("'","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("_","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(" ","")
    
df3=df1
for i in range(0, max(df2.index)+1):
    for j in range(0, max(df3.index)+1):
        if (df2.loc[i,'Product']==df3.loc[j,'Product']):
            df3.loc[j,'Type']=df2.loc[i,'Type']

df4=df3          
df3 = df3[pd.notnull(df3['Type'])]
df3= df3.reset_index().drop('index',1)


df3.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\producttype.csv",index=False)
#df4.to_csv("C:\Users\saisree849\Desktop\\allproducttype.csv",index=False)