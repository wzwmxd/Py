import pytesseract
from PIL import Image

# linux下的一个库，可以识别验证码
image = Image.open('/home/kyo/C/Random_Img/8.jpg')
vcode = pytesseract.image_to_string(image)
print vcode
