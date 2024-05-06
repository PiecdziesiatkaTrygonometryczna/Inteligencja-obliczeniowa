import os
import shutil
from pydub import AudioSegment

def split_songs(folder):
    for filename in os.listdir(folder):
        if filename.endswith('.mp3') or filename.endswith('.wav'):
            song = AudioSegment.from_file(os.path.join(folder, filename))

            # Split the song into 30-second fragments
            fragments = []
            for i in range(0, len(song), 30000):  # 30 seconds = 30000 milliseconds
                fragment = song[i:i+30000]
                fragments.append(fragment)

            # If the last fragment is less than 25 seconds, take the last 30 seconds of the song
            if len(fragments) > 1 and len(fragments[-1]) < 25000:
                fragments[-1] = song[-30000:]

            # Create a new folder for the processed songs
            new_folder = os.path.join(folder + "31")
            os.makedirs(new_folder, exist_ok=True)

            # Save fragments in the new folder
            for i, fragment in enumerate(fragments):
                fragment.export(os.path.join(new_folder, f"{os.path.splitext(filename)[0]}_{i}.mp3"), format="mp3")

def main():
    current_dir = os.getcwd()
    for folder in os.listdir(current_dir):
        if os.path.isdir(folder):
            split_songs(folder)

if __name__ == "__main__":
    main()
