from pandas import read_csv, DataFrame
import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\1_common_pair_products\orders_export-2.csv'
df = pd.read_csv(location)

df = df[0:11025]
df = df[['Email','Lineitem name']]

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\category_sku.csv'
df1 = pd.read_csv(location)

df = df.sort('Lineitem name', ascending=True)
df1 = df1.sort('name', ascending=True)
for i in range(0, max(df.index)+1):
    for j in range(0, max(df1.index)+1):
        if (df.loc[i, 'Lineitem name'] == df1.loc[j, 'name']):
            #df.loc[i, 'Lineitem sku'] = df1.loc[j, 'sku']
            df.loc[i, 'Category'] = df1.loc[j, 'type']
            #print i, df.loc[i, 'Lineitem name']
            
            
df = df.sort("Email", ascending=True)

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\categories_emails.csv", sep=",", index=False)