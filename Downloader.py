from pytube import YouTube, Playlist
from pyperclip import paste
from pathlib import Path
import os
path = str(Path.home() / "Music")
def download(yt:YouTube, type:str, path:str):
    print(yt.title)
    if type == "V": yt.streams.get_highest_resolution().download(path)
    elif type == "A": 
        audio = yt.streams.get_audio_only().download(path)
        base, ext = os.path.splitext(audio)
        audioN = base + ".mp3"
        if os.path.exists(audioN): os.remove(audioN)
        os.rename(audio, audioN)
def getYT(type:str, link:str):
    try: download(YouTube(link), type, path)
    except:
        try:
            pl = Playlist(link)
            for i in pl.video_urls: download(YouTube(i), type, path + pl.title)
        except Exception as e: print(e)
getYT(input("V/A:").upper(), paste())
