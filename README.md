# Lyrics Scraper

 Follow in-line comments for clarification

 ## Usage
 
 Run scraper.exe in the output folder (only works on windows).
 
 If you are not on windows, you will have to install the google, urllib, and bs4 libraries through the terminal and then run the scraper.py file using "python3 [path]\scraper.py"

 * This script uses the googlesearch module to look up the song and get the url
 * BeautifulSoup4 then makes the html file readable and urllib retrieves the actual html file to print out the lyrics
 * All lyrics are accessed through azlyrics.com
 
## Todo:
- [X] Add UI using a python library
- [X] Add youtube player inside application window (I tried to find ways to embed a yt player into tkinter however I could not find a way and so I resorted to simply opening the song in a browser window)
- [ ] Customize the width/height of the browser window if possible 
