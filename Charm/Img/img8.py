from __future__ import print_function
import sys
from PIL import Image

for infile in sys.argv[1:]:
    img = Image.open(infile)
    r, g, b = img.split()
    img = Image.merge('RGB', (b, g, r))
    img.save("test.jpg")
    img.show()
