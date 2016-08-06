from __future__ import print_function
import sys
from PIL import Image


# Rolling an image

def roll(image, delta):
    img = image.copy()
    xsize, ysize = img.size
    delta = delta % xsize
    if delta == 0: return image

    part1 = img.crop((0, 0, delta, ysize))
    part2 = img.crop((delta, 0, xsize, ysize))
    img.paste(part2, (0, 0, xsize - delta, ysize))
    img.paste(part1, (xsize - delta, 0, xsize, ysize))

    return img


for infile in sys.argv[1:]:
    img = Image.open(infile)
    new_img = roll(img, 20)
    new_img.save('test.jpg')
    new_img.show()
