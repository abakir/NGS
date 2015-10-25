import pandas as pd
from datetime import datetime
import re

#read
df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\bought_together\orders_export.csv")

#function to get month and year
def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    data = matchobj.group(1)
    matchobj = re.match(r'(.*)-(.*)-(.*).*',data)
    data = matchobj.group(1) + "-" + matchobj.group(2)
    return data

#function to get the number of repeated order no's
def getUnique(data):
    return len(data) - len(set(data))


df = df[['Name', 'Lineitem name', 'Created at']] #subset required columns
df.columns = ['Name', 'Product', 'Date'] #rename columns

df['Date'] = df.Date.apply(convertDate) #call function
df['Product'] = df.Product.apply(lambda x: x.upper()) #change product names to uppercase
df = df.drop_duplicates().reset_index().drop('index',1) #remove products with same names in single order

df = df.groupby(['Date', 'Product'], axis = 0, as_index=False)['Name'].sum() #group by date and product and aggregate the order no's

df['Name'] = df.Name.apply(lambda x: x.split("#")) #split the order no's by #
df['Name'] = df.Name.apply(lambda x: x[1:]) #remove the extra comma

e = df['Date'].tolist() #create a list of dates
#create a list of distinct dates
d = []
for i in e:
    if i not in d:
        d.append(i)
        
df1 = pd.DataFrame(columns = ['Date', 'Product1', 'Product2','Name', 'Count']) #create new dataframe
df = df.set_index('Date') 

pr1 = []
pr2 = []
dat = []
for i in d: #traverse through all months
    p1 = []
    p2 = []
    leng =  len(df.loc[i,'Product']) #count the products in each month
    e = df.loc[i,'Product'].tolist() #make a list of all products in a month
    for j in range(0, leng): #iterate through the length
        p1 = p1 + e
    for k in e: 
        for j in range(0, leng):
            p2.append(k)
            dat.append(i)
    pr1 = pr1 + p1
    pr2 = pr2 + p2
df1['Date'] = pd.Series(dat)
df1['Product1'] = pd.Series(pr1)
df1['Product2'] = pd.Series(pr2)

na = []
for i in d:
    #n = []
    e = df.loc[i,'Name'].tolist()
    for k in e:
        for j in e:
             p = k + j
             na.append(p)
df1['Name'] = pd.Series(na)

df1 = df1[df1.Product1 != df1.Product2]
df1 = df1.reset_index().drop('index',1)

df1['Count'] = df1.Name.apply(getUnique)
df1 = df1[df1.Count != 0]
df1 = df1.reset_index().drop('index',1)

df1 = df1[['Date', 'Product1', 'Product2', 'Count']]
df1['Date'] = df1.Date.apply(lambda x: pd.to_datetime(datetime.strptime(x, '%Y-%m')).date())

df1.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\\bought_together\pair_by_month.csv", index = False)