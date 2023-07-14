from spleeter.separator import Separator

def split_audio(input_path, output_path):
    # Create a separator with 2 stems (vocals and accompaniment)
    separator = Separator('spleeter:2stems')

    # Use the separator to separate the tracks
    separator.separate_to_file(input_path, output_path)

if __name__ == "__main__":
    # Define the path to the audio file
    input_path = "Clean-Audio/FTF.wav"
    # Define the output directory
    output_path = "Separated-Audio"

    # Call the function to split the audio file
    split_audio(input_path, output_path)
