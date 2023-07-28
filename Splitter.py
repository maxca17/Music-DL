from spleeter.separator import Separator
import os

def split_audio(input_directory, output_directory):
    # Create a separator with 2 stems (vocals and accompaniment)
    separator = Separator('spleeter:2stems')

    # Loop over every file in the input directory
    for filename in os.listdir(input_directory):
        # Construct the full input path
        input_path = os.path.join(input_directory, filename)
        # Use the separator to separate the track
        separator.separate_to_file(input_path, output_directory)

if __name__ == "__main__":
    # Define the input directory
    input_directory = "Clean-Audio"
    # Define the output directory
    output_directory = "Separated-Audio"

    # Call the function to split all audio files
    split_audio(input_directory, output_directory)
