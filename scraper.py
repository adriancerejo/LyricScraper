# google library to search songs
from googlesearch import search


# looks up song name on google
def google_search(look):
    for i in search(look, tld="com", num=1, stop=1, pause=2):

        # beautiful soup library to make html file readable
        from bs4 import BeautifulSoup

        # urllib lib to request document behind url
        from urllib.request import urlopen

        # "prettifies" it (makes it readable) and prints)
        # uses bs4 to open the url after urllib gets the doc
        soup = BeautifulSoup(urlopen(i), 'html.parser')
    # uses bs4 find all method to extract text from div containing lyrics
    div = soup.find_all("div", {"class": None})
    # converts div text to string and passes into remove_html_tags
    remove_html_tags(str(div))


def remove_html_tags(refine):
    # removes html tags from string using regex
    import re
    clean = re.compile('<.*?>')
    print(re.sub(clean, '', refine))


def youtube_link(ytfind):
    import webbrowser
    for i in search(ytfind, tld="com", num=1, stop=1, pause=2):
        webbrowser.open(i, new=2)


# song name to search and uses azlyrics.com (exclusively)
print("Enter song name and artist: ")
query = input()
queryhold = query + " audio music video"
query += ' azlyrics'
# pass into function to search up lyrics
print("Do you want to watch the music video?(y/n)")
video = input()

if video == 'n':
    google_search(query)
elif video == 'y':
    google_search(query)
    youtube_link(queryhold)
else:
    print("Error")
    exit()





