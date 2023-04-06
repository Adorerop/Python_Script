import os
import sys
import pydub.AudioSegment

# Get command-line arguments
mp3_folder = sys.argv[1]
wav_folder = sys.argv[2]

# Ensure the output folder exists, create it if it does not
if not os.path.exists(wav_folder):
    os.makedirs(wav_folder)

# Loop through all MP3 files in the input folder
for filename in os.listdir(mp3_folder):
    if filename.endswith(".mp3"):
        # Load the MP3 file using Pydub
        mp3_path = os.path.join(mp3_folder, filename)
        sound = AudioSegment.from_mp3(mp3_path)

        # Create the output WAV file path
        wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + ".wav")

        # Export the file to WAV format using Pydub
        sound.export(wav_path, format="wav")

# Print a message to indicate the conversion has completed
print("MP3 files converted to WAV and saved in " + wav_folder)
