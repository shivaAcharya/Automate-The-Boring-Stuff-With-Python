# Program to list and delete unneeded files
#! python3

import os

from pathlib import Path
folder = r'C:'
#folder = os.path.abspath(folder)
for foldername, subfolders, filenames in os.walk(folder):
    if os.path.getsize(foldername) > 10000000:
        print(f'The size of {foldername} is ' + str((os.path.getsize(foldername))/100000) + ' MB')
        print()
