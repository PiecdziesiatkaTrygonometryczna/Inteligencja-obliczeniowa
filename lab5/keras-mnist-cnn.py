import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History, ModelCheckpoint

# Load dataset
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Preprocess data
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
original_test_labels = np.argmax(test_labels, axis=1)  # Save original labels for confusion matrix

# Define model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


checkpoint = ModelCheckpoint("iris_model.keras", monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')



# Train model
history = History()
model.fit(train_images, train_labels, epochs=4000, batch_size=64, validation_split=0.2, callbacks=[history, checkpoint])

# Evaluate on test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

# Predict on test images
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Confusion matrix
cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig("1.png")

# Plotting training and validation accuracy
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

# Plotting training and validation loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

plt.tight_layout()
plt.savefig("2.png")

# Display 25 images from the test set with their predicted labels
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(predicted_labels[i])
plt.savefig("3.png")


#2

# a)  preprocesing to wstępna obróbka danych, aby elegancko pasowały one do naszego modelu
# reshape(28,28) zmienia wymiary obrazka na 28x28 pikseli
# to_categorical służy do kodowania danych, zazwyczaj powstaje tablica jednowymiarowa złożona z zer oraz jedynek
# np.argmax zwraca największą wartość w podanej tablicy (możemy podać w którym wymiarze, jeżeli nie podamy - spłaszczy tablicę)

# b) dane są wczytywane z bazy mnist (jest to baza zawierająca ręcznie pisane cyfry). potem dane są preprocesowane, tak jak opisano w poprzednim zadaniu

    # Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)), # wejście: obrazy wyjście: mapa danych
    # MaxPooling2D((2, 2)), # wejście: tak jak wyjście wyżej, wyjście: dane zdownsamplowane
    # Flatten(), # wejście: ^ , wyjście: spłaszczona tablica jednowymiarowa
    # Dense(64, activation='relu'), # wejście: ^ , wyjście: dane pomnożone przez funkcję aktywacji
    # Dense(10, activation='softmax') # wejście: ^, wyjście: finalne prawdopodobieństwo

# c ) błędów jest stosunkowo mało. Jak już się zdarzyły, to najwięcej pomylił dziewiątkę z siódemką (16 razy),
# dziewiątkę z czwórką (13 razy), ósemkę z siódemką, dwójkę z jedynką (po 10 razy) oraz piątkę z szóstką (11 razy).
# mimo że pomylił kilka razy dzieiwątkę, to 966 razy zgadł dobrze

# d ) raczej niedouczony, training loss jest stosunkowo duży, a validation loss prawie nie spada

# e ) należało dodać poniższą linijkę:
# checkpoint = ModelCheckpoint("iris_model.keras", monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
# oraz do linijki wywołującej trenowanie modelu, do argumentu callbacks dodać checkpoint:   callbacks=[history, checkpoint]