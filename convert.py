from pydub import AudioSegment
import os

def convert_mp3_to_wav(input_directory, output_directory):
    # Loop over every file in the input directory
    for filename in os.listdir(input_directory):
        # If the file is an .mp3 file
        if filename.endswith(".mp3"):
            # Construct the full input path
            input_path = os.path.join(input_directory, filename)

            # Load the mp3 file
            audio = AudioSegment.from_mp3(input_path)

            # Construct the output path, replacing .mp3 with .wav
            output_path = os.path.join(output_directory, filename.replace(".mp3", ".wav"))

            # Export the audio file as wav
            audio.export(output_path, format="wav")

if __name__ == "__main__":
    # Define the input directory
    input_directory = "Clean-Audio"

    # Define the output directory
    output_directory = "Split"

    # Call the function to convert all mp3 files
    convert_mp3_to_wav(input_directory, output_directory)
