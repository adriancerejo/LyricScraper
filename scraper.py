# google library to search songs
from googlesearch import search
# beautiful soup library to make html file readable
from bs4 import BeautifulSoup
# urllib lib to request document behind url
from urllib.request import urlopen


# looks up song name on google
def google_search(look):
    for j in search(look, tld="com", num=1, stop=1, pause=2):

        # "prettifies" it (makes it readable) and prints)
        # uses bs4 to open the url after urllib gets the doc
        soup = BeautifulSoup(urlopen(j), 'html.parser')
    # uses bs4 find all method to extract text from div containing lyrics
    div = soup.find_all("div", {"class": None})
    # converts div text to string and passes into remove_html_tags
    div = str(div)
    remove_html_tags(div)


def remove_html_tags(refine):
    # removes html tags from string using regex
    import re
    clean = re.compile('<.*?>')
    print(re.sub(clean, '', refine))


# song name to search and uses azlyrics.com (exclusively)
print("Enter song name and artist: ")
query = input()
query += ' azlyrics'
# pass into function to search up lyrics
google_search(query)








