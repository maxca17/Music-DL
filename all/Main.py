import Splitter
import convert
from soundcloud import *
import soundcloud
y = "X"

    # Call the function to download the track
if y == 'X':
    print('Please paste a link')
    try:
        download_soundcloud_track(url, output_directory)
    except:
        print('404 link is not working or is invalid')
        

