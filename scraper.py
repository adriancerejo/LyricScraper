# import search.py to use its methods
import search as song
# import tkinter for the gui
import tkinter as tk
from tkinter import *

# create a global variable to store lyrics
lyrics = ""
      
# create tkinter objects
root = tk.Tk()
s = tk.Scrollbar(root)

# set main window dimensions
root.geometry("1200x800") # Width X Height

# create title label
lblTitle = tk.Label(root, text='Lyrics Scraper')
lblTitle.place(x= 24, y=10)
lblTitle.config(font=('helvetica', 14))

# create label
lblSongName = tk.Label(root, text='Enter Song:')
lblSongName.place(x= 24, y=35)
lblSongName.config(font=('helvetica', 10))

# create textbox
txtSongName = tk.Entry (root) 
txtSongName.place(x=24, y=55)


def getSong():
    # get input from textbox
    songName = txtSongName.get()

    # function to allow user to scroll up
    def on_mousewheelup(event):
        canvas.yview_scroll(-1, "units")
    # function to allow user to scroll down
    def on_mousewheeldown(event):
        canvas.yview_scroll(1, "units")

    # passes song name with additional string at end into google search method from search module
    lyrics = song.searchSong.google_search(songName + " site:azlyrics.com")
    # create the canvas that will show the lyrics and position it
    canvas = Canvas(root, width=500, height=600, yscrollcommand=s.set)
    canvas.place(relx=0.02, rely=.15)
    canvas.create_text(10, 0, anchor=NW, text=lyrics)
    # listen for scrolls to move window up/down
    canvas.bind_all("<Button-4>", on_mousewheelup)
    canvas.bind_all("<Button-5>", on_mousewheeldown)
    # other scroll commands
    s.config(command=canvas.yview)
    s.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(scrollregion=canvas.bbox("all"))
    
    # ytSearch = name + " official music video"
    # song.searchSong.youtube_link(ytSearch)


# button to search the lyrics; will call requestSong function on click
btnSearch = tk.Button(text='Get Lyrics', command=getSong,  bg='brown', fg='white', font=('helvetica', 9, 'bold'))
btnSearch.place(x=24, y=85)

# REQUIRED for tkinter
root.mainloop()

