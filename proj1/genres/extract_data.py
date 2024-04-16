import json
import math
import librosa

TEST_FILE_PATH = "test/test2.mp3"
JSON_PATH = "data_test.json"
SAMPLE_RATE = 22050
TRACK_DURATION = 575  # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION


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


if __name__ == "__main__":
    save_mfcc(TEST_FILE_PATH, JSON_PATH, num_segments=191)
