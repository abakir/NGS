import pandas as pd
location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\\vend-total_revenue-for-type-by-month.csv'
df = pd.read_csv(location)

df=df[0:max(df.index)-4]

n=range(0,len(df.columns)-4)

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
    df1.loc[i,'Type']=df.loc[i,'Type']
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
    tot=0
    for j in range(1,len(df.columns)-1):
        if(df.iloc[i,j]!=0):
            t=1
            break
    n=len(df.columns)-2-j
    df1.loc[i,'Average']=(df.iloc[i,len(df.columns)-1]-df.iloc[i,j])*100/(n*df.iloc[i,j])
            
df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\\type_growth_rate.csv",index=False)