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

# split product name into individual words
individual_words = transaction_data['PROD_NAME'].str.split(expand=True).stack().unique()

# Removing digits and special characters
individual_words = individual_words.str.replace(r'[^a-zA-Z]', '')

# Removing salsa products
transaction_data = transaction_data[~transaction_data['PROD_NAME'].str.contains('salsa', case=False)]

# counting frequency for each word
word_frequency = individual_words.value_counts()
print(word_frequency)

#check summary statistics and for null
print(transaction_data.describe())
print(transaction_data.isnull().sum())

# investigate outliers - transaction with large quantity of chips
product_outliers = transaction_data[transaction_data['PROD_QTY'] == 200]

# investigating other transaction by the same customer
customer_transaction = transaction_data[transaction_data['LYLTY_CARD_NBR'].isin(product_outlier['LYLTY_CARD_NBR'])]
print(customer_transaction)


