import pandas as pd
import re
from datetime import datetime

def convertDate(data):
    matchobj = re.match(r'(.*) (.*) (.*).*',data)
    data = matchobj.group(1)[:-2] + " " + matchobj.group(2) + " " + matchobj.group(3)
    return pd.to_datetime(datetime.strptime(data, '%d %b %Y')).date()

df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\vend-gross_profit-sales_summary-by-week.csv")
#remove extra rows
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
#get only weeks columns
df = df.iloc[0,range(0,4)]
#create dataframe
gp = pd.DataFrame(df)
#create integer index
gp = gp.reset_index(level=0)
#rename columns
gp.columns = ['Week', 'Gross Profit'] 
gp['Week'] = gp.Week.apply(convertDate)



df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\vend-total_revenue-sales_summary-by-week.csv")
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
df = df.iloc[0,range(0,4)]
rv = pd.DataFrame(df)
#create integer index
rv = rv.reset_index(level=0)
#rename columna
rv.columns = ['Week', 'Revenue'] 
rv['Week'] = rv.Week.apply(convertDate)


df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\vend-margin-sales_summary-by-week.csv")
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
df = df.iloc[0,range(0,4)]
mg = pd.DataFrame(df)
#create integer index
mg = mg.reset_index(level=0)
#rename columna
mg.columns = ['Week', 'Margin'] 
mg['Week'] = mg.Week.apply(convertDate)


df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\vend-total_cost-sales_summary-by-week.csv")
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
df = df.iloc[0,range(0,4)]
cg = pd.DataFrame(df)
#create integer index
cg = cg.reset_index(level=0)
#rename columna
cg.columns = ['Week', 'Cost of Goods'] 
cg['Week'] = cg.Week.apply(convertDate)


df = pd.read_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\vend-basket_value-sales_summary-by-week.csv")
df = df[:max(df.index)-4]
#remove the initial column
del df['Unnamed: 0']
df = df.iloc[0,range(0,4)]
bv = pd.DataFrame(df)
#create integer index
bv = bv.reset_index(level=0)
#rename columns
bv.columns = ['Week', 'Basket Value'] 
bv['Week'] = bv.Week.apply(convertDate)



weeks_4 = bv.merge(rv, on=['Week'], how='inner')
weeks_4 = weeks_4.merge(cg, on=['Week'], how='inner')
weeks_4 = weeks_4.merge(gp, on=['Week'], how='inner')
weeks_4 = weeks_4.merge(mg, on=['Week'], how='inner')


for i in range(0, max(weeks_4.index)+1):
    weeks_4.loc[i, 'Orders'] = round((weeks_4.loc[i, 'Revenue'] / weeks_4.loc[i, 'Basket Value']), 2)


weeks_4.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\last_4_weeks\\last_4_weeks.csv",index=False)