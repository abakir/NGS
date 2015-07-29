from pandas import read_csv
import pandas as pd
import re

location = 'C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\\vend.csv'

df = pd.read_csv(location)

df = df[pd.notnull(df['Product'])]
df = df[df.Revenue != 0]
df=df.sort('Product')
df= df.reset_index().drop('index',1)

df2 = df[['Product', 'Apr-12', 'May-12', 'Jun-12', 'Jul-12', 'Aug-12', 'Sep-12', 'Oct-12', 'Nov-12', 'Dec-12', 'Jan-13', 'Feb-13', 'Mar-13', 'Apr-13', 'May-13', 'Jun-13', 'Jul-13', 'Aug-13', 'Sep-13', 'Oct-13', 'Nov-13', 'Dec-13', 'Jan-14', 'Feb-14', 'Mar-14', 'Apr-14', 'May-14', 'Jun-14', 'Jul-14', 'Aug-14', 'Sep-14', 'Oct-14', 'Nov-14', 'Dec-14', 'Jan-15', 'Feb-15', 'Mar-15', 'Apr-15', 'May-15', 'Jun-15', 'Jul-15', 'Item Count', 'Revenue']]
for i in range(0, max(df2.index)+1):
    df2.loc[i, 'Product'] = df2.loc[i, 'Product'].upper()
    
for i in range(0,max(df2.index)+1):
    df2.loc[i, 'Product'] =df2.loc[i, 'Product'].replace(",","")
    
df2=df2.sort('Product')
df2= df2.reset_index().drop('index',1)

for i in range(0, max(df2.index)+1):
    if re.search('ALL PURPOSE BAKING FLOUR', df2.loc[i,'Product']):
        df2.loc[i, 'Product'] = 'ALL PURPOSE BAKING FLOUR (GLUTEN FREE)'
    elif re.search('AMERICAN GREEN APPLES', df2.loc[i,'Product']):
        df2.loc[i,'Product'] = 'AMERICAN GREEN APPLE'
    elif re.search('AMERICAN RED APPLES', df2.loc[i,'Product']):
        df2.loc[i,'Product'] = 'AMERICAN RED APPLE'
    elif re.search('ARUGULA \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ARUGULA(CHEMICAL FREE)'
    elif re.search('AUBERGENE \(ROUMY\) - ORGANIC', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'AUBERGENE (ROUMY) - CHEMICAL FREE'
    elif re.search('AUBERGINE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'AUBERGENE'
    elif re.search('AVOCADOES \( IMPORTED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'AVOCADOS (IMPORTED)'
    elif re.search('BABY CARROTS - CHEMICAL FREE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BABY CARROTS (CHEMICAL FREE)'
    elif re.search('BABY POTATOES \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BABY POTATOES (CHEMICAL FREE)'
    elif re.search('BABY SPINACH\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BABY SPINACH (CHEMICAL FREE)'
    elif re.search('BALADY EGGS \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BALADY EGGS (CHEMICAL FREE)'
    elif re.search('BALADY EGGS \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BALADY EGGS (CHEMICAL FREE)'
    elif re.search('BANANAS \( IMPORTED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BANANAS (IMPORTED)'
    elif re.search('BEETROOT', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BEET ROOT'
    elif re.search('BEETROOT\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BEETROOT (CHEMICAL FREE)'
    elif re.search('BOLTI FILLET\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BOLTI FILLET (CHEMICAL FREE)'
    elif re.search('BROCCOLI\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'BROCCOLI (CHEMICAL FREE)'
    elif re.search('CARROT \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CARROT  (ORGANIC)'
    elif re.search('CHERRY TOMATOES \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CHERRY TOMATOES (CHEMICAL FREE)'
    elif re.search('CHERRY TOMATO \(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CHERRY TOMATOES (CHEMICAL FREE)'
    elif re.search('CHICKEN BREASTS', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CHICKEN BREAST'
    elif re.search('CHICKEN CUTLETS \(SHISHTAWOOK-CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CHICKEN CUTLETS - SHISHTAWOOK (CHEMICAL FREE)'
    elif re.search('COLORED BELL PEPPER \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'COLORED BELL PEPPER (CHEMICAL FREE)'
    elif re.search('CORIANDER \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CORIANDER (CHEMICAL FREE)'
    elif re.search('CORIANDER \( CHMEICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CORIANDER (CHEMICAL FREE)'
    elif re.search('CORIANDER\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CORIANDER (CHEMICAL FREE)'
    elif re.search('CUCUMBER \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CUCUMBER (CHEMICAL FREE)'
    elif re.search('CUCUMBER \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CUCUMBER (CHEMICAL FREE)'
    elif re.search('CUCUMBER - CHEMICAL FREE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'CUCUMBER (CHEMICAL FREE)'
    elif re.search('DILL \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DILL (CHEMICAL FREE)'
    elif re.search('DRIED CRANBERRY', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED CRANBERRIES'
    elif re.search('DRIED DATES - KHEIR MISR', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED DATES (KHEIR MISR)'
    elif re.search('DRIED LEMONGRASS \(CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED LEMONGRASS (CHEMICAL FREE)'
    elif re.search('DRIED NECTARINE  \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED NECTARINE (CHEMICAL FREE)'
    elif re.search('DRIED PEACH \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED PEACH (CHEMICAL FREE)'
    elif re.search('DRIED PEAR \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DRIED PEARS (CHEMICAL FREE )'
    elif re.search('DUCK\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'DUCK (CHEMICAL FREE)'
    elif re.search('FENNEL \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'FENNEL (CHEMICAL FREE)'
    elif re.search('FRENCH PARSELY \(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'FRENCH PARSLEY (CHEMICAL FREE)'
    elif re.search('FRESH GINGER \( IMPORTED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'FRESH GINGER (IMPORTED)'
    elif re.search('GARLIC\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GARLIC (CHEMICAL FREE)'
    elif re.search('GARLIC \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GARLIC (CHEMICAL FREE)'
    elif re.search('GRAPEFRUIT', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GRAPE FRUIT'
    elif re.search('GREEN APPLES \( FRENCH \) -IMPORTED', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GREEN APPLES (FRENCH) - IMPORTED'
    elif re.search('GREEN BEANS \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GREEN BEANS (CHEMICAL FREE)'
    elif re.search('GREEN ICEBERG LETTUCE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GREEN ICE BERG LETTUCE'
    elif re.search('GREEN ONION \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GREEN ONIONS (CHEMICAL FREE)'
    elif re.search('GREEN ONIONS \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'GREEN ONIONS (CHEMICAL FREE)'
    elif re.search('ICE BERG LETTUCE - CHEMICAL FREE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ICE BERG LETTUCE (CHEMICAL FREE)'
    elif re.search('ICEBERG LETTUCE\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ICE BERG LETTUCE (CHEMICAL FREE)'
    elif re.search('LEMON GRASS\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'LEMON GRASS (CHEMICAL FREE)'
    elif re.search('LIME \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'LIME(CHEMICAL FREE)'
    elif re.search('LOLLA ROSSA LETTUCE\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'LOLLA ROSSA LETTUCE (CHEMICAL FREE)'
    elif re.search('MOLOKHEYA \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'MOLOKHEYA (CHEMICAL FREE)'
    elif re.search('MOLOKHYIA \(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'MOLOKHEYA (CHEMICAL FREE)'
    elif re.search('MOLOKHYIA\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'MOLOKHEYA (CHEMICAL FREE)'
    elif re.search('OAT MILK \( ORIGINAL \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'OAT MILK ( ORGANIC )'
    elif re.search('PARSELY\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PARSLEY (CHEMICAL FREE)'
    elif re.search('PARSLEY \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PARSLEY (CHEMICAL FREE)'
    elif re.search('PEARS ( AMERICAN ) - IMPORTED', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PEARS (AMERICAN) - IMPORTED'
    elif re.search('PEPPERMINT', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PEPPER MINT'
    elif re.search('PINK GRAPEFRUIT', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PINK GRAPE FRUIT'
    elif re.search('PINK GRAPFRUIT', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PINK GRAPE FRUIT'
    elif re.search('PINKGRAPFRUITS', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'PINK GRAPE FRUIT'
    elif re.search('POTATOES\( CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'POTATOES (CHEMICAL FREE)'
    elif re.search('POTATOES \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'POTATOES (CHEMICAL FREE)'
    elif re.search('QUINOA \(CHEMICAL FREE\) - LOCAL', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'QUINOA (CHEMICAL FREE) - EGYPTIAN'
    elif re.search('RAW ALMONDS - SHELLED', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RAW ALMONDS SHELLED'
    elif re.search('RAW HONEY \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RAW HONEY (NATURAL)'
    elif re.search('RAW SUNFLOWER SEED \( SHELLED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RAW SUNFLOWER SEED SHELLED'
    elif re.search('RED APPLES \( AMERICAN \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED APPLES (AMERICAN)'
    elif re.search('RED CABBAGE\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED CABBAGE (CHEMICAL FREE)'
    elif re.search('RED CHILI PEPPER \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED CHILLI PEPPER ( CHEMICAL FREE )'
    elif re.search('RED GRAPES \( IMPORTED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED GRAPES (IMPORTED)'
    elif re.search('RED GRAPES - SEEDLESS\(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED GRAPES - SEEDLESS(CHEMICAL FREE)'
    elif re.search('RED ONION \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED ONION (CHEMICAL FREE)'
    elif re.search('RED ONIONS \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED ONION (CHEMICAL FREE)'
    elif re.search('RED ONION', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED ONIONS'
    elif re.search('RED PLUM', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED PLUMS'
    elif re.search('RED PLUMS \( IMPORTED \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED PLUMS (IMPORTED)'
    elif re.search('RED RADISH\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED RADISH (CHEMICAL FREE)'
    elif re.search('RED SWISS CHARD\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'RED SWISS CHARD (CHEMICAL FREE)'
    elif re.search('ROSAMARRY\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ROSEMERY (CHEMICAL FREE)'
    elif re.search('ROSEMARY\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ROSEMERY (CHEMICAL FREE)'
    elif re.search('SHORT GRAIN BROWN RICE \( ECO FARMED \) - ORGANIC', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SHORT GRAIN BROWN RICE ( ORGANIC ) - ECO FARMED'
    elif re.search('SMOKED SALMON \( FROZEN \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SMOKED SALMON (FROZEN)'
    elif re.search('SOYA MILK \( ORIGINAL \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SOYA MILK ( ORGANIC )'
    elif re.search('SPINACH\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SPINACH ( CHEMICAL FREE )'
    elif re.search('SPINASH', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SPINACH'
    elif re.search('SPRING ONION \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SPRING ONION (CHEMICAL FREE)'
    elif re.search('STRAWBERRY', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'STRAWBERRIES'
    elif re.search('SWEET BASIL\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET BASIL (CHEMICAL FREE)'
    elif re.search('SWEET POTATOES\(CHEMICAL FREE\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET POTATOES (CHEMICAL FREE)'
    elif re.search('SWEET POTATOES \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET POTATOES (CHEMICAL FREE)'
    elif re.search('SWEET POTATO \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET POTATOES (CHEMICAL FREE)'
    elif re.search('SWEET POTATO \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET POTATOES (CHEMICAL FREE)'
    elif re.search('SWEET POTATO', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'SWEET POTATOES'
    elif re.search('THYME \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'THYME (CHEMICAL FREE)'
    elif re.search('TOMATO \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'TOMATO (CHEMICAL FREE)'
    elif re.search('TOMATO - CHEMICAL FREE', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'TOMATO (CHEMICAL FREE)'
    elif re.search('UNSWEETENED SOY MILK \( ORIGINAL \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'UNSWEETENED SOY MILK ( ORGANIC )'
    elif re.search('VEAL ESCALOPE \(CHEMICAL FREE\) - FROZENFROZEN', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'VEAL ESCALOPE (CHEMICAL FREE) FROZEN'
    elif re.search('VEAL LIVER \(CHEMICAL FREE\) - FROZEN', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'VEAL LIVER (CHEMICAL FREE) FROZEN'
    elif re.search('WHITE GRAPES \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'WHITE GRAPES ( CHEMICAL FREE )'
    elif re.search('ZUCCHINI \( CHEMICAL FREE \)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ZUCCHINI (CHEMICAL FREE)'
    elif re.search('ZUCCHINI \(ORGANIC\)', df2.loc[i, 'Product']):
        df2.loc[i, 'Product'] = 'ZUCCHINI (CHEMICAL FREE)'
    
    
df2.to_csv("C:\Users\saisree849\Documents\GitHub\NGS_Project\\5_demand_forecast\\allrenamedprods.csv",sep=",",index=False,header=None)