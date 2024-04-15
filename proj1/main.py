import librosa
import matplotlib.pyplot as plt
import numpy as np

file = "riff.mp3"

signal, sr = librosa.load(file, sr=22050) # sr * T -> 22050 * 30


# librosa.display.waveshow(signal, sr=sr, color='b')
# plt.xlabel("czas")
# plt.ylabel("amplituda")
# plt.savefig("plot1.png")




# fft = np.fft.fft(signal)

# magnitude = np.abs(fft)
# frequency = np.linspace(0, sr, len(magnitude))

# left_frequency = frequency[:int(len(frequency)/2)]
# left_magnitude = magnitude[:int(len(frequency)/2)]
# plt.plot(left_frequency, left_magnitude)
# plt.xlabel("częstotliwość")
# plt.ylabel("magnituda")
# plt.savefig("plot2.png")




n_fft = 2048 # liczba sampli
hop_length = 512


stft = librosa.core.stft(signal, hop_length=hop_length, n_fft=n_fft)

spectogram = np.abs(stft)

log_spectogram = librosa.amplitude_to_db(spectogram)

librosa.display.specshow(log_spectogram, sr=sr, hop_length=hop_length)
plt.xlabel("czas")
plt.ylabel("częstotliwość")
plt.colorbar()
plt.savefig("plot3.png")