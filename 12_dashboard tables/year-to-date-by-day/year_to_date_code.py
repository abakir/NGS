import pandas as pd
import re
from datetime import datetime

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\year-to-date-by-day\\vend-total_revenue-sales_summary-by-day.csv")

def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*) (.*).*',data)
    data = matchobj.group(2)[:-2] + " " + matchobj.group(3) + " " + matchobj.group(4)
    return pd.to_datetime(datetime.strptime(data, '%d %b %Y')).date()
    
df = df[1:5]
df = df.set_index('Unnamed: 0')

df = df.transpose()
df = df.reset_index()
df = df[:max(df.index)-4]
df.columns = ['Day', 'Revenue', 'Cost of Goods', 'Gross Profit', 'Margin']

df['Day'] = df.Day.apply(convertDate)

df.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\year-to-date-by-day\year-to-date-by-day.csv", index = False)