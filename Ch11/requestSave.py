import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
#get the data from the desired web page

try:
    res.raise_for_status()
    #checks that the webpage was accesed succesfully, otherwise raises an exception
    with open('RomeoAndJuliet.txt', 'wb') as playFile:
        #open a file to save contents, using wb (write binary mode) to maintain unicode encoding of text
        for chunk in res.iter_content(100000):
            #iterates over chunks of the data (100,000 bytes at a time in this case)
            #thus prevents using too much memory when downloading large pages
            playFile.write(chunk)        
except Exception as err:
    print('There was an error: ' + err)