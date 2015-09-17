import pandas as pd
location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\\vend-total_revenue-for-product_variant-by-month (1).csv'
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
col.append('Average')
                        
df1=pd.DataFrame(columns=col)

for i in range(0,max(df.index)+1):
    df1.loc[i,'Product']=df.loc[i,'Product']
    for j in range(2,len(df.columns)-1):
        if(df.iloc[i,j-1]!=0):
            df1.iloc[i,j-1]=(df.iloc[i,j]-df.iloc[i,j-1])*100/df.iloc[i,j-1]
        else:
            k=j-1
            flag=0
            while(k!=1):
                if(df.iloc[i,k]==0):
                    k=k-1
                else:
                    df1.iloc[i,j-1]=(df.iloc[i,j]-df.iloc[i,k])*100/df.iloc[i,k]
                    flag=1
                    break
            if(flag==0):
                df1.iloc[i,j-1]=0

for i in range(0,max(df.index)+1):
    for j in range(1,len(df.columns)-1):
        #To get the first non zero revenue month
        if(df.iloc[i,j]!=0):
            t=1
            break
    #TO get the total no of months        
    n=len(df.columns)-1-j
    #df.iloc[i,len(df.columns)-1] is the total revnue from original table
    df1.loc[i,'Average']=(df.iloc[i,len(df.columns)-1]-df.iloc[i,j])*100/(n*df.iloc[i,j])
    
                            
df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\product_growth_rate.csv",index=False)