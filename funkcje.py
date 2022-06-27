"""
funkcje.py:
"""

from pytube import YouTube
import os
from urllib import request
from mutagen.id3 import ID3, APIC
from PIL import Image
from moviepy.audio.io.AudioFileClip import AudioFileClip


class NotYTVideoError(Exception):
    """Source is not YT video """
    pass

def pob(source, path):
    if (source.startswith('https://www.youtube.com/watch')==False):
        raise NotYTVideoError
    else:
        mf = YouTube(source)
        audio=mf.streams.get_audio_only().download(path)
        file=audio[:-4]+'.mp3'
        fmp3=AudioFileClip(audio)
        fmp3.write_audiofile(file)
        fmp3.close()
        os.remove(audio)
        url = mf.thumbnail_url
        im = request.urlretrieve(url, 'pic.jpg')
        cover=Image.open(im[0])
        cover.save(im[0])
        fa = ID3(file)
        fa.add(APIC(encoding=3, mime='image/jpeg', type=3, desc=u'Cover', data=open(im[0], 'rb').read()))
        fa.save(v2_version=3)
        os.remove(im[0])

def starting_path():
    if os.path.isfile('path.txt'):
        file_path=open('path.txt', 'r')
        p=file_path.read()
        file_path.close()
        return str(p)
    else:
        p=os.getcwd()
        file_path=open('path.txt', 'w')
        file_path.write(p)
        file_path.close()
        return str(p)


