# google library to search songs
from googlesearch import search
import os

# looks up song name on google
def google_search(look):
    try:
        for i in search(look, tld="ca", num=1, stop=1, pause=2):

            # beautiful soup library to make html file readable
            from bs4 import BeautifulSoup

            # urllib lib to request document behind url
            from urllib.request import urlopen

            # "prettifies" it (makes it readable) and prints
            # uses bs4 to open the url after urllib gets the doc
            soup = BeautifulSoup(urlopen(i), 'html.parser')
        # uses bs4 find all method to extract text from div containing lyrics
        div = soup.find_all("div", {"class": None})
        # converts div text to string and passes into remove_html_tags
        remove_html_tags(str(div))
    except:
        print("song not found")

def remove_html_tags(refine):
    # removes html tags from string using regex
    import re
    clean = re.compile('<.*?>')
    print(re.sub(clean, '', refine))


def youtube_link(ytfind):
    import webbrowser
    for i in search(ytfind, tld="ca", num=1, stop=1, pause=2):
        webbrowser.open(i, new=2)


def requestSong():
    # song name to search and uses azlyrics.com (exclusively)
    print("Enter song name and artist: ")
    name = input()
    ytSearch = name + " audio music video"
    name += " site:azlyrics.com"
    # pass into function to search up lyrics
    print("Do you want to listen to the song?(y/n)")
    video = input()

    if video == 'n':
        google_search(name)
    elif video == 'y':
        google_search(name)
        youtube_link(ytSearch)


while 1:
    cont = input("To use type 's' and to exit hit enter.\n")
    if cont == 's':
        os.system('clear')
        os.system('cls')
        requestSong()
    else:
        os.system('clear')
        os.system('cls')
        break
