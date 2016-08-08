import Image, ImageDraw, ImageFont
import random
import math

width = 100
height = 40
bg_color = (255, 255, 255)
image = Image.new('RGB', (width, height), bg_color)
font = ImageFont.truetype(r'cour.ttf', 30)
font_color = (0, 0, 0)
draw = ImageDraw.Draw(image)
draw.text((0, 0), '1234', font=font, fill=font_color)
del draw
image.save('1234_1.jpg')
new_image = Image.new('RGB', (width, height), bg_color)
new_pix = new_image.load()
pix = image.load()
offset = 0
for y in range(0, height):
    offset += 1
    for x in range(0, width):
        new_x = x + offset
        if new_x < width:
            new_pix[new_x, y] = pix[x, y]
new_image.save('1234_2.jpg')
new_image = image.transform((width + 30, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0))
new_image.save('1234_3.jpg')
draw = ImageDraw.Draw(new_image)
line_color = (0, 0, 0)
for i in range(0, 15):
    x1 = random.randint(0, width)
    x2 = random.randint(0, width)
    y1 = random.randint(0, height)
    y2 = random.randint(0, height)
    draw.line([(x1, y1), (x2, y2)], line_color)
new_image.save('1234_4.jpg')

new_image.show()
