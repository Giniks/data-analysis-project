#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import re
from spicy import stats

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

# Filter to December
december_data = transaction_data[(transaction_data['DATE'].dt.month == 12)]

# plotting transaction data by date in December
plt.plot(december_data['DATE'], december_data['transactio_counts'])
plt.xlabel('Date')
plt.ylabel('Number of transaction')
plt.title('Transactions in December')
plt.xticks(rotation=45)
plt.show()

# PlOtting histogeam of pack sizes
plt.hist(transactipn_data['PACK_SIZE'], bins=20)
plt.xlabel('Pack Size (g)')
plt.ylabel('Number of transactions')
plt.title('Distribution of pack size')
plt.show()

# Extracting Brand names from PROD_NAME
# Create Column for brand by extracting it from product name
transaction_data['BRAND'] = transactioon_data['PROD_NAME'].apply(lambda x: x.split()[0])

# Checking unique Brand names
unique_brands = transaction_data['BRAND'].unique()
print(unique_brands)

# Clean Brand names if necessary
transaction_data.lox[transaction_data['BRAND'] == 'RED', 'BRAND' ] = 'RRD'

# Check to ensure that the result is reasonable
unique_brands_cleaned = transaction_data['BEAND'].unique()
print(unique_brannds_cleaned)

# Get the basic summarries of customer dataset
customer_data_summary = customer_data_summary.describe()
print(customer_data_summary)

# Merge transaction data with customer data
merge_data = pd.merge(transaction_data, customer_data, how='left' on='LYLTY_CARD_NBR')

# Check for missing customer data
missing_cuatomer = merge_data[merge_data['LIFESTAGE'].isnull() | merge_data['PREMIUM_CUSTOMER'].isnull()]
print(missing_customer)

# Save dataset as CSV file
merged_data.to_csv('QVI_data.csv', index=False)

# Calculate Customer Summary number of LIFESTAGE AND PREMIMU_CUSTOMER
customer_summary = merged_data.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER']).size().reset_index(name='customer_counts')

# Plot the number of customer by LIFESTAGE and PREMIUM_CUSTOMER
plt.figure(figure=(10, 6))
sns.barplot(x='customer_counts', y='LIFESTAGE', hue='PREMIUM_CUSTOMER', data=customer_counts)
plt.title('Number of customers by LIFESTAGE and PREMIUM_CUSTOMER')
plt.xlabel('Number of Customer')
plt.ylabel('LIFESTAGE')
plt.legend(title='PREMIUM_CUSTOMER')
plt.show()

# Calculate average number of unit per customer by LIFESTAGE and PREMIUM_CUSTOMER

avg_units_per_customer = merge_data.groupby(['LIFESTAGE', 'PREMUIM_CUSTOMER'])['PROD_QTY'].mean().reset_index(name='avg_units_per_customer')

# plot the average number of units per customer by lifestage and premium customer.

plt.figure(10, 6)
sns.barplot(x='avg_units_per_customer', y='LIFESTAGE', hue='PREMIUM_CUSTOMER', data=avg_uniys_per_customer)
plt.title('Average Number of Units Per Customer')
plt.xlabel('avg_units_per_customer')
plt.ylabel('LIFESTAGE')
plt.legend(title='PREMIUM_CUSTOMED')
plt.show()

# Calculate and Plot average price per unit by LIFESTAGE and PREMIUM_CUSTOMER
avg_price_per_unit = merge_data.groupby(['LIFESTAGE', 'PREMUUM_CUSTOMER'])['TOT_SALES'].mean() / merge_data.groupby(['LIFESTAGE', 'PREMIUM_CUSTOMER'])['PROD_QTY'].mean()
avg_price_per_unit = avg_per_unit.reset_index(name='avg_price_per_unit')

plt.figure(10, 6)
sns.barplot(x='avg_price_per_unit', y='LIFESTAGE', hue='PREMIUM_CUSTOMER', data=avg_price_per_unit)
plt.title('Averagw Price Per Unit by LIFESTAGE and PREMIUM_CUSTOMER')
plt.xlabel('Average Price Per Unit')
plt.ylabel('LIFESTAGE')
plt.legend(title='PREMUIM_CUSTOMER')
plt.show()

# Perform an independent t-test between mainstream vs premium and budget midage and young singles and couples
mainstream_young = merged_data[(merged_data['PREMIUM_CUSTOMER'] == 'Mainstream') &
                               ((merged_data['LIFESTAGE'] == 'YOUNG SINGLES/COUPLES') |
                                (merged_data['LIFESTAGE'] == 'MIDAGE SINGLES/COUPLES'))]['TOT_SALES']

other_segments = merged_data[~((merged_data['PREMIUM_CUSTOMER'] == 'Mainstream') &
                               ((merged_data['LIFESTAGE'] == 'YOUNG SINGLES/COUPLES') |
                                (merged_data['LIFESTAGE'] == 'MIDAGE SINGLES/COUPLES')) )]['TOT_SALES']

t_stat, p_value = stats.ttest_ind(mainstream_young, other_segments)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Deep dive into Mainstream, young singles/couples
# Calculate the brand preferences for Mainstream, young singles/couples
mainstream_young_brands = merged_data[(merged_data['PREMIUM_CUSTOMER'] == 'Mainstream') &
                                      ((merged_data['LIFESTAGE'] == 'YOUNG SINGLES/COUPLES'))]['BRAND'].value_counts()

# Preferred pack size compared to the rest of the population
# Calculate the pack size preferences for Mainstream, young singles/couples
mainstream_young_pack_size = merged_data[(merged_data['PREMIUM_CUSTOMER'] == 'Mainstream') &
                                         ((merged_data['LIFESTAGE'] == 'YOUNG SINGLES/COUPLES'))]['PACK_SIZE'].value_counts()

# Plotting brand preferences
plt.figure(figsize=(10, 6))
mainstream_young_brands.plot(kind='bar')
plt.title('Brand Preferences of Mainstream, Young Singles/Couples')
plt.xlabel('Brand')
plt.ylabel('Number of Purchases')
plt.show()

# Plotting pack size preferences
plt.figure(figsize=(10, 6))
mainstream_young_pack_size.plot(kind='bar')
plt.title('Pack Size Preferences of Mainstream, Young Singles/Couples')
plt.xlabel('Pack Size')
plt.ylabel('Number of Purchases')
plt.show()


