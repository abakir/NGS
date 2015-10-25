__author__ = 'Haroun'
import pandas as pd

raw_segments = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\segments.csv')
customer_value = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\\vend-total_revenue-for-customer-by-year.csv')

# Remove NA's
customer_value = customer_value[customer_value.Revenue.notnull()]

# Keep relevant/related columns
customer_value = customer_value[['Customer', 'Revenue', 'Basket Value', 'Gross Profit']]

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
customer_segments = gather(raw_segments, 'Segment', 'Customer', segment_names)

# Remove NA's generated due to gathering
customer_segments = customer_segments[customer_segments.Customer.notnull()]

# merge
customer_info_with_segments = pd.merge(customer_value, customer_segments, on="Customer")

#group same customers
#customer_info_with_segments = customer_info_with_segments.groupby([ 'Customer', 'Segment'], axis = 0, as_index=False).sum()

# save
customer_info_with_segments.to_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\customer_info_with_segments.csv', index=False)
