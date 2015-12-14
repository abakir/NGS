import os
import sys
f = open('./config.yaml', 'w')

#root folder
f.write("root: "+os.getcwd())

#subfolders
f.write("\ndata: /data")
f.write("\nbought_together: /1_bought_together")
f.write("\ncustomer_retention: /2_customer_retention")
f.write("\ncustomers_dates: /3_customers_dates")
f.write("\ncustomers_table: /4_customers_table")
f.write("\norder_frequency: /5_order_frequency")
f.write("\nproduct_table: /6_products_table")
f.write("\nproducts_dates: /7_products_dates")
f.write("\nrevenue_by_type: /8_revenue_by_type")
f.write("\nunfulfilled_orders: /9_unfulfilled_orders")
f.write("\nyear-to-date-by-day: /10_year-to-date-by-day")
f.write("\nmonthly_segments: /11_monthly_segments")
f.write("\noutput: /output")

#code files with extention
f.write("\nfbought_together_all: /bought_together_all.py")
f.write("\nfmonthly_bought_together: /monthly_bought_together.py")
f.write("\nfretention_calc: /retention_calc.py")
f.write("\nfget_customer_dates: /get_customer_dates.py")
f.write("\nfget_day_hour_purchases: /get_day_hour_purchases_1.py")
f.write("\nfget_info_segments: /get_info_segments_2.py")
f.write("\nfget_latest_order_days: /get_latest_order_days_3.py")
f.write("\nfget_order_frequency_customer: /get_order_frequency_customer_4.py")
f.write("\nfmerge_tables: /merge_tables_5.py")
f.write("\nfget_order_frequency: /get_order_frequency.py")
f.write("\nfget_products_table: /get_products_table.py")
f.write("\nfget_products_dates: /get_products_dates.py")
f.write("\nfRevenue_by_type_code: /Revenue_by_type_code.py")
f.write("\nfunfulfilled_orders_week: /unfulfilled_orders_week.py")
f.write("\nfunfulfilled_orders_yr: /unfulfilled_orders_yr.py")
f.write("\nfyear_to_date_code: /year_to_date_code.py")

#input files
f.write("\nsegments: /segments.csv")
f.write("\norders: /orders_export.csv")
f.write("\ncustomers: /customers_export.csv")
f.write("\nproducts: /products_export.csv")
f.write("\ngross_profit_prod: /vend-gross_profit-for-product_variant-by-month.csv")
f.write("\ngross_profit_type: /vend-gross_profit-for-type-by-month.csv")
f.write("\ntotal_revenue_prod: /vend-total_revenue-for-product_variant-by-month.csv")
f.write("\ntotal_revenue_type: /vend-total_revenue-for-type-by-month.csv")
f.write("\ntotal_revenue_daily: /vend-total_revenue-sales_summary-by-day.csv")

#output files
f.write("\npair_complete: /pair_complete.csv")
f.write("\npair_by_month: /pair_by_month.csv")
f.write("\nwith_retention: /with_retention.csv")
f.write("\ncustomer_dates: /customer_dates.csv")
f.write("\ncustomer_days_time: /customer_days_time.csv")
f.write("\ncustomers_segments: /customers_segments.csv")
f.write("\nlatest_order: /latest_order.csv")
f.write("\nfrequency: /frequency.csv")
f.write("\ncustomers_mid: /customers.csv")
f.write("\norder_frequency: /order_frequency.csv")
f.write("\nproducts: /products.csv")
f.write("\nproducts_dates: /products_dates.csv")
f.write("\nRevenue_by_type: /Revenue_by_type.csv")
f.write("\nunfulfilled: /unfulfilled.csv")
f.write("\nunfulfilled_yr: /unfulfilled_yr.csv")
f.write("\nyear-to-date-by-day: /year-to-date-by-day.csv")
f.write("\ncust_score: /cust_score.csv")


