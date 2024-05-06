from flask import Flask, request, render_template
from pytube import YouTube
import os
import json
import math
import librosa
import numpy as np
import tensorflow.keras as keras
from collections import Counter

app = Flask(__name__)
DOWNLOAD_FOLDER = "../songs/downloads"
UPLOAD_FOLDER = "../songs/uploads"
JSON_FOLDER = "../songs/json"
MODEL_PATH = "../model/cnn_model8.h5"
SAMPLE_RATE = 22050
TRACK_DURATION = 575
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
NUM_SEGMENTS = 191
NUM_MFCC = 13
N_FFT = 2048
HOP_LENGTH = 512

# Function to create necessary folders if they don't exist
def create_folders():
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(JSON_FOLDER, exist_ok=True)

# Call create_folders() before using the folders
create_folders()

# Load the genre prediction model
model = keras.models.load_model(MODEL_PATH)
def save_mfcc(file_path, json_path, num_mfcc=NUM_MFCC, n_fft=N_FFT, hop_length=HOP_LENGTH, num_segments=NUM_SEGMENTS):
    data = {
        "mfcc": [],
        "labels": []
    }

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

    for d in range(num_segments):
        start = samples_per_segment * d
        finish = start + samples_per_segment

        mfcc = librosa.feature.mfcc(y=signal[start:finish], sr=sample_rate, n_mfcc=num_mfcc, n_fft=n_fft,
                                    hop_length=hop_length)
        mfcc = mfcc.T

        if len(mfcc) == num_mfcc_vectors_per_segment:
            data["mfcc"].append(mfcc.tolist())
            data["labels"].append(0)

    print("Number of segments processed:", len(data["mfcc"]))
    print("Shape of MFCCs:", len(data["mfcc"]), "segments, each with shape", len(data["mfcc"][0]), "MFCCs")

    # Ensure that the directory for saving JSON files exists
    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

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

def predict_genre(json_path):
    """Predicts the genre for a given JSON file containing MFCC data."""
    # Load the saved model
    model = load_model(MODEL_PATH)

    # Load test data from the JSON file
    X_test, y_test = load_data(json_path)

    # Predict using the loaded model
    predictions = predict(model, X_test)

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

    # Return percentages for each label meeting the threshold
    return percentages

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        clean_folder(DOWNLOAD_FOLDER)
        clean_folder(UPLOAD_FOLDER)
        clean_folder(JSON_FOLDER)
        # Get the YouTube video URL from the form
        video_url = request.form.get("video_url")

        # Create a YouTube object
        yt = YouTube(video_url)

        # Extract the title of the YouTube video
        video_title = yt.title

        # Extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # Download the file
        filename = video.download(output_path=DOWNLOAD_FOLDER)

        # Save the file as an mp3
        base, ext = os.path.splitext(filename)
        new_filename = base + '.mp3'
        os.rename(filename, new_filename)

        # Process the downloaded audio file
        process_audio(new_filename)

        # Move the processed file to the uploads folder
        processed_filename = os.path.basename(new_filename)
        processed_filepath = os.path.join(UPLOAD_FOLDER, processed_filename)
        os.rename(new_filename, processed_filepath)

        # Predict genre for the processed audio file
        json_filename = os.path.splitext(os.path.basename(processed_filepath))[0] + ".json"
        json_path = os.path.join(JSON_FOLDER, json_filename)
        genres = predict_genre(json_path)

        # Construct HTML response with predicted genres, song title, and file name
        genres_html = "<h2>Gatunki przewidywane przez model:</h2>"
        for genre, percentage in genres.items():
            genres_html += f"<p>{genre}: {percentage:.2f}%</p>"

        # Include the song title and file name in the HTML response
        return render_template("index.html", video_title=video_title, genres=genres)

    return render_template("index.html")

def process_audio(audio_file):
    # Generate the JSON file path
    json_filename = os.path.splitext(os.path.basename(audio_file))[0] + ".json"
    json_path = os.path.join(JSON_FOLDER, json_filename)
    
    # Process the file and save the MFCCs to JSON
    save_mfcc(audio_file, json_path, num_segments=NUM_SEGMENTS)

if __name__ == "__main__":
    app.run(debug=True)
