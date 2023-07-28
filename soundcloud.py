import os
import youtube_dl

def download_soundcloud_track(url, output_directory):
    command = f'youtube-dl --extract-audio --audio-format mp3 -o "{output_directory}/%(title)s.%(ext)s" {url}'
    os.system(command)

if __name__ == "__main__":
    # URL of the Soundcloud track you want to download
    url = "https://soundcloud.com/user-705298452/future-x-lana-del-ray"

    # Output directory
    output_directory = "Audio"

    # Call the function to download the track
    try:
        download_soundcloud_track(url, output_directory)
    except:
        print('404 link is not working')
