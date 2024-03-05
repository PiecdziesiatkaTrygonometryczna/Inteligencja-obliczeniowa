import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder

iris = pd.read_csv("iris.csv")

label_encoder = LabelEncoder()
iris['variety_encoded'] = label_encoder.fit_transform(iris['variety'])

plt.scatter(iris["sepal.length"], iris["sepal.width"], c=iris["variety_encoded"])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Original")
plt.savefig('original.png') 

scaler = MinMaxScaler()
iris_normalized = scaler.fit_transform(iris[["sepal.length", "sepal.width"]])

plt.figure()
plt.scatter(iris_normalized[:, 0], iris_normalized[:, 1], c=iris["variety_encoded"])
plt.xlabel("Sepal Length (Normalized)")
plt.ylabel("Sepal Width (Normalized)")
plt.title("Normalized")
plt.savefig('normalized.png') 

scaler = StandardScaler()
iris_scaled = scaler.fit_transform(iris[["sepal.length", "sepal.width"]])

plt.figure()
plt.scatter(iris_scaled[:, 0], iris_scaled[:, 1], c=iris["variety_encoded"])
plt.xlabel("Sepal Length (Z-score)")
plt.ylabel("Sepal Width (Z-score)")
plt.title("Scaled")
plt.savefig('scaled.png') 
