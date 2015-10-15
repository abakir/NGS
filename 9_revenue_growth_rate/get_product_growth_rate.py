import pandas as pd
location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\\vend-total_revenue-for-product_variant-by-month.csv'
df = pd.read_csv(location)

df=df[0:max(df.index)-4]

n=range(7,len(df.columns)-4)
n=[0]+n

df=df[n]

df = df.groupby('Product', axis=0, as_index=False).sum()
                        
df1=pd.DataFrame(columns=['Product', 'CAGR', 'Period'])

def copyData(data):
    return data
    

df1['Product'] = df.Product.apply(copyData)

for i in range(0,max(df.index)+1):
    for j in range(1,len(df.columns)-1):
        #To get the first non zero revenue month
        if(df.iloc[i,j]!=0):
            t=1
            break
    #TO get the total no of months        
    n=len(df.columns)-1-j
    m=n**(-1)
    #df.iloc[i,len(df.columns)-1] is the total revnue from original table
    y=df.iloc[i,len(df.columns)-1]/df.iloc[i,j]
    df1.loc[i,'CMGR']=(pow(y,m)-1)*100
    df1.loc[i,'Period'] = n
    
                            
df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\9_revenue_growth_rate\product_growth_rate.csv",index=False)