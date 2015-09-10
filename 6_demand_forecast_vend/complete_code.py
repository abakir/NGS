import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\vend-item_count.csv'
df = pd.read_csv(location)
#names to upper
for i in range(0, max(df.index)+1):
    df.loc[i, 'Product'] = df.loc[i, 'Product'].upper()

df=df.sort('Product')
df= df.reset_index().drop('index',1)

#remove products with name 'item count'
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
    if (re.search('ABOVE',df1.loc[i,'Product'])):
        lis.append(i)
    if (re.search('ELKATAMEYAFIFTHSETTLEMENT',df1.loc[i,'Product'])):
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
        for j in range(1,37):
            if ((df1.iloc[i,j]==0) & (df1.iloc[i+1,j]!=0)):
                #df1.iloc[i,j]=df1.iloc[i+1,j]
                ls.append(i+1)
                ls.append(i)
                
            elif ((df1.iloc[i+1,j]==0) & (df1.iloc[i,j]!=0)):
                #df1.iloc[i+1,j]=df1.iloc[i,j]
                ls.append(i)
                ls.append(i+1)
                
#remove redundancies in indices listed
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

df6=df5

#df5.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\itemcount.csv',index=None)



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
    if (re.search('ABOVE',df1.loc[i,'Product'])):
        lis.append(i)
    if (re.search('ELKATAMEYAFIFTHSETTLEMENT',df1.loc[i,'Product'])):
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

#df5.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\totalrevenue.csv',index=None)


#location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\itemcount.csv'
#df = pd.read_csv(location)

#location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\totalrevenue.csv'
#df1 = pd.read_csv(location)

df=df6
df2=df5

#divide each revenue by item count
for i in range(0,max(df.index)+1):
    for j in range(1,37):
        if(df.iloc[i,j] > 0):
            df2.iloc[i,j] = df1.iloc[i,j]/df.iloc[i,j]
            
#get price from recent months
for i in range(0,max(df2.index)+1):
    flag=0
    for j in range(1,37):
        if(df2.iloc[i,j] == 0):
            flag+=1
        elif ((flag>0) & (df2.iloc[i,j]>0)):
            for k in range(j-flag, j+1):
                df2.iloc[i,k]=df2.iloc[i,j]
            flag=0
        if ((flag>0) & (j==36)):
            y=j-flag
            for k in range(j-flag+1, j+1):
                df2.iloc[i,k]=df2.iloc[i,y]

#df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\price.csv', index=False)

#location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\price.csv'
#df = pd.read_csv(location)
df=df2
#remove products whose revenue is 0
df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
#get products which make 80% sales
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break
dfimpp=df4
#df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv', index=False)

#-----------------------------------------------------------------------------------------------------------

#location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\totalrevenue.csv'
#df = pd.read_csv(location)

df=df5
df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break

dfimptr = df4
#df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_totalrevenue.csv', index=False)

#-----------------------------------------------------------------------------------------------------------------

#location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\itemcount.csv'
#df = pd.read_csv(location)
df=df6
df = df[df.Revenue != 0]
df = df[pd.notnull(df['Revenue'])]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df
df3=df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total=0
for i in range(0, max(df3.index)+1):
    total+=df3.loc[i,'Revenue']
    
temp=0
for i in range(0, max(df3.index)+1):
    temp+=df3.loc[i,'Revenue']
    if (temp>=total*0.8):
        df4=df3[0:i]
        break

dfimpic = df4
#df4.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_itemcount.csv', index=False)


#location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_price.csv'
#df = pd.read_csv(location)
location='C:\Users\saisree849\AppData\Roaming\Skype\My Skype Received Files\\vend-total_revenue-sales_summary-by-month-2.csv'
df1 = pd.read_csv(location)
df=dfimpp
#creating column names 
col=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ind = [0,1,2,3]

df2=pd.DataFrame(index=ind,columns=col)

t12=0
t13=0
t14=0
p12=0
p13=0
p14=0
#adding all positive revenues
for i in range(1,13):
    if(df1.iloc[0,i]>0):
        p12=p12+1
        t12=t12+df1.iloc[0,i]
for i in range(13,25):
    if(df1.iloc[0,i]>0):
        p13=p13+1
        t13=t13+df1.iloc[0,i]
for i in range(25,37):
    if(df1.iloc[0,i]>0):
        p14=p14+1
        t14=t14+df1.iloc[0,i]
    
#getting monthly average
t12=t12/p12
t13=t13/p13
t14=t14/p14

#creating seasonal index for each year
for i in range(1,13):
    df2.iloc[0,i-1]=df1.iloc[0,i]/t12
for i in range(13,25):
    df2.iloc[1,i-13]=df1.iloc[0,i]/t13
for i in range(25,37):
    df2.iloc[2, i-25]=df1.iloc[0,i]/t14
    
#getting average SI for each month
for i in range(0,12):
    t=0
    p=0
    for j in range(0,max(df2.index)):
        if(df2.iloc[j,i]>0):
            p=p+1
        t=t+df2.iloc[j,i]
    df2.iloc[max(df2.index), i] = t/p
    
df=df.drop('Revenue',axis=1)
df.loc[max(df.index)+1,'Product']='SeasonalIndex'

k=4
for j in range(1,37):
    df.iloc[max(df.index), j] = df2.loc[3,k]
    k=k+1
    if(k==13):
        k=1
        
df.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\6_demand_forecast_vend\\imp_seasonalindex.csv', index=False)