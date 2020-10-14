# This YT Video Downloader created by John07-noob
# Sep/5/2020

import pytube
from pytube import YouTube
path = (/home/john/Downloads)

print("Welcome to YT Video Downloader")          # Welcoming user
link = input("Insert Youtube links here: ")      # Ask usr youtube url
yt = YouTube(link)
print("The title: " + yt.title)                                       # Print Video title

ask = input("Which format you want to download? (video/audio): ")     # Ask usr video or audio
if ask == "video":
    res = input("What resolution you want? (720/360): ")              # Ask usr res 720p/360p
    if res == "720":                                   # if else statements, of course
        print("Downloading")
        stream = yt.streams.get_by_itag(22)            # Dwnlding using itag(22) 720p (set vars)
        stream.download(path)                                 # Code for download (vars.object)
        print("Done")
    elif res == "360":
        print("Downloading")
        stream = yt.streams.get_by_itag(18)            # Dwnlding using itag(18) 360p (set vars)
        stream.download(path)                                 # Code for download (vars.object)
        print("Done")
    else:
        print("Please insert the valid option.")

elif ask == "audio":
    print("Downloading")                               # NOTE: itag(140) == .mp4a extensions
    stream = yt.streams.get_by_itag(140)               # Dwnlding using itag(140) (set vars)
    stream.download(path)                                     # Code for download (vars.object)
    print("Done")
    
else:
    print("Please insert the valid option.")
