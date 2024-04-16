import json
import numpy as np
import tensorflow.keras as keras
from collections import Counter

# Path to the saved model
MODEL_PATH = "model.h5"
# Path to the test data
TEST_DATA_PATH = "data_test.json"

def load_model(model_path):
    """Loads the saved model from file.

    :param model_path: Path to the saved model file
    :return model: Loaded model
    """
    model = keras.models.load_model(model_path)
    print("Model loaded successfully!")
    return model

def load_data(data_path):
    """Loads dataset from json file.

    :param data_path (str): Path to json file containing data
    :return X (ndarray): Inputs
    :return y (ndarray): Targets
    """
    with open(data_path, "r") as fp:
        data = json.load(fp)

    # Convert lists to numpy arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    print("Data successfully loaded!")
    return X, y

def predict(model, X):
    """Predicts class labels for input data using the trained model.

    :param model: Trained model
    :param X: Input data
    :return predictions: Predicted class labels
    """
    # Predict probabilities for each class
    predictions = model.predict(X)
    
    # Get the index of the class with the highest probability for each sample
    predicted_labels = np.argmax(predictions, axis=1)
    
    return predicted_labels

if __name__ == "__main__":
    # Load the saved model
    model = load_model(MODEL_PATH)

    # Load test data
    X_test, y_test = load_data(TEST_DATA_PATH)

    # Predict using the loaded model
    predictions = predict(model, X_test)



# Count total number of predictions
total_predictions = len(predictions)

# Count occurrences of each digit
occurrences = Counter(predictions)

# Set the threshold for minimum percentage of occurrences
threshold_percentage = 15

# Calculate total occurrences for all digits meeting the threshold
total = sum(count for digit, count in occurrences.items() if (count / total_predictions) * 100 >= threshold_percentage)

# Calculate percentage for each digit meeting the threshold
percentages = {digit: (count / total) * 100 for digit, count in occurrences.items() if (count / total_predictions) * 100 >= threshold_percentage}

# Print percentages for each digit meeting the threshold
for digit, percentage in percentages.items():
    print(f"Digit {digit}: {percentage:.2f}%")

