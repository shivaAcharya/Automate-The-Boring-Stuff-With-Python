#! python3
# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from pil import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'
path = 'D:\Learning\Automate the Boring Stuff with Python\Chap 19 Manipulating Images'
os.chdir(path)
print(os.getcwd())
logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#TODO: Loop over all files in the working directory
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue    # skip non-image files ad logo file itself

    im = Image.open(filename)
    width, height = im.size

    #TODO: Check if image needs to be resized.

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        #TODO: Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        #TODO: Resize the image.
        print('Resizing %s....' %filename)
        im = im.resize((width, height))

    #TODO: Add the logo.
    print('Adding logo to %s....' % filename)
    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    #TODO: Save changes.
    im.save(os.path.join('withlogo', filename))
    