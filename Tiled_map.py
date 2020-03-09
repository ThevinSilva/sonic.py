'''
UPDATE 13 - 02 - 20

make a construct in photo shop import the image onto the game canvas then separate the image into smaller 64 x 64 tiles
with varying height information

'''

import csv, pygame, os
from PIL import Image

mask = set(pygame.mask.from_surface(pygame.image.load('test_low_poly.png')).outline())
print(sorted(mask))

def crop(input,height, width, page, area):
    im = Image.open(input)
    imwidth, imheight = im.size
    for i in range(0,imheight,height):
        for j in range(0,imwidth,width):
            box = (j,i,j+width, i+height)
            a = im.crop(box)

