import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

## Use this to read data directly from github
df = pd.read_csv('https://gist.githubusercontent.com/Harsh-Git-Hub/2979ec48043928ad9033d8469928e751/raw/72de943e040b8bd0d087624b154d41b2ba9d9b60/retail_dataset.csv', sep=',')
## Use this to read data from the csv file on local system.
# df = pd.read_csv('./data/retail_data.csv', sep=',') 
## Print first 10 rows 
print(df.head(10))

items = set()
for col in df:
    items.update(df[col].unique())
# print(items)


# custom one hot encoding

itemset = set(items)
encoded_vals = []
for index, row in df.iterrows():
    rowset = set(row) 
    labels = {}
    uncommons = list(itemset - rowset)
    commons = list(itemset.intersection(rowset))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
encoded_vals[0]
ohe_df = pd.DataFrame(encoded_vals)

print(ohe_df.head(10))


# applying appriori
freq_items = apriori(ohe_df, min_support=0.2, use_colnames=True, verbose=1)
print(freq_items.head(7))