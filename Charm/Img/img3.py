from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    print('f=', f, ',e=', e)
    outfile = f + '.bmp'
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print('Cannot convert', infile)
