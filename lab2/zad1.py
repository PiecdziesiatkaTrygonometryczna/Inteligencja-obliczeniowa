import pandas as pd


# A

missing_values = ["n/a", "na", "--", "-", "NA"]
df = pd.read_csv('iris_with_errors.csv', na_values = missing_values)

numeric_columns = ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


na_values_rows = df[df.isna().any(axis=1)]
not_positive_values_rows = df[(df._get_numeric_data() <= 0).any(axis=1)]
greater_than_15_rows = df[df['sepal.length'] > 15]

print(pd.concat([na_values_rows, not_positive_values_rows, greater_than_15_rows]))

# 8 rekordów jest błędnych

# B

medians = df[numeric_columns].median()

for col in numeric_columns:
    for index, value in df[col].items():
        if value < 0 or value > 15:
            df.at[index, col] = medians[col]

for col in numeric_columns:
    df[col].fillna(medians[col], inplace=True)







# C 


df['variety'] = df['variety'].str.replace('colour', 'color', regex=True).str.title()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print(df)