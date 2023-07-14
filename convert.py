from pydub import AudioSegment

def convert_mp3_to_wav(mp3_path, wav_path):
    # Load the mp3 file
    audio = AudioSegment.from_mp3(mp3_path)
    
    # Export the audio file as wav
    audio.export(wav_path, format="wav")

# Define your mp3 file path
mp3_path = "Audio/FTF.mp3"

# Define your output wav file path
wav_path = "Clean-Audio/FTF.wav"

# Call the function to convert the file
convert_mp3_to_wav(mp3_path, wav_path)
