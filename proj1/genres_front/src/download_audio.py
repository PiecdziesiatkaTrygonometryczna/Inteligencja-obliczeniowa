# importing packages 
from pytube import YouTube 
import os 

# URL of the video to download
video_url = "https://youtu.be/cXGavNpV1FE"

# Create a YouTube object
yt = YouTube(video_url)

# Extract only audio 
video = yt.streams.filter(only_audio=True).first() 

# Destination to save the file (current directory)
destination = '.' 

# Download the file 
out_file = video.download(output_path=destination) 

# Save the file as an mp3
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 

# Print success message 
print(yt.title + " has been successfully downloaded.")
