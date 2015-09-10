import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\producttype.csv'
df = pd.read_csv(location)
df1=df

for i in range(0, max(df1.index)+1):
    if ('CHICKENBREASTS1KG' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'CHICKENBREAST'
    elif ('AVOCADO' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'AVOCADOSIMPORTED'
    elif ('AVOCADOESIMPORTED' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'AVOCADOSIMPORTED'
    elif ('WHOLECHICKEN1KG' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'WHOLECHICKEN'
    elif ('SALMONSTEAKFROZEN' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'SALMONSTEAK'
    elif ('PREMIUMNORWEGIANSALMONSTEAK' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'SALMONSTEAK'
    elif ('BALADYWHOLECHICKENCHEMICALFREEDEFAULT' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'BALADYWHOLECHICKENCHEMICALFREE'
    elif ('BANANA' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'BANANASIMPORTED'
    elif ('DUCKCHEMICALFREE' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'DUCK'
    elif ('APPLECIDERVINEGARORGANIC473G' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'APPLECIDERVINEGARORGANIC'
    elif ('ORGANICREDQUINOA454G' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'QUINOAREDPERU'
    elif ('REDQUINOA' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'QUINOAREDPERU'
    elif ('SPINACH' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'BABYSPINACHCHEMICALFREE'
    elif ('PINEAPPLE' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'SWEETPINEAPPLES'
    elif ('ALLPURPOSEBAKINGFLOURGLUTENFREE623G' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'ALLPURPOSEBAKINGFLOURGLUTENFREE'
    elif ('BROWNRICEEGYPTIAN750G' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'BROWNRICEEGYPTIAN'
    elif ('FRESHGINGER' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'FRESHGINGERIMPORTED'
    elif ('GREENASPARAGUSDEFAULT' == df1.loc[i,'Product']):
        df1.loc[i, 'Product'] = 'GREENASPARAGUS'
        
location='C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\\imp_price.csv'
df=pd.read_csv(location)

df2=pd.DataFrame(columns=df1.columns)
for i in range(0,max(df1.index)+1):
    for j in range(0,max(df.index)+1):
        if(df.loc[j,'Product']==df1.loc[i,'Product']):
            df2.loc[i,'Email']=df1.loc[i,'Email']
            df2.loc[i,'Quantity']=df1.loc[i,'Quantity']
            df2.loc[i,'Product']=df1.loc[i,'Product']
            df2.loc[i,'Price']=df1.loc[i,'Price']
            df2.loc[i,'Type']=df1.loc[i,'Type']
df2= df2.reset_index().drop('index',1)

df2.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\7_customer_orders\\allimp.csv',Index=None, Header = False)
