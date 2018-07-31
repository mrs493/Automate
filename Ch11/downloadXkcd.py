#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import os, requests, bs4

#make a folder to save comics in

os.makedirs('xkcd', exist_ok = True)

home = 'https://xkcd.com/'

url = home

i = 0

number = ''

print('Downloading comics...')

###
while not url.endswith('#'):
    
    comicRes = requests.get(url)
    comicRes.raise_for_status()
    
    comicSoup = bs4.BeautifulSoup(comicRes.text, 'lxml')
    comic = comicSoup.select('#comic img')
    
    previous = comicSoup.select('a[rel="prev"]')[0]
    
    if not number:
        number = str(int(previous.get('href')[1:-1])+1)
        digits = len(number)
                                   
    #if comic:
    try:
        comic = comic[0]
        #title = comic['alt']
        imageURL = 'https:' + comic['src']
        comicImgRes = requests.get(imageURL)
        comicImgRes.raise_for_status()
        #with open(os.path.join('xkcd', number + ' ' + title + '.png'), 'wb') as imageFile:
        with open(os.path.join('xkcd', number + '.png'), 'wb') as imageFile:
            for chunk in comicImgRes.iter_content(100000):
                imageFile.write(chunk)
    #else:
    except:
        print('could not find comic on page ' + url)
    
    number = previous.get('href')[1:-1].zfill(digits)
    
    url = home + previous.get('href')
    
print('Done')