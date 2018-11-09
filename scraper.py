# google library to search songs
from googlesearch import search
# beautiful soup library to make html file readable
from bs4 import BeautifulSoup
# urllib lib to request document behind url
from urllib.request import urlopen


# looks up song name on google
def google_search(look):
    for j in search(look, tld="com", num=1, stop=1, pause=2):
        # stores url into variable
        url = j
        # uses bs4 to open the url after urllib gets the doc
        soup = BeautifulSoup(urlopen(j), 'html.parser')
        # "prettifies" it (makes it readable) and prints
        print(j)
        # removes html tags and elements
        for script in soup(["script", "style"]):
            script.extract()

        # get text
        text = soup.get_text()
        clean_text(text)


def clean_text(text):
    refined = str(text)
    print(refined.split())


# song name to search and uses azlyrics.com exclusively
print("Enter song name: ")
query = input()
query += 'azlyrics'
google_search(query)

