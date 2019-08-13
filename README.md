# Lyrics Scraper

 Follow in-line comments for clarification

 ## Usage
 
 Run scraper.exe in the .\dist folder (only works on windows AFAIK).
 
 If you are not on windows, you will have to install the google, urllib, and bs4 libraries through the terminal and then run the scraper.pyw file using "python3 [path]\scraper.pyw"

 * This script uses the googlesearch module to look up the song and get the url
 * BeautifulSoup4 then makes the html file readable and urllib retrieves the actual html file to print out the lyrics
 * All lyrics are accessed through azlyrics.com
 * GUI made using tkinter
 
## Todo:
- [X] Add UI using a python library
- [X] Add youtube player inside application window (I tried to find ways to embed a yt player into tkinter however I could not find a way and so I resorted to simply opening the song in a browser window)
