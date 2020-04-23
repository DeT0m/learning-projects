#!usr/bin/env python3

import os
from PIL import Image, ImageDraw, ImageFont

guestlist = 'guests.txt'  # Filename with guest names in each line
os.makedirs('guestcards', exist_ok=True)  # Creating directory for images

# Setting system font folder and font style
FONT_FOLDER = '/usr/share/fonts/truetype/'
lato_font = ImageFont.truetype(os.path.join(FONT_FOLDER,
                                            'lato/Lato-Regular.ttf'), 32)

BACKGROUND = 'flower.jpeg'  # file with background image (sized properly)

# Opening assets (background image, guest list)
im_background = Image.open(BACKGROUND)
file = open(guestlist)
lines = file.read().splitlines()

# Iterating over each name in guest list
for line in lines:
    print(f'Creating card for {line}.')
    im = Image.new('RGBA', (288, 360), 'white')  # Creating new image
    im.paste(im_background, (0, 0))  # Pasting background image
    imWidth, imHeight = im.size  # Defining size
    draw = ImageDraw.Draw(im)  # Creating draw object
    # Finding name text size
    textWidth, textHeight = draw.textsize(line,
                                          font=lato_font)
    # Finding middle position for this text size
    verticalMiddle = (imHeight / 2) - (textHeight / 2)
    horizontalMiddle = (imWidth / 2) - (textWidth / 2)
    # Drawing name exactly in the middle of the image
    draw.text((horizontalMiddle, verticalMiddle), line, fill=(39, 62, 112),
              font=lato_font)
    # Drawing black border on the edges
    draw.line([(0, 0), ((imWidth - 1), 0),
               ((imWidth - 1), (imHeight - 1)),
               (0, imHeight - 1), (0, 0)], fill='black')
    # Saving file
    im.save(os.path.join('guestcards/' + line + '.png'))
    print(f'Created card for {line}.')
