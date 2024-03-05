import pandas as pd

# Tworzenie DataFrame z pliku CSV
df = pd.read_csv('iris_with_errors.csv')

# Ustawienie opcji wyświetlania na wyświetlanie wszystkich wierszy i kolumn
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Wyświetlenie całego DataFrame
print(df)
