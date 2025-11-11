# Ali Ghanbari
# Student Number: 4001239216

# Importing the required datasets
import numpy as np
import pandas as pd
from apyori import apriori

# Loading the dataset
store_data = pd.read_excel('Pandas Library\\Sales_info.xlsx', header=None)

# Having a glance at the records
# print(store_data)

# Look at the shape
# print(store_data.shape)

# Converting the pandas dataframe into a List of Lists
records = []
for i in range(0, 22):
    records.append([str(store_data.values[i, j]) for j in range(0, 6)])

# Build the Apriori model
association_rules = apriori(
    records, min_support=0.50, min_confidence=0.70, min_lift=1.2, min_length=2)
association_rules = list(association_rules)

# Glancing at the first rules
print(association_rules)
