import os
import search as song
import tkinter as tk
from tkinter import *


lyrics = ""
      
root = tk.Tk()
s = tk.Scrollbar(root)

root.geometry("1200x800") # Width X Height

canvas = Canvas(root, width=500, height=600, yscrollcommand=s.set)


lblTitle = tk.Label(root, text='Lyrics Scraper')
lblTitle.place(x= 24, y=10)
lblTitle.config(font=('helvetica', 14))

lblSongName = tk.Label(root, text='Enter Song:')
lblSongName.place(x= 24, y=35)
lblSongName.config(font=('helvetica', 10))


txtSongName = tk.Entry (root) 
txtSongName.place(x=24, y=55)

def on_mousewheelup(event):
    canvas.yview_scroll(-1, "units")

def on_mousewheeldown(event):
    canvas.yview_scroll(1, "units")
    
    
canvas.bind_all("<Button-5>", on_mousewheeldown)
canvas.bind_all("<Button-4>", on_mousewheelup)

def getSong(songName):

    lyrics = song.searchSong.google_search(songName + " site:azlyrics.com")
    s.config(command=canvas.yview)
    s.pack(side=tk.RIGHT, fill=tk.Y) 
    canvas.create_text(10, 10, anchor=NW, text=lyrics)
    canvas.place(relx=0.02, rely=.15)

    canvas.config(scrollregion=canvas.bbox("all"))
    
    # ytSearch = name + " official music video"
    # song.searchSong.youtube_link(ytSearch)

def requestSong():
    songName = txtSongName.get()
    getSong(songName)

    # canvas.create_text(10, 90, text='something')
    # canvas.focus_set()
    # canvas.pack(expand=YES, fill=BOTH)
    # root.mainloop()


btnSearch = tk.Button(text='Get Lyrics', command=requestSong,  bg='brown', fg='white', font=('helvetica', 9, 'bold'))
btnSearch.place(x=24, y=85)

root.mainloop()

