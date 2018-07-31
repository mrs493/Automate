import os, requests

os.makedirs('pokemon', exist_ok = True)

number = 1

#for number in range(1, 808):
for number in range(1, 152):
    try:
        imageRes = requests.get('https://www.serebii.net/art/th/' + str(number) +'.png')
        imageRes.raise_for_status()
        
        with open(os.path.join('pokemon', str(number).zfill(3) + '.png'), 'wb') as imageFile:
            for chunk in imageRes.iter_content(100000):
                imageFile.write(chunk)
        try:
            imageRes = requests.get('https://www.serebii.net/art/th/' + str(number) +'-m.png')
            imageRes.raise_for_status()
            with open(os.path.join('pokemon', str(number).zfill(3) + '-mega.png'), 'wb') as imageFile:
                for chunk in imageRes.iter_content(100000):
                    imageFile.write(chunk)
        except:
            pass
        try:
            imageRes = requests.get('https://www.serebii.net/art/th/' + str(number) +'-a.png')
            imageRes.raise_for_status()
            with open(os.path.join('pokemon', str(number).zfill(3) + '-alolan.png'), 'wb') as imageFile:
                for chunk in imageRes.iter_content(100000):
                    imageFile.write(chunk)
        except:
            pass
    except:
        print('image for number ' + str(number) + ' not found')