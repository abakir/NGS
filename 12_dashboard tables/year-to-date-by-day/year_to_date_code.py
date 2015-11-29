import pandas as pd
import re
from datetime import datetime
import os

df = pd.read_csv(os.path.split(os.path.abspath(os.getcwd()))[0]+"\data\\vend-total_revenue-sales_summary-by-day.csv")

def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*) (.*).*',data)
    data = matchobj.group(2)[:-2] + " " + matchobj.group(3) + " " + matchobj.group(4)
    return pd.to_datetime(datetime.strptime(data, '%d %b %Y')).date()
    
df = df[1:5]
df = df.set_index('Unnamed: 0')

df = df.transpose()
df = df.reset_index()
df = df[:max(df.index)-4]
df.columns = ['Date', 'Revenue', 'Cost of Goods', 'Gross Profit', 'Margin']

df['Date'] = df.Date.apply(convertDate)

df.to_csv("year-to-date-by-day.csv", index = False)