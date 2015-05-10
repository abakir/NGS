from pandas import read_csv, DataFrame
import pandas as pd

location = "C:\Users\saisree849\Documents\GitHub\NGS_Project\\3_customer_basket\customerbasket.csv"

df = read_csv(location, header=None)

df.columns=['Email', 'Created at', 'Quantity', 'Itemname', 'Sku', 'Vendor']

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\3_customer_basket\\finalbasket.csv", sep =",")