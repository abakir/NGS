import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS\\6_demand_forecast_vend\\vend-item_count.csv'
#read dataframe
df = pd.read_csv(location)
#remove unnecessary rows
df = df[:max(df.index)-5]
#change product names to upper case
df['Product'] = df['Product'].apply(lambda x: x.upper())
#sort dataframe by product
df = df.sort('Product')
#reorder the indices
df= df.reset_index().drop('index',1)
#remove unnecessary rows
df = df[~df['Product'].str.contains("CAIRO")]
#reorder the indices
df= df.reset_index().drop('index',1)
#remove unnecessary symbols in products
df['Product'] = df['Product'].apply(lambda s: re.sub(r"[(|)|,|/|-|_|&|\s|']", '', s))
#insert useful column numbers into list
#all months columns
ls = range(7,len(df.columns)-6)
#revenue column
ls.append(len(df.columns)-5)
#product column
ls.insert(0, 0)
#get useful columns
df = df[ls]
#remove redundant products
df = df.groupby(['Product'], axis=0, as_index=False).sum()


location = 'C:\Users\saisree849\Documents\GitHub\NGS\\6_demand_forecast_vend\\vend-total_revenue.csv'
df1 = pd.read_csv(location)
df1 = df1[:max(df1.index)-4]
df1['Product'] = df1['Product'].apply(lambda x: x.upper())
df1 = df1.sort('Product')
df1= df1.reset_index().drop('index',1)
df1 = df1[~df1['Product'].str.contains("CAIRO")]
#reorder the indices
df1= df1.reset_index().drop('index',1)
df1['Product'] = df1['Product'].apply(lambda s: re.sub(r"[(|)|,|/|-|_|&|\s|']", '', s))
ls = range(7,len(df1.columns)-4)
ls.insert(0, 0)
df1 = df1[ls]
df1 = df1.groupby(['Product'], axis=0, as_index=False).sum()


#in item count replace 0's by 1 for division purpose
df3 = df.replace(0, 1)
#make product column as index
df3 = df3.set_index('Product')
#change name of columns to numbers
df3.columns = range(0,len(df3.columns))
#change revenue values in item count to 1
df3[[len(df3.columns)-1]]=1
#make product column as index
df4 = df1.set_index('Product')
#change name of columns to numbers
df4.columns = range(0,len(df4.columns))
#divide reach cell in revenue with corresponding cell in item count
df2 = df4.div(df3,axis='columns')
#remove product column as index
df2.reset_index(level=0, inplace=True)



def calc_price(monthly_price):
    temp = 0
    for i, v in enumerate(monthly_price):
        if v > 0:
            monthly_price[i] = v
            temp = v
        elif v == 0:
            monthly_price[i] = temp
            
            
    temp = 0
    for i, v in reversed(list(enumerate(monthly_price))):
        if v > 0:
            monthly_price[i] = v
            temp = v
        elif v == 0:
            monthly_price[i] = temp
    return monthly_price
        
        

df2 = df2.set_index('Product')
df12 = df2.loc[:, 0:len(df2.columns)-2].apply(calc_price, axis=1)
#copy revenue column
df12[['Revenue']]=df2[[len(df2.columns)-1]]
df12.reset_index(level=0, inplace=True)

        
        
#price
df2 = df12[df12.Revenue != 0]
df2 = df2[pd.notnull(df2['Revenue'])]
df2 = df2.sort('Product')
df2 = df2.reset_index().drop('index',1)

df3 = df2.sort('Revenue',ascending = False)
df3= df3.reset_index().drop('index',1)

total = df3['Revenue'].sum(1)
#get products which make 80% sales
temp = 0
for i in range(0, max(df3.index)+1):
    temp += df3.loc[i,'Revenue']
    if (temp >= total*0.8):
        df2 = df3[0:i]
        break
 


location='C:\Users\saisree849\Documents\GitHub\NGS\\6_demand_forecast_vend\\vend-total_revenue-sales_summary-by-month.csv'
df1 = pd.read_csv(location)
df1 = df1[1:2]

#creating column names 
col=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
ind = [0,1,2,3]
df1.columns = range(0, len(df1.columns))
df1 = df1[range(1, len(df1.columns))]
df1.columns = range(0, len(df1.columns))


#calculate monthly SI
def get_revenues(revenues):
    t12=0
    t13=0
    t14=0
    p12=0
    p13=0
    p14=0
    for i, v in enumerate(revenues):
        if ((0 <= i) & (i <= 11)):
            if (v != 0):
                p12 += 1
                t12 += v
        elif ((12 <= i) & (i <= 23)):
            if (v != 0):
                p13 += 1
                t13 += v
        elif ((24 <= i) & (i <= 35)):
            if (v != 0):
                p14 += 1
                t14 += v
    t12 = t12/p12 
    t13 = t13/p13
    t14 = t14/p14
    for i, v in enumerate(revenues):
        if ((0 <= i) & (i <= 11)):
            revenues[i] = revenues[i]/t12
        elif ((12 <= i) & (i <= 23)):
            revenues[i] = revenues[i]/t13
        elif ((24 <= i) & (i <= 35)):
            revenues[i] = revenues[i]/t14
    return revenues
    
df2 = pd.DataFrame(index=ind,columns = col)
ls = df1.apply(get_revenues, axis = 1)
d12 = ls[range(0,12)]
d13 = ls[range(12,24)]
d14 = ls[range(24,36)]
d13.columns = range(0,12)
d14.columns = range(0,12)
df2= d12.append(d13,ignore_index = True)
df2= df2.append(d14,ignore_index = True)


#calculate average SI
def find_mean(values):
    for i in values:
        t = len(values)
        if (i == 0):
            t -= 1
    return sum(values)/t
df2.loc[3] = df2.apply(find_mean, axis=0)


#add SI row to price file and remove revenue column
df=df.drop('Revenue',axis=1)
df.loc[max(df.index)+1,'Product']='SeasonalIndex'

#copy average SI to price file
k=0
for j in range(1,37):
    df.iloc[max(df.index), j] = df2.iloc[3,k]
    k=k+1
    if(k==12):
        k=0
        
df.to_csv('C:\Users\saisree849\Documents\GitHub\NGS\\6_demand_forecast_vend\\imp_seasonalindex.csv', index=False)