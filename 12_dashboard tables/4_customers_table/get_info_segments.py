import pandas as pd
import os

df = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+'\data\orders_export.csv')
df1 = df
df = df[[ 'Email', 'Lineitem quantity', 'Lineitem price']]
df.columns = ['Email', 'Quantity', 'Price']
df['Revenue'] = df['Quantity'] * df['Price']
df = df[['Email', 'Revenue']]
df = df.groupby('Email', axis = 0, as_index=False).sum()
df1 = df1[['Name', 'Email']]
df1.columns = ['Orders', 'Email']
df1 = df1.drop_duplicates().reset_index().drop('index', 1)
df1['Orders'] = 1
df1 = df1.groupby('Email', axis = 0, as_index=False).sum()
df = df.merge(df1, on = ['Email'], how = 'inner')
df['Basket Value'] = df['Revenue'] / df['Orders']
customer_value = df[['Email', 'Revenue', 'Basket Value']]

customers = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+'\data\\customers_export.csv')

customers['Name'] = customers['First Name'] + " " + customers['Last Name']
customers['Address'] = customers['Address1'] + " " + customers['Address2'] + " " + customers['City']

customers = customers[['Name', 'Address', 'Phone', 'Email']]

customer_value = customers.merge(customer_value, on = ['Email'], how = 'inner')

raw_segments = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+'\data\segments.csv')


customer_info_with_segments = raw_segments.merge(customer_value, on = ['Email'], how = 'outer')
customer_info_with_segments = customer_info_with_segments[['Name', 'Revenue', 'Basket Value', 'Segment', 'Email', 'Address', 'Phone' ]]


customer_info_with_segments.to_csv('customers_segments.csv', index=False)