import pandas as pd

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers_segments.csv")
df1 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\latest_order.csv")
df3 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\\frequency.csv")
df5 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customer_days_time.csv")

df.columns = ['Name', 'Revenue', 'Basket Value', 'Segment', 'Email', 'Address', 'Phone' ]
df10 = df1.merge(df3, on = ['Email'], how = 'inner')

df6 = df10.merge(df5, on = ['Email'], how = 'inner')

df2 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers_export.csv")
df2 = df6.merge(df2, on = ['Email'], how = 'inner')

df2 = df2[['First Name', 'Last Name', 'Average', 'Email', 'Days from Last order', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0', '6', '12', '18']]

for i in range(0, max(df2.index)+1):
    df2.loc[i, 'Name'] = df2.loc[i, 'First Name'] + " " + df2.loc[i, 'Last Name']

df4 = df2.merge(df, on = ['Name', 'Email'], how = 'inner')

df4 = df4[['Name', 'Revenue', 'Basket Value', 'Segment', 'Address','Phone', 'Average', 'Email', 'Days from Last order', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', '0', '6', '12', '18']]

df4.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers.csv",index = False)