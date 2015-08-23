import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-item_count.csv'
df = pd.read_csv(location)
#names to upper
for i in range(0, max(df.index)+1):
    df.loc[i, 'Product'] = df.loc[i, 'Product'].upper()

df=df.sort('Product')
df= df.reset_index().drop('index',1)
lis=[]
for i in range(0,max(df.index)+1):
    if('ITEM COUNT'==df.loc[i,'Product']):
        lis.append(i)

df=df.drop(df.index[lis])
        
#sort products and reset index
df= df.reset_index().drop('index',1)

#Subsetting with reqd fields
df1 = df[['Product','Aug 2012','Sep 2012','Oct 2012','Nov 2012','Dec 2012','Jan 2013','Feb 2013','Mar 2013','Apr 2013','May 2013','Jun 2013','Jul 2013','Aug 2013','Sep 2013','Oct 2013','Nov 2013','Dec 2013','Jan 2014','Feb 2014','Mar 2014','Apr 2014','May 2014','Jun 2014','Jul 2014','Aug 2014','Sep 2014','Oct 2014','Nov 2014','Dec 2014','Jan 2015','Feb 2015','Mar 2015','Apr 2015','May 2015','Jun 2015','Jul 2015','Revenue']]

#removing special characters
for i in range(0,max(df1.index)+1):
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(",","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("(","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(")","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("&","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("/","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("-","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("'","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("_","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(" ","")
    
#remove unnecessary products
lis=[]
for i in range(0,max(df1.index)+1):
    if (re.search('L.E',df1.loc[i,'Product'])):
        lis.append(i)
    if (re.search('CAIRO',df1.loc[i,'Product'])):
        lis.append(i)
df1=df1.drop(df1.index[lis])

#sort and reset index
df1=df1.sort('Product')
df1= df1.reset_index().drop('index',1)

df2=df1

#get the row indices which have same product
ls=[]
for i in range(0,max(df1.index)):
    if (df1.loc[i,'Product']==df1.loc[i+1,'Product']):
        for j in range(1,36):
            if ((df1.iloc[i,j]==0) & (df1.iloc[i+1,j]!=0)):
                #df1.iloc[i,j]=df1.iloc[i+1,j]
                ls.append(i+1)
                ls.append(i)
                
            elif ((df1.iloc[i+1,j]==0) & (df1.iloc[i,j]!=0)):
                #df1.iloc[i+1,j]=df1.iloc[i,j]
                ls.append(i)
                ls.append(i+1)
                
#remove redundancies in indices
p=[]
for i in ls:
    if i not in p:
        p.append(i)
        
#get redundant products
df3=df1.iloc[p]
df3= df3.reset_index().drop('index',1)

#remove redundant products
df1=df1.drop(df1.index[ls])
df1= df1.reset_index().drop('index',1)

#get all the unique names of redundant products
names=[]
for i in df3.index:
    if df3.loc[i,'Product'] not in names:
        names.append(df3.loc[i, 'Product'])
        
#create a dataframe with only redundant products
df4=pd.DataFrame(columns=df1.columns)
j=0
for i in names:
    df4.loc[j,'Product']=i
    j=j+1
for i in range(0,max(df4.index)+1):
    for j in range(1,37):
        df4.iloc[i,j]=0
        
for i in range(0,max(df4.index)+1):
    c=[]
    tot=0
    for j in range(0,max(df3.index)+1):
        if (df4.loc[i,'Product']==df3.loc[j,'Product']):
            tot=tot+df3.iloc[j,37]
            c.append(j)
        else:
            if(tot!=0):
                df4.iloc[i,37] = tot
            for k in c:
                for l in range(1,37):
                    if(df3.iloc[k,l]!=0):
                        df4.iloc[i,l]=df3.iloc[k,l]
            tot=0
            c=[]
            
df2=df1
df5=pd.concat([df2,df4],ignore_index=True)
df5=df5.sort('Product')
df5= df5.reset_index().drop('index',1)

df5.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\itemcount.csv',index=None)



#----------------Revenue--------------------------

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-total_revenue.csv'
df = pd.read_csv(location)

df1=df
#names to upper
for i in range(0, max(df.index)+1):
    df.loc[i, 'Product'] = df.loc[i, 'Product'].upper()

#sort products and reset index
df=df.sort('Product')
df= df.reset_index().drop('index',1)

#Subsetting with reqd fields
df1 = df[['Product','Aug 2012','Sep 2012','Oct 2012','Nov 2012','Dec 2012','Jan 2013','Feb 2013','Mar 2013','Apr 2013','May 2013','Jun 2013','Jul 2013','Aug 2013','Sep 2013','Oct 2013','Nov 2013','Dec 2013','Jan 2014','Feb 2014','Mar 2014','Apr 2014','May 2014','Jun 2014','Jul 2014','Aug 2014','Sep 2014','Oct 2014','Nov 2014','Dec 2014','Jan 2015','Feb 2015','Mar 2015','Apr 2015','May 2015','Jun 2015','Jul 2015','Revenue']]

#removing special characters
for i in range(0,max(df1.index)+1):
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(",","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("(","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(")","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("&","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("/","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("-","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("'","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace("_","")
    df1.loc[i, 'Product'] =df1.loc[i, 'Product'].replace(" ","")
    
#remove unnecessary products
import re
lis=[]
for i in range(0,max(df1.index)+1):
    if (re.search('L.E',df1.loc[i,'Product'])):
        lis.append(i)
    if (re.search('CAIRO',df1.loc[i,'Product'])):
        lis.append(i)
df1=df1.drop(df1.index[lis])

#sort and reset index
df1=df1.sort('Product')
df1= df1.reset_index().drop('index',1)

df2=df1

        
#get redundant products
df3=df1.iloc[p]
df3= df3.reset_index().drop('index',1)

#remove redundant products
df1=df1.drop(df1.index[ls])
df1= df1.reset_index().drop('index',1)

#get all the unique names of redundant products
names=[]
for i in df3.index:
    if df3.loc[i,'Product'] not in names:
        names.append(df3.loc[i, 'Product'])
        
#create a dataframe with only redundant products
df4=pd.DataFrame(columns=df1.columns)
j=0
for i in names:
    df4.loc[j,'Product']=i
    j=j+1
for i in range(0,max(df4.index)+1):
    for j in range(1,37):
        df4.iloc[i,j]=0
        
for i in range(0,max(df4.index)+1):
    c=[]
    tot=0
    for j in range(0,max(df3.index)+1):
        if (df4.loc[i,'Product']==df3.loc[j,'Product']):
            tot=tot+df3.iloc[j,37]
            #print tot
            c.append(j)
        else:
            if(tot!=0):
                df4.iloc[i,37] = tot
            for k in c:
                for l in range(1,37):
                    if(df3.iloc[k,l]!=0):
                        #print df4.loc[i,'Product'], l, df3.iloc[k,l]
                        df4.iloc[i,l]=df3.iloc[k,l]
            tot=0
            c=[]
            
df2=df1
df5=pd.concat([df2,df4],ignore_index=True)
df5=df5.sort('Product')
df5= df5.reset_index().drop('index',1)

df5.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\totalrevenue.csv',index=None)
