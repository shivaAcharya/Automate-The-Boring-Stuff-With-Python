# Program to Save Webpage Files to the Hard Drive

import requests

res = requests.get('https://en.wikipedia.org/wiki/List_of_HTTP_status_codes')
res.raise_for_status()

Book = open('Beyond the Basic Stuff with Python', 'wb')

for chunks in res.iter_content(100000):
    Book.write(chunks)

Book.close()
