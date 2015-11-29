import pandas as pd

df = pd.read_csv("customers_segments.csv")
df1 = pd.read_csv("latest_order.csv")
df3 = pd.read_csv("frequency.csv")
df5 = pd.read_csv("customer_days_time.csv")

df.columns = ['Name', 'Revenue', 'Basket Value', 'Segment', 'Email', 'Address', 'Phone' ]
df10 = df1.merge(df3, on = ['Email'], how = 'inner')

df6 = df10.merge(df5, on = ['Email'], how = 'inner')

df6 = df6.merge(df, on = ['Email'], how = 'outer')

df2 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\data\customers_export.csv")
df2 = df6.merge(df2, on = ['Email'], how = 'inner')

df2 = df2[['First Name', 'Last Name', 'Total orders', 'Average days between orders', 'Email', 'Days from Last order', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0:00 - 2:00', '2:00 - 4:00', '4:00 - 6:00', '6:00 - 8:00', '8:00 - 10:00', '10:00 - 12:00', '12:00 - 14:00', '14:00 - 16:00', '16:00 - 18:00', '18:00 - 20:00', '20:00 - 22:00', '22:00 - 0:00']]

for i in range(0, max(df2.index)+1):
    df2.loc[i, 'Name'] = df2.loc[i, 'First Name'] + " " + df2.loc[i, 'Last Name']

df4 = df2.merge(df, on = ['Name', 'Email'], how = 'inner')

df4 = df4[['Name', 'Revenue', 'Basket Value', 'Segment', 'Address','Phone', 'Total orders', 'Average days between orders', 'Email', 'Days from Last order', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0:00 - 2:00', '2:00 - 4:00', '4:00 - 6:00', '6:00 - 8:00', '8:00 - 10:00', '10:00 - 12:00', '12:00 - 14:00', '14:00 - 16:00', '16:00 - 18:00', '18:00 - 20:00', '20:00 - 22:00', '22:00 - 0:00']]

df = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\data\orders_export.csv')
df1 = df[['Lineitem quantity', 'Lineitem price']]
df1['Revenue'] = df1.apply(lambda x: x['Lineitem quantity'] * x['Lineitem price'], axis=1)
df1=df1[['Lineitem quantity', 'Revenue']]
df = df[['Email']]
df = df.drop_duplicates().reset_index().drop('index',1)

df1 = df1.sum()
df4['Average Revenue'] = df1['Revenue']/float(max(df.index)+1)
df4['Average Basket Size'] = df1['Lineitem quantity']/float(max(df.index)+1)

df3 = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\monthly_segments\cust_score.csv')
df3.columns = [u'Email', u'Beef', u'Dried fruits and nuts', u'Fresh Beef & Poultry', u'Fruits', u'General', u'Rice and pasta', u'Vegetables', u'Beverages', u'Cosmetics', u'Dairy', u'Food supplements', u'Grains_Seeds_Cereal', u'Herbs', u'Oil_ Vinegar_Sauces', u'Bakery', u'Condiments and paste', u'Poultry', u'Chocolate_cookies_snacks', u'Jams & spreads & honey', u'Non-dairy', u'Seafood', u'Gluten free', u'Herbal pharmacy', u'Tea and herbal drinks', u'Accessories', u'Lamb', u'Prepared food', u'Home appliance', u'Books']
df4 = df4.merge(df3, on = ['Email'], how='left')

df4[['Total orders', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0:00 - 2:00', '2:00 - 4:00', '4:00 - 6:00', '6:00 - 8:00', '8:00 - 10:00', '10:00 - 12:00', '12:00 - 14:00', '14:00 - 16:00', '16:00 - 18:00', '18:00 - 20:00', '20:00 - 22:00', '22:00 - 0:00']] = df4[['Total orders', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0:00 - 2:00', '2:00 - 4:00', '4:00 - 6:00', '6:00 - 8:00', '8:00 - 10:00', '10:00 - 12:00', '12:00 - 14:00', '14:00 - 16:00', '16:00 - 18:00', '18:00 - 20:00', '20:00 - 22:00', '22:00 - 0:00']].astype(float)
df4.to_csv("customers.csv",index = False)