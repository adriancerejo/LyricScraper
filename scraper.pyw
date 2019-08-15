# import search.py to use its methods
import search as songs
# import tkinter for the gui
import tkinter as tk
from tkinter import *

# create a global variable to store lyrics
lyrics = ""
song = songs.searchSong()
# create tkinter objects
root = tk.Tk()
root.title("Lyrics Scraper")

checked = tk.IntVar()

c = Checkbutton(root, text="Open Music?", variable=checked)
c.place(x= 50, y=55)
# set main window dimensions
root.geometry("600x800") # Width X Height

# create title label
lblTitle = tk.Label(root, text='Lyrics Scraper')
lblTitle.place(x= 175, y=10)
lblTitle.config(font=('helvetica', 14))

# create label
lblSongName = tk.Label(root, text='Enter Song:')
lblSongName.place(x= 175, y=35)
lblSongName.config(font=('helvetica', 10))

# create textbox
txtSongName = tk.Entry (root) 
txtSongName.place(x=175, y=55)


s = tk.Scrollbar(root)


def getSong():
    # get input from textbox
    songName = txtSongName.get()
    def MouseWheelHandler(event):
        count = 0

        def delta(event):
            if event.num == 5 or event.delta < 0:
                return -1 
            return 1 
        
        count += delta(event)
        if count == -1:
            canvas.yview_scroll(1, "units")
        elif count == 1:
            canvas.yview_scroll(-1, "units")

    root.bind("<MouseWheel>",MouseWheelHandler)
    root.bind("<Button-4>",MouseWheelHandler)
    root.bind("<Button-5>",MouseWheelHandler)
    # # function to allow user to scroll up
    # def on_mousewheelup(event):
    #     canvas.yview_scroll(-1, "units")
    # # function to allow user to scroll down
    # def on_mousewheeldown(event):
    #     canvas.yview_scroll(1, "units")

    # passes song name with additional string at end into google search method from search module
    lyrics = song.google_search(songName + " site:azlyrics.com")
    # create the canvas that will show the lyrics and position it
    canvas = Canvas(root, width=500, height=600, yscrollcommand=s.set)
    canvas.place(relx=0.13, rely=.15)
    canvas.create_text(10, 0, anchor=NW, text=lyrics)
    # listen for scrolls to move window up/down
    # canvas.bind_all("<Button-4>", on_mousewheelup)
    # canvas.bind_all("<Button-5>", on_mousewheeldown)
    # other scroll commands
    s.config(command=canvas.yview)
    s.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.config(scrollregion=canvas.bbox("all"))
    
    ytSearch = songName + " official music video"
    if checked.get() == 1:
        song.youtube_link(ytSearch)


# button to search the lyrics; will call requestSong function on click
btnSearch = tk.Button(text='Get Lyrics', command=getSong,  bg='brown', fg='white', font=('helvetica', 9, 'bold'))
btnSearch.place(x=175, y=85)

# REQUIRED for tkinter
root.mainloop()

