#! python2
# lucky.py - Opens several Google search results.

import sys, pyperclip, requests, bs4, webbrowser

#get search terms from command line or clipboard (make sure are string)

if len(sys.argv) > 1:
    search = ' '.join(sys.argv[1:])
else:
    search = pyperclip.paste()

#download results page and pass to bs

#webbrowser.open('http://www.google.co.uk/search?q='+search)

resultsRes = requests.get('http://www.google.co.uk/search?q='+search)
resultsRes.raise_for_status()

resultsSoup = bs4.BeautifulSoup(resultsRes.text, 'lxml')

#identify results and open

links = resultsSoup.select('.r a')

print(str(links))

toOpen = min(5, len(links))

for link in links[:toOpen]:
    webbrowser.open('http://google.com' + link.get('href'))