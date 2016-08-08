from __future__ import print_function
import sys, os
from PIL import Image

img = Image.open(r'random_img/tmp/1_0.gif')
pix = img.load()
#for x in xrange(img.size[0]):
#    for y in range(img.size[1]):
# print(pix[x, y])
print(pix[0, 0])
