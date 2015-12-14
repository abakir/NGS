import yaml
import os
import sys
with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)


sys.path.insert(0, os.path.join(cfg['root']+cfg['bought_together']))
import bought_together_all
execfile(os.path.join(cfg['root']+cfg['bought_together']+cfg['fbought_together_all']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['bought_together']))
import monthly_bought_together
execfile(os.path.join(cfg['root']+cfg['bought_together']+cfg['fmonthly_bought_together']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customer_retention']))
import retention_calc
execfile(os.path.join(cfg['root']+cfg['customer_retention']+cfg['fretention_calc']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_dates']))
import get_customer_dates
execfile(os.path.join(cfg['root']+cfg['customers_dates']+cfg['fget_customer_dates']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import get_day_hour_purchases_1
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_day_hour_purchases']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import get_info_segments_2
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_info_segments']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import get_latest_order_days_3
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_latest_order_days']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import get_order_frequency_customer_4
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_order_frequency_customer']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import merge_tables_5
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fmerge_tables']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['order_frequency']))
import get_order_frequency
execfile(os.path.join(cfg['root']+cfg['order_frequency']+cfg['fget_order_frequency']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['product_table']))
import get_products_table
execfile(os.path.join(cfg['root']+cfg['product_table']+cfg['fget_products_table']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['products_dates']))
import get_products_dates
execfile(os.path.join(cfg['root']+cfg['products_dates']+cfg['fget_products_dates']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['revenue_by_type']))
import Revenue_by_type_code
execfile(os.path.join(cfg['root']+cfg['revenue_by_type']+cfg['fRevenue_by_type_code']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['unfulfilled_orders']))
import unfulfilled_orders_week
execfile(os.path.join(cfg['root']+cfg['unfulfilled_orders']+cfg['funfulfilled_orders_week']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['unfulfilled_orders']))
import unfulfilled_orders_yr
execfile(os.path.join(cfg['root']+cfg['unfulfilled_orders']+cfg['funfulfilled_orders_yr']))

sys.path.insert(0, os.path.join(cfg['root']+cfg['year-to-date-by-day']))
import year_to_date_code
execfile(os.path.join(cfg['root']+cfg['year-to-date-by-day']+cfg['fyear_to_date_code']))

