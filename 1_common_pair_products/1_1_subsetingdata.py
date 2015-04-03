from pandas import read_csv
import pandas as pd
import numpy as np
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\1_common_pair_products\orders_export-2.csv'

df = pd.read_csv(location)

df.columns = ['Name','Email','Financial Status','Paid at','Fulfillment Status','Fulfilled at','Accepts Marketing','Currency','Subtotal','Shipping','Taxes','Total','Discount Code','Discount Amount','Shipping Method','Created at','Lineitem quantity','Lineitem name','Lineitem price','Lineitem compare at price','Lineitem sku','Lineitem requires shipping','Lineitem taxable','Lineitem fulfillment status','Billing Name','Billing Street','Billing Address1','Billing Address2','Billing Company','Billing City','Billing Zip','Billing Province','Billing Country','Billing Phone','Shipping Name','Shipping Street','Shipping Address1','Shipping Address2','Shipping Company','Shipping City','Shipping Zip','Shipping Province','Shipping Country','Shipping Phone','Notes','Note Attributes','Cancelled at','Payment Method','Payment Reference','Refunded Amount','Vendor','Id','Tags','Risk Level','Source','Lineitem discount','Tax 1 Name','Tax 1 Value','Tax 2 Name','Tax 2 Value','Tax 3 Name','Tax 3 Value','Tax 4 Name','Tax 4 Value','Tax 5 Name','Tax 5 Value']


df = df[0:11025]
df = df[['Name','Email','Created at','Lineitem name','Lineitem sku']]


df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\1_common_pair_products\\reqddata.csv", sep=',')