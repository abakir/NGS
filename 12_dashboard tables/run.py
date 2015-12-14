import yaml
import os
import sys
with open("config.yaml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)


sys.path.insert(0, os.path.join(cfg['root']+cfg['bought_together']))
import cfg['bought_together_all']
execfile(os.path.join(cfg['root']+cfg['bought_together']+cfg['fbought_together_all']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['bought_together']))
import cfg['monthly_bought_together']
execfile(os.path.join(cfg['root']+cfg['bought_together']+cfg['fmonthly_bought_together']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customer_retention']))
import cfg['retention_calc']
execfile(os.path.join(cfg['root']+cfg['customer_retention']+cfg['fretention_calc']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_dates']))
import cfg['get_customer_dates']
execfile(os.path.join(cfg['root']+cfg['customers_dates']+cfg['fget_customer_dates']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import cfg['get_day_hour_purchases']
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_day_hour_purchases']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import cfg['get_info_segments']
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_info_segments']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import cfg['get_latest_order_days']
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_latest_order_days']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import cfg['get_order_frequency_customer']
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fget_order_frequency_customer']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['customers_table']))
import cfg['merge_tables']
execfile(os.path.join(cfg['root']+cfg['customers_table']+cfg['fmerge_tables']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['order_frequency']))
import cfg['get_order_frequency']
execfile(os.path.join(cfg['root']+cfg['order_frequency']+cfg['fget_order_frequency']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['product_table']))
import cfg['get_products_table']
execfile(os.path.join(cfg['root']+cfg['product_table']+cfg['fget_products_table']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['products_dates']))
import cfg['get_products_dates']
execfile(os.path.join(cfg['root']+cfg['products_dates']+cfg['fget_products_dates']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['revenue_by_type']))
import cfg['Revenue_by_type_code']
execfile(os.path.join(cfg['root']+cfg['revenue_by_type']+cfg['fRevenue_by_type_code']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['unfulfilled_orders']))
import cfg['unfulfilled_orders_week']
execfile(os.path.join(cfg['root']+cfg['unfulfilled_orders']+cfg['funfulfilled_orders_week']))


sys.path.insert(0, os.path.join(cfg['root']+cfg['unfulfilled_orders']))
import cfg['unfulfilled_orders_yr']
execfile(os.path.join(cfg['root']+cfg['unfulfilled_orders']+cfg['funfulfilled_orders_yr']))

sys.path.insert(0, os.path.join(cfg['root']+cfg['year-to-date-by-day']))
import cfg['year_to_date_code']
execfile(os.path.join(cfg['root']+cfg['year-to-date-by-day']+cfg['fyear_to_date_code']))

