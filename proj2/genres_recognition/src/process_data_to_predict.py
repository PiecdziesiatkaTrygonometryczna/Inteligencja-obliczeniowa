import json
import math
import librosa
import os

TEST_FOLDER = "../data_to_predict/test"
TEST_JSON_FOLDER = "../data_to_predict/test_json"
SAMPLE_RATE = 22050
TRACK_DURATION = 575  # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION
NUM_SEGMENTS = 191


def save_mfcc(file_path, json_path, num_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
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

    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


def convert_to_mfccs():
    # Create the test_json folder if it doesn't exist
    os.makedirs(TEST_JSON_FOLDER, exist_ok=True)

    # Iterate over all files in the test folder
    for filename in os.listdir(TEST_FOLDER):
        file_path = os.path.join(TEST_FOLDER, filename)
        
        # Check if the file is a WAV or MP3 file
        if file_path.endswith(".wav") or file_path.endswith(".mp3"):
            # Generate the JSON file path
            json_filename = os.path.splitext(filename)[0] + ".json"
            json_path = os.path.join(TEST_JSON_FOLDER, json_filename)
            
            # Process the file and save the MFCCs to JSON
            save_mfcc(file_path, json_path, num_segments=NUM_SEGMENTS)

if __name__ == "__main__":
    convert_to_mfccs()
