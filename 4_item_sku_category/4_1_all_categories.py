from os import listdir
from os.path import isfile, join
import pandas as pd
from pandas import read_csv

ls=[]
for f in listdir('C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\\all_items'):
    if isfile(join('C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\\all_items',f)):
        ls.append(f)
        
df = pd.DataFrame(columns=['sku', 'name', 'type'])
df = df.fillna(0)

for i in ls:
    location = "C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\\all_items\\"+i
    df1 = read_csv(location)
    df1 = df1[['sku', 'name', 'type']]
    df = df.append(df1,ignore_index = True)
    
df = df.drop_duplicates()

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\4_item_sku_category\category_sku.csv", sep=",", index=False)