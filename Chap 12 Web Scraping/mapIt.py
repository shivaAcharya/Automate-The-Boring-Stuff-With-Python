#! python3
# mapIt.py - Program to find places in google maps from command line argument or clipboard

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

webbrowser.open('www.google.com/maps/place/' + address)
