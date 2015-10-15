import pandas as pd

df = pd.read_csv("C:\Users\saisree849\AppData\Roaming\Skype\My Skype Received Files\customers.csv")
df1 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\latest_order.csv")
df3 = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\10_order_frequency\\frequency.csv")

df1.columns =['Email', 'Days from Last order', 'Name']

df2 = df1.merge(df3, on = ['Name', 'Email'], how = 'inner')

df4 = df2.merge(df, on = ['Name', 'Email'], how = 'inner')

df4 = df4[['Name', 'Revenue', 'Basket Value', 'Gross Profit', 'Segment', 'Address','Phone', 'Average', 'Email', 'Days from Last order']]

df4.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers.csv",index = False)