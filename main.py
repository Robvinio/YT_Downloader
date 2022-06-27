import os.path
from tkinter import *
from tkinter.messagebox import showerror, showinfo
from tkinter import filedialog
import os
import funkcje
from pytube import Playlist

def download():
    s=source.get()
    p=path.cget('text')
    if os.path.exists(p):
        try:
            funkcje.pob(s,p)
        except funkcje.NotYTVideoError:
            showerror('Błąd', 'Niepoprawny link')
        else:
            file_path = open('path.txt', 'w')
            file_path.write(p)
            file_path.close()
            showinfo('Pobrany','Plik został pobrany')
    else:
        showerror('Błąd', 'Nie ma takiej ścieżki')

def chose_path():
    p=filedialog.askdirectory()
    path.config(text=str(p))

okno=Tk()
okno.title('YT Dowloader')
okno.geometry('500x300')
Label(okno, text='Link do pobrania').grid(row=1, column=1)
Label(okno, text='Ścieżka zapisu').grid(row=1, column=2)
source=Entry(okno)
source.grid(row=2, column=1)
path=Label(okno, text=funkcje.starting_path())
ws=Button(okno,text='Zmień ścieżkę', command=chose_path).grid(row=3, column=2)
path.grid(row=2, column=2)
d=Button(okno, text='Pobierz', command=download).grid(row=3, column=1)
okno.mainloop()