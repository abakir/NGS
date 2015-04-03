from pandas import read_csv, DataFrame
import pandas as pd
import numpy as np

location = "C:\Users\saisree849\Documents\GitHub\NGS_Project\\1_common_pair_products\output1.csv"

df = read_csv(location, header=None)

#df.columns = ['Sku', 'Sample']
df = df.dropna()

df = df.reset_index()


df1 = pd.DataFrame(columns=['Sku1', 'Sku2', 'Count'])
df1 = df1.fillna(0)
j = 0
for i in range(0, max(df.index)+1):
    if (i % 2 == 0):
        df1.loc[j, 'Sku1'] = df.loc[i, 0]
        df1.loc[j, 'Sku2'] = df.loc[i, 1]
    else:
        df1.loc[j, 'Count'] = df.loc[i, 1]
        j = j + 1
        

df1[['Count']] = df1[['Count']].astype(int)
df2 = df1.sort('Count', ascending=False)
df2 = df2.reset_index()
df2 = df2.drop('index', axis=1)


df2.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\1_common_pair_products\pairs.csv", sep =",")