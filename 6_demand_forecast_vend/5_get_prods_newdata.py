import pandas as pd

location='C:\Users\saisree849\AppData\Roaming\Skype\My Skype Received Files\NGS_Comp_Price.csv'
df = pd.read_csv(location)

df=df[pd.notnull(df[' S.Price '])]
df= df.reset_index().drop('index',1)

df=df.drop('sku',1)
df=df.drop('brand',1)
df=df.drop('Offah.com product comments',1)
df=df.drop('Gourmetegypt Product comments',1)
df=df.drop('Healthharveststore.com product comments',1)
df=df.drop('Imtenan.com Product Comments',1)
df=df.drop('Knockmart.com Product Comments',1)
df=df.drop('Beqala.com Product Comments',1)
df=df.drop('Categories',1)
df=df.drop('Average Competitor Prices(ACP)',1)
df=df.drop('Price Variance',1)
df=df.drop('Availability in NGS',1)
df=df.drop('Availability @ Others',1)

for i in range(0,max(df.index)+1):
    df.iloc[i,0] = df.iloc[i,0].upper()
    df.iloc[i,0] = df.iloc[i,0].replace(",","")
    df.iloc[i,0] = df.iloc[i,0].replace("(","")
    df.iloc[i,0] = df.iloc[i,0].replace(")","")
    df.iloc[i,0] = df.iloc[i,0].replace("&","")
    df.iloc[i,0] = df.iloc[i,0].replace("/","")
    df.iloc[i,0] = df.iloc[i,0].replace("-","")
    df.iloc[i,0] = df.iloc[i,0].replace("'","")
    df.iloc[i,0] = df.iloc[i,0].replace("_","")
    df.iloc[i,0] = df.iloc[i,0].replace(" ","")
    
location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv'
df1 = pd.read_csv(location)

ls=[]
ls1=[]
for j in range(0, max(df1.index)+1):
    k=0
    q=0
    p=0
    for i in range(0, max(df.index)+1):
        if(df.iloc[i,0]==df1.iloc[j,0]):
            p=i
            q=j
            #print i, df.iloc[i,0]
            k=k+1
    if(k==1):
        ls.append(p)
        ls1.append(q)
        
df2=pd.DataFrame(index=ls,columns=df.columns)
for i in ls:
    for j in df.columns:
        df2.loc[i,j] = df.loc[i,j]

df2=df2.reset_index().drop('index',1)

ls1.sort()
df1=df1.drop(df1.index[ls1])
df1= df1.reset_index().drop('index',1)

df.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\Comparedata.csv',index=False)

ls.sort()
df=df.drop(df.index[ls])
df= df.reset_index().drop('index',1)

for i in range(0,max(df.index)+1):
    df.iloc[i,1] = str(df.iloc[i,1])
    df.iloc[i,1] = df.iloc[i,1].upper()
    
import re
for i in range(0, max(df.index)+1):
    for j in range(0, max(df1.index)+1):
        if(re.match(df.iloc[i,0]+df.iloc[i,1],df1.iloc[j,0])):
            df.iloc[i,0] = df.iloc[i,0] + df.iloc[i,1]
            
ls=[]
ls1=[]
for j in range(0, max(df1.index)+1):
    k=0
    q=0
    p=0
    for i in range(0, max(df.index)+1):
        if(df.iloc[i,0]==df1.iloc[j,0]):
            p=i
            q=j
            #print i, df.iloc[i,0]
            k=k+1
    if(k==1):
        ls.append(p)
        ls1.append(q)
        
ls1.sort()
df1=df1.drop(df1.index[ls1])
df1= df1.reset_index().drop('index',1)

ls.sort()
df=df.drop(df.index[ls])
df= df.reset_index().drop('index',1)

df.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\Comparedatawithoutmatches.csv',index=False)

df1.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\impdatawithoutmatches.csv',index=False)