from __future__ import print_function
import os, sys
from PIL import Image

try:
    im = Image.open(r'E:\Pictures\icon.jpg')
    print(im.format, im.size, im.mode)
except IOError:
    print("Cannot open file!")
