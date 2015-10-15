import pandas as pd
import re
from datetime import datetime

def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*) (.*).*',data)
    data = matchobj.group(2)[0] + " " + matchobj.group(3) + " " + matchobj.group(4)
    return pd.to_datetime(datetime.strptime(data, '%d %b %Y')).date()


df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_7_days\\vend-gross_profit-sales_summary-by-day.csv")
#remove extra rows
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
#get only days columns
df = df.iloc[0,range(0,7)]
#create dataframe
gp = pd.DataFrame(df)
#create integer index
gp = gp.reset_index(level=0)
#rename columns
gp.columns = ['Day', 'Gross Profit']

gp['Day'] = gp.Day.apply(convertDate)



df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_7_days\\vend-total_revenue-sales_summary-by-day.csv")
df = df[:max(df.index)-4]
del df['Unnamed: 0']
df = df.iloc[0,range(0,7)]
rv = pd.DataFrame(df)
rv = rv.reset_index(level=0)
rv.columns = ['Day', 'Revenue']
rv['Day'] = rv.Day.apply(convertDate)



df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_7_days\\vend-margin-sales_summary-by-day.csv")
df = df[:max(df.index)-4]
del df['Unnamed: 0']
df = df.iloc[0,range(0,7)]
mg = pd.DataFrame(df)
mg = mg.reset_index(level=0)
mg.columns = ['Day', 'Margin']
mg['Day'] = mg.Day.apply(convertDate)


df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_7_days\\vend-total_cost-sales_summary-by-day.csv")
df = df[:max(df.index)-4]
del df['Unnamed: 0']
df = df.iloc[0,range(0,7)]
cg = pd.DataFrame(df)
cg = cg.reset_index(level=0)
cg.columns = ['Day', 'Cost of Goods']
cg['Day'] = cg.Day.apply(convertDate)

days_7 = rv.merge(cg, on=['Day'], how='inner')
days_7 = days_7.merge(gp, on=['Day'], how='inner')
days_7 = days_7.merge(mg, on=['Day'], how='inner')

days_7.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_7_days\\last_7_days.csv",index=False)