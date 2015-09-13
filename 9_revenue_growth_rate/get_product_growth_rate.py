import pandas as pd
location = 'C:\Users\saisree849\Downloads\\vend-total_revenue-for-product_variant-by-month (1).csv'
df = pd.read_csv(location)

df=df[0:max(df.index)-4]

n=range(7,len(df.columns)-4)
n=[0]+n

df=df[n]

col=[]
p=0
for i in df.columns:
    p=p+1
    if(p!=2):
        if(p!=len(df.columns)):
            col.append(i)
            
df1=pd.DataFrame(columns=col)

for i in range(0,max(df.index)+1):
    df1.loc[i,'Product']=df.loc[i,'Product']
    for j in range(2,len(df.columns)-2):
        if(df.iloc[i,j-1]!=0):
            df1.iloc[i,j-1]=(df.iloc[i,j]-df.iloc[i,j-1])*100/df.iloc[i,j-1]
        else:
            df1.iloc[i,j-1]=0
            
df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\product_growth_rate.csv",index=False)