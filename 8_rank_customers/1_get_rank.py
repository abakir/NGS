import pandas as pd
import re
import math

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\8_rank_customers\\vend-sale_count-for-customer-by-month.csv'
df = pd.read_csv(location)
df=df.drop('Sale Count',1)
df=df.drop('Margin',1)
df=df.drop('Cost of Goods',1)
df=df.drop('Tax',1)

lis=[]
for i in range(0,max(df.index)+1):
    if('Revenue'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Cost of Goods'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Gross Profit'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Basket Value'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Sale Count'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Tax'==df.loc[i,'Customer']):
        lis.append(i)
    elif('Margin'==df.loc[i,'Customer']):
        lis.append(i)
    elif(math.isnan(df.iloc[i,1])):
        lis.append(i)
df=df.drop(df.index[lis])
        
#sort products and reset index
df= df.reset_index().drop('index',1)

n=0
col=[]
months=[]
for i in df.columns:
    n=n+1
    if((n==1)|(len(df.columns)-2<=n)|(n>=len(df.columns))):
        col.append(i)
    else:
        col.append(i+'-rank')
        col.append(i+'-order')
        months.append(i)
        
df1=pd.DataFrame(columns=col)

for i in range(0,max(df.index)+1):
    n=0
    for j in df.columns:
        n=n+1
        if((n==1)|(len(df.columns)-2<=n)|(n>=len(df.columns))):
            df1.loc[i,j]=df.loc[i,j]
        else:
            df1.loc[i,(j+'-order')]=df.loc[i,j]
        
df2=df1

t=0
for j in months:
    df2=df2.sort(j+'-order',0,ascending=False)
    df2= df2.reset_index().drop('index',1)
    t=t+2
    n=[]
    for i in range(0, max(df2.index)+1):
        if df2.iloc[i,t] not in n:
            n.append(df2.iloc[i,t])
    k=len(n)
    df2.iloc[0,t-1]=k
    for i in range(1, max(df2.index)+1):
        if(df2.iloc[i,t]==df2.iloc[i-1,t]):
            df2.iloc[i,t-1]=k
        else:
            k=k-1
            df2.iloc[i,t-1]=k

df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\8_rank_customers\\rank.csv', index=False)