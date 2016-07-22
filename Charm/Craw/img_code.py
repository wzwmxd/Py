import pytesseract
from PIL import Image

image = Image.open('/home/kyo/C/Random_Img/8.jpg')
vcode = pytesseract.image_to_string(image)
print vcode
