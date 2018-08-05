import os, requests, bs4

search = 'watercolour'
get = 10

os.makedirs(os.path.join('imgur', search), exist_ok = True)

resultsRes = requests.get('https://imgur.com/search?q=' + search)
resultsRes.raise_for_status()

resultsSoup = bs4.BeautifulSoup(resultsRes.text, 'html5lib')

results = resultsSoup.select('.cards img')

#no = min(get, len(results))

no = len(results)
dig = len(str(no))

print(no)

for i in range(no):
    imageRes = requests.get('http:' + results[i]['src'])
    imageRes.raise_for_status()
    
    with open(os.path.join('imgur', search, 'result_' + str(i+1).zfill(dig) + '.jpg'), 'wb') as imageFile:
        for chunk in imageRes.iter_content(10000):
            imageFile.write(chunk)
    
    