__author__ = 'haroun'
import pandas as pd

# read 3 files of customers data from vend
df1 = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\\vend-customers\\vend-customers-1.csv', error_bad_lines = False, warn_bad_lines = False)
df2 = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\\vend-customers\\vend-customers-2.csv', error_bad_lines = False, warn_bad_lines = False)
df3 = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\\vend-customers\\vend-customers-3.csv', error_bad_lines = False, warn_bad_lines = False)

# read the customer info with segments file
customer_value = pd.read_csv('C:\Users\saisree849\Documents\GitHub\NGS-master\\14_customers\customer_info_with_segments.csv')

# combine into one data frame
customers = pd.concat([df1, df2, df3])

# Customer name is defined as first_name + last_name, this will be used to match other vend tables
customers['Customer'] = customers.first_name + ' ' + customers.last_name

# check if this customer has an email in the customers table
def check_mail(customer):
    if customer in customers.Customer.values:
        return customers[customer == customers.Customer]['email'].values[0]

# check if this customer has an address in the customers table
def check_address(customer):
    if customer in customers.Customer.values:
        return customers[customer == customers.Customer]['postal_address1'].values[0]

# check if this customer has a phone number in the customers table
def check_phone(customer):
    if customer in customers.Customer.values:
        return customers[customer == customers.Customer]['phone'].values[0]

# check if this customer has a mobile number in the customers table
def check_mobile(customer):
    if customer in customers.Customer.values:
        return customers[customer == customers.Customer]['mobile'].values[0]

# fill email, address, phone and mobile columns with values (if found)
customer_value['email'] = customer_value.Customer.apply(check_mail)
customer_value['address'] = customer_value.Customer.apply(check_address)
customer_value['phone'] = customer_value.Customer.apply(check_phone)
customer_value['mobile'] = customer_value.Customer.apply(check_mobile)

# save
customer_value.to_csv('C:\Users\saisree849\Documents\GitHub\NGS_Project\\12_dashboard tables\customers_table\customers_segments.csv', index=False)
