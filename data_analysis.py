#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

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
