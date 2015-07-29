from pandas import read_csv
import pandas as pd

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\\reqdprods.csv'

df = pd.read_csv(location,header = None)

df=df.rename(columns={0: 'Product', 41:'Itemcount',42:'Revenue'})

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\groupedprod.csv",sep=",",index=False)