# Program to walk tree directory

import os

for foldername, subfolders, filenames in os.walk(r'D:\Job Hunt'):
    print('The current folder is : ' + foldername)

    for subfolder in subfolders:
        print('The folder inside ' + foldername + ': ' + subfolder)

    for filename in filenames:
        print ('File inside ' + foldername + ': ' + filename)

    print('')
