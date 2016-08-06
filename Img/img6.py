from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    try:
        im = Image.open(infile)
        print(infile, im.format, '%dx%d' % im.size, im.mode)
    except IOError:
        pass
box = im.copy()
box = (0, 0, 40, 20)
region = im.crop(box)
region = region.transpose(Image.ROTATE_180)
im.paste(region, box)
im.save('test.jpg')
im.show()
