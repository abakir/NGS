from pandas import read_csv, DataFrame
import pandas as pd

location = "C:\Users\saisree849\Documents\GitHub\NGS_Project\\2_group_by_customer\grouped.csv"

df = read_csv(location, header=None)

df.columns=['Email', 'Quantity', 'Itemname', 'Sku', 'Vendor', 'Date', 'Time', 'Hours', 'Day']

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\2_group_by_customer\custgroup.csv", sep =",")