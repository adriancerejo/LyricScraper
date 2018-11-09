# google library to search songs
from googlesearch import search

# looks up song name on google
def google_search(look):
    for j in search(look, tld="co.in", num=1, stop=1, pause=2):
        print(j)


# song name to search
print("Enter song name: ")
query = input()
query += 'azlyrics'
google_search(query)


