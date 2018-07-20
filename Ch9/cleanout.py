import os

folder = 'C:\\Users\\Matt\\Desktop'

for folder, _, filenames in os.walk(folder):
    for filename in filenames:
        filesize = os.path.getsize(os.path.join(folder, filename))
        if filesize > 100e6:
            print(os.path.join(folder, filename) + ': ' + str(filesize))