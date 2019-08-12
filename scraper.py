import os
import search as song
import tkinter as tk
from tkinter import *
lyrics = ""
        
        
root = tk.Tk()
vscrollbar = tk.Scrollbar(root)

root.geometry("1200x800") # Width X Height

lblTitle = tk.Label(root, text='Lyrics Scraper')
lblTitle.place(x= 24, y=10)
lblTitle.config(font=('helvetica', 14))

lblSongName = tk.Label(root, text='Enter Song:')
lblSongName.place(x= 24, y=35)
lblSongName.config(font=('helvetica', 10))


txtSongName = tk.Entry (root) 
txtSongName.place(x=24, y=55)

# def getLyrics ():
    
#     x1 = entry1.get()
    
#     lyrics = song.searchSong.google_search(x1)
#     print(lyrics)
    
#     label4 = tk.Label(root, text= float(x1)**0.5,font=('helvetica', 10, 'bold'))
#     canvas1.create_window(200, 230, window=label4)

def getSong(songName):
    lyrics = song.searchSong.google_search(songName + " site:azlyrics.com")
    print(lyrics)
        
    canvas = Canvas(root, width=500, height=600, yscrollcommand=vscrollbar.set)

    vscrollbar.config(command=canvas.yview)
    vscrollbar.pack(side=tk.RIGHT, fill=tk.Y) 
    canvas.create_text(10, -45, anchor=NW, text=lyrics)
    canvas.place(relx=0.02, rely=.15)
    root.update()
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

