import webbrowser, sys, pyperclip

#webbrowser.open("www.google.com")
#sys.argv

if len(sys.argv) >1:
    address= ' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+address)
