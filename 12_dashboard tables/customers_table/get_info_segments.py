import pandas as pd

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\orders_export.csv")
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

customers = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\\customers_export.csv')

customers['Name'] = customers['First Name'] + " " + customers['Last Name']
customers['Address'] = customers['Address1'] + " " + customers['Address2'] + " " + customers['City']

customers = customers[['Name', 'Address', 'Phone', 'Email']]

customer_value = customers.merge(customer_value, on = ['Email'], how = 'inner')

raw_segments = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\segments.csv')
# 18 segments in total
segment_names = ['Sea Food', 'Vegetables', 'Herbs & Herbal Drinks', 'Variety', 'Dairy',
                 'Cosmetics', 'Poultry', 'Beverages', 'Oil & Vinegar', 'Grains & Seeds & Cereal',
                 'Honey & Jams & Sweeteners', 'Condiments', 'Rice & Pasta', 'Dried Fruits & Nuts',
                 'Bakery', 'Fruits', 'Meat', 'Snacks']

# like tidyr in R
def gather(df, key, value, cols):
    id_vars = [col for col in df.columns if col not in cols]
    id_values = cols
    var_name = key
    value_name = value
    return pd.melt(df, id_vars, id_values, var_name, value_name)

# gather column names into "Segment" variable
customer_segments = gather(raw_segments, 'Segment', 'Name', segment_names)

# Remove NA's generated due to gathering
customer_segments = customer_segments[customer_segments.Name.notnull()]

# merge
customer_info_with_segments = pd.merge(customer_value, customer_segments, on="Name")

customer_info_with_segments = customer_info_with_segments[['Name', 'Revenue', 'Basket Value', 'Segment', 'Email', 'Address', 'Phone' ]]

customer_info_with_segments.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers_segments.csv', index=False)