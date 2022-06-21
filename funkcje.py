"""
funkcje.py:
"""

from pytube import YouTube
import os

class NotYTVideoError(Exception):
    """Source is not YT video """
    pass

def pob(source, path):
    if (source.startswith('https://www.youtube.com/watch')==False):
        raise NotYTVideoError
    else:
        mf = YouTube(source)
        audio=mf.streams.filter(only_audio=True).first()
        out_file=audio.download(output_path=path)
        base, ext =os.path.splitext(out_file)
        file=base + '.mp3'
        os.rename(out_file, file)

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


