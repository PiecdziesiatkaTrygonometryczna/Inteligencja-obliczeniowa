import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
encoder = OneHotEncoder()
y_encoded = to_categorical(y)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=42)

# Define the model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(64, activation='relu'),
    Dense(y_encoded.shape[1], activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model with batch size equal to 4
history_batch4 = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=4)

# Train the model with batch size equal to 8
history_batch8 = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=8)

# Train the model with batch size equal to 16
history_batch16 = model.fit(X_train, y_train, epochs=100, validation_split=0.2, batch_size=16)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# Plot the learning curves for different batch sizes
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(history_batch4.history['accuracy'], label='batch size = 4')
plt.plot(history_batch8.history['accuracy'], label='batch size = 8')
plt.plot(history_batch16.history['accuracy'], label='batch size = 16')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history_batch4.history['loss'], label='batch size = 4')
plt.plot(history_batch8.history['loss'], label='batch size = 8')
plt.plot(history_batch16.history['loss'], label='batch size = 16')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.tight_layout()

plt.savefig("accuracy_plot.png")

# Save the model
model.save('iris_model.keras')

# Plot and save the model architecture
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)

# Zad 1
# a) Skaluje dane. A konkretniej, za pomocą takiego wzoru:     z = (x - u) / s   
#   Dana x jest skalowana do danej z, gdzie u to średnia zbioru treningowego, a s to odchylenie standardowe

# b) koduje klasy do tablic złożonych z samych zer i jedynek

# c) warstwa wejściowa ma tyle neuronów, ile wartości mają dane wejściowe. 
# warstwa wyjściowa ma tyle neuronów, ile klas model ma przewidzieć
# X_train.shape[1] to liczba neuronów w warstwie wejściowej
#  y_encoded.shape[1] to liczba neuronów w warstwie wyjściowej

# d) dla 100 epok:
# - sigmoid: 95,56%
# - relu: 100%

# e) adam, categorical_crossentropy, accuracy 100%
# sgd, mean_squared_error, Precision() 100%
# rmsprop, binary_crossentropy, Recall() 97,78%

# f) odpowiedz na wykresie accuracy_plotF.png

# g) po okolo 20 epokach sieć ma njalpeszą wydajność

# h) wczytuje zbiór danych, przygotowuje go, dotrenowuje wcześniej
# wytrenowany model, zapisuje go i wyświetla jego dokładność

# model = Sequential([
#     Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
#     Dense(64, activation='relu'),
#     Dense(y_encoded.shape[1], activation='softmax')
# ])

# model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])