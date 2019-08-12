# google library to search songs
from googlesearch import search
songLyrics = ''


class searchSong:
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
            return searchSong.remove_html_tags(str(div))
        except:
            songLyrics = "Error: Song Not Found \n(Check spelling/Enter Artist Name)"
            return songLyrics
    
    def remove_html_tags(refine):
        # removes html tags from string using regex
        import re
        clean = re.compile('<.*?>')
        lyrics = re.sub(clean, '', refine)
        lyrics = str(lyrics)
        lyrics = lyrics.replace('[', '')
        lyrics = lyrics.replace(']', '')
        lyrics = lyrics.replace(',', '', 1)
        songLyrics = lyrics
        return str(songLyrics)
        
    def youtube_link(ytfind):
        import webbrowser
        for i in search(ytfind, tld="ca", num=1, stop=1, pause=2):
            webbrowser.open(i, new=2)
