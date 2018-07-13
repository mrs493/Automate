import pyperclip

text = pyperclip.paste()
text = text.split('\n')

for line in range(len(text)):
    text[line] = '* ' + text[line]

text = '\n'.join(text)

pyperclip.copy(text)