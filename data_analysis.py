#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import re

#filling in the path to my working directory
file_path = ""
transactio_data = pd.read_csv(file_path + "QVI_transaction_data.csv")
customer_data = pd.read_csv(file_path + "QVI_purchase_behaviour.csv")

# Examining transaxtion data
print(transaction_data.info())
ptint(transaction_data.head())

# Example plot using matplotlib
plt.hist(transaction_data['coloumn_name'])
plt.xlabel('X label')
plt.ylabel('Y label')
plt.title('Title')
plt.show()

# Convert date column to date format
transaction.data['DATE'] = pd.to_datetime(transaction.data['DATE'], origin='1899-12-30')

# Generate the summary of a product name column
product_name_summary = transaction_data['PROD_NAME'].value_counts()
print(product_name_summary)

# Split product name into individual words
individual_words = transaction_data['PROD_NAME'].str.split(expand=True).stack().unique()

# Removing digits and special characters
individual_words = individual_words.str.replace(r'[^a-zA-Z]', '')

# Removing salsa products
transaction_data = transaction_data[~transaction_data['PROD_NAME'].str.contains('salsa', case=False)]

# Counting frequency for each word
word_frequency = individual_words.value_counts()
print(word_frequency)

# Check summary statistics and for null
print(transaction_data.describe())
print(transaction_data.isnull().sum())

# lnvestigate outliers - transaction with large quantity of chips
product_outliers = transaction_data[transaction_data['PROD_QTY'] == 200]

# Investigating other transaction by the same customer
customer_transaction = transaction_data[transaction_data['LYLTY_CARD_NBR'].isin(product_outlier['LYLTY_CARD_NBR'])]
print(customer_transaction)

# Filter customer based on the loyalty card number
transaction_data = transaction_data[transaction_data['LYLTY_CARD_NBR'] != outlier_customer_card]

# Re-examine transaction data
print(transaction_data.head())

# Count the number of transaction by date
transaction_grouped_by_date = transaction_data.groupby('DATE').size().reset_index(name='transaction_count')

# create dates sequence
date_range = pd.date_range(start='2018-07-01', end='2019-06-30')

# Merge it with transaction data to fill in the missing dates
transaction_grouped_by_date = pd.merge(date_range.to_frame(name='DATE'), transaction_grouped_by_date, on='DATE', how='left')

# Plot transaction over time
plt.plot(transaction_grouped_by_date['DATE'], transaction_grouped_by_date['transaction_count'])
plt.xlabel('Date')
plt.ylabel('Number of transaction')
plt.title('Transaction over time')
plt.xticks(rotation=90)
plt.show()
