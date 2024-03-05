# uzyłem chatGPT 3.5

# jako prompt podałem data.csv, podałem treść polecenia, a dokładniej:

# Stwórz wykresy z irysami jako punktami na wykresie, dla dwóch zmiennych: sepal length i sepal width. Klasy irysów 
# oznaczone są w legendzie wykresu. Zrób wykres w trzech wersjach: dane oryginalne, znormalizowane min-max i 
# zeskalowane z-scorem.

# podany program uruchamiał się z błędami, więc podałem wynik z konsoli, chat zwrócił poprawiony program, który uruchamiał
# się z innymi błędami, więc powtarzałem tę sekwencję aż uzyskałem program pokazany poniżej, w 100% sprawny.


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load data
iris_df = pd.read_csv("iris.csv")

# Split into features and labels
X = iris_df[['sepal.length', 'sepal.width']]
y = iris_df['variety']

# Create three different versions of the data: original, min-max normalized, and z-score scaled
versions = {
    'Original': X.values,  # Convert DataFrame to NumPy array
    'Min-Max': MinMaxScaler().fit_transform(X),
    'Z-Score': StandardScaler().fit_transform(X)
}

# Create three plots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

for ax, (version, data) in zip(axs, versions.items()):
    # Split the data into individual iris classes
    for variety in y.unique():
        subset = data[y == variety]
        ax.scatter(subset[:, 0], subset[:, 1], label=variety)  # Directly access columns using integer indexing
    ax.set_title(f'Iris Data ({version})')
    ax.set_xlabel('Sepal Length')
    ax.set_ylabel('Sepal Width')
    ax.legend()

plt.savefig(f'iris_data_{version}.png')  # Save the plot as a PNG file

