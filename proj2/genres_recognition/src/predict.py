import json
import numpy as np
import os
from tensorflow.keras.models import load_model

MODEL_PATH = "../models/rnn_model5.h5"
SONG_FOLDER_PATH = "../data_to_predict/test_json"
GENRE_LABELS = [
    "alternatywna",
    "elektroniczna",
    "klasyczna",
    "metal",
    "pop",
    "rap",
    "rock"
]

def load_song_data(song_path):
    """Loads song data from a json file.

    :param song_path (str): Path to json file containing song data
    :return song_data (ndarray): Processed song data
    """
    with open(song_path, "r") as fp:
        song_data = json.load(fp)
    

    song_data = np.array(song_data["mfcc"])
    # Add batch dimension if necessary
    if song_data.ndim == 2:
        song_data = np.expand_dims(song_data, axis=0)
    
    return song_data

def predict_genre(model, song_data):
    """Predicts the genre of the song using the trained model.

    :param model: Trained Keras model
    :param song_data (ndarray): Preprocessed song data
    :return predicted_genre (str): Predicted genre name
    """
    predictions = model.predict(song_data)
    predicted_label = np.argmax(predictions, axis=1)
    predicted_genre = GENRE_LABELS[predicted_label[0]]
    return predicted_genre


model = load_model(MODEL_PATH)


for filename in os.listdir(SONG_FOLDER_PATH):
    if filename.endswith(".json"):
        song_path = os.path.join(SONG_FOLDER_PATH, filename)
        

        song_data = load_song_data(song_path)
        

        predicted_genre = predict_genre(model, song_data)
        print(f'{filename}: Predicted genre: {predicted_genre}')
