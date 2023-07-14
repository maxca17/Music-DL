import os

def download_soundcloud_track(url):
    command = f"youtube-dl --extract-audio --audio-format mp3 {url}"
    os.system(command)

if __name__ == "__main__":
    # URL of the Soundcloud track you want to download
    url = "https://soundcloud.com/liluzivert/lil-uzi-vert-flooded-the-face"

    # Call the function to download the track
    try:
        download_soundcloud_track(url)
    except:
        print('404 link is not working')
