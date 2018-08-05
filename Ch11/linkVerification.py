import requests, bs4

url = 'http://www.serebii.net'

pageRes = requests.get(url)
pageRes.raise_for_status()

pageSoup = bs4.BeautifulSoup(pageRes.text, 'html5lib')
links = pageSoup.select('a')

print(len(links))

tried = 0
fail = 0

for link in links:
    tried += 1
    if tried%20 == 0:
        print(tried)
    address = link['href']
    if address[0] == '/':
        address = url + address
    try:
        linkRes = requests.get(address)
        linkRes.raise_for_status()
    except:
        print('could not open page ' + address)
        fail += 1

print(fail + ' of ' + len(links) + ' failed to open')