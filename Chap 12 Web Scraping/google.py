#! python3
# google.py - Program to open several search results

import sys, webbrowser, bs4, requests

print('Searching....') #Print searching message while looking for query

res = requests.get('https://www.google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# Retrieve top search results

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Open browser tab for each result

linkElems = soup.select('a')

numOpen = min(5, len(linkElems))

for i in range(numOpen):
    urlToOpen = linkElems[i].get('href')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)
