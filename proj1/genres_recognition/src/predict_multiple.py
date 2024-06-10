import json
import numpy as np
import tensorflow.keras as keras
from collections import Counter
import os

# Path to the saved model
MODEL_PATH = "../models/cnn_model8.h5"
# Path to the folder containing the JSON files
JSON_FOLDER = "../data_to_predict/test_json"

def load_model(model_path):
    """Loads the saved model from file."""
    model = keras.models.load_model(model_path)
    print("Model loaded successfully!")
    return model

def load_data(data_path):
    """Loads dataset from json file."""
    with open(data_path, "r") as fp:
        data = json.load(fp)

    # Convert lists to numpy arrays
    X = np.array(data["mfcc"])
    y = np.array(data["labels"])

    return X, y

def predict(model, X):
    """Predicts class labels for input data using the trained model."""
    # Predict probabilities for each class
    predictions = model.predict(X)
    # Get the index of the class with the highest probability for each sample
    predicted_labels = np.argmax(predictions, axis=1)
    return predicted_labels

if __name__ == "__main__":
    # Load the saved model
    model = load_model(MODEL_PATH)

    # Iterate through each file in the JSON folder
    for filename in os.listdir(JSON_FOLDER):
        if filename.endswith(".json"):
            # Construct the full path to the JSON file
            json_file_path = os.path.join(JSON_FOLDER, filename)
            # Load test data from the JSON file
            X_test, y_test = load_data(json_file_path)
            # Predict using the loaded model
            predictions = predict(model, X_test)
            print(predictions)
            # Mapping of class indices to genre names
            mapping = [
                "electronic",
                "indie-rock",
                "rock",
                "jpop",
                "rap",
                "pop",
                "kpop",
                "pop-rock",
                "classical",
                "metal"
            ]

            # Count total number of predictions
            total_predictions = len(predictions)

            # Count occurrences of each predicted label
            occurrences = Counter(predictions)

            # Set the threshold for minimum percentage of occurrences
            threshold_percentage = 10

            # Calculate total occurrences for all digits meeting the threshold
            total = sum(count for digit, count in occurrences.items() if (count / total_predictions) * 100 >= threshold_percentage)

            # Calculate percentage for each digit meeting the threshold
            percentages = {mapping[digit]: (count / total) * 100 for digit, count in occurrences.items() if (count / total_predictions) * 100 >= threshold_percentage}

            # Print percentages for each label meeting the threshold
            print(f"Predictions for {filename}:")
            for genre, percentage in percentages.items():
                print(f"{genre}: {percentage:.2f}%")
