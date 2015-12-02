import pandas as pd
import os

df = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+'\data\\vend-total_revenue-for-product_variant-by-month.csv')


df = df[:max(df.index)-4]
df['Product'] = df['Product'].apply(lambda x: x.upper())
df = df.sort('Product')
df = df[~df['Product'].str.contains("CAIRO")]
df = df.reset_index().drop('index',1)
df = df.groupby(['Product', 'Brand', 'Type'], axis=0, as_index=False).sum()

n=range(4,len(df.columns)-4)
n=[0]+[1]+[2]+n
n.append(len(df.columns)-3)

df=df[n]

for i in range(0,max(df.index)+1):
    for j in range(3,len(df.columns)-1):
        #To get the first non zero revenue month
        if(df.iloc[i,j]!=0):
            t=1
            break
    #TO get the total no of months        
    n=len(df.columns)-1-j
    m=n**(-1)
    y=df.loc[i, 'Revenue']/df.iloc[i,j]
    df.loc[i,'CMGR']=(pow(y,m)-1)*100
    df.loc[i,'Period'] = n
    
gprofit = df[['Product', 'Brand', 'Type', 'Revenue' , 'Gross Profit', 'CMGR', 'Period']]

total = gprofit['Revenue'].sum(1)
totalgp = gprofit['Gross Profit'].sum(1)
gprofit['%Total Revenue'] = gprofit['Revenue'].apply(lambda x: x*100/total)
totprods = max(gprofit.index) + 1
temp = total/totprods
gprofit['Average Revenue'] = temp
gprofit['Average Gross Profit'] = totalgp/totprods
gprofit['% Variation from Average'] = gprofit['Revenue'].apply(lambda x: (x-temp)*100/temp)
total = gprofit['Gross Profit'].sum(1)
gprofit['%Total Gross Profit'] = gprofit['Gross Profit'].apply(lambda x: x*100/total)

#gprofit.columns = ['Product', 'Brand', 'Type', 'Revenue', '%Total Revenue', 'Gross Profit', '%Total Gross Profit', 'CMGR', '% Variation from Average']

gprofit.to_csv('products.csv', index=False)