import pandas as pd

location ="C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\count_category.csv"
df = pd.read_csv(location)

i=0
while (i < max(df.index)):
    total = df.loc[i, 'Count']
    j = 1
    while ((i+j < max(df.index)) & (df.loc[i, 'Email'] == df.loc[i+j, 'Email'])):
        total = total + df.loc[i+j, 'Count']
        j = j + 1
    if (i+j == max(df.index)):
        total = total + df.loc[i+j, 'Count']
    p = j
    df.loc[i, 'Proportion'] = float(df.loc[i, 'Count']) / total
    while (j!=0):
        df.loc[i+j, 'Proportion'] = float(df.loc[i+j, 'Count']) / total
        j = j - 1
    i = i + p
    
    
df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\proportion_category.csv", sep=",",index=False)