from __future__ import print_function
import sys, os
from PIL import Image
# import ImageEnhance, ImageFilter
import math


def cut(img, file_name, dir):
    w, h = img.size
    img_list = []
    for i in range(4):
        img_list.append(Image.new(img.mode, (w / 4, h)))
    image = img.copy()
    xsize, ysize = image.size
    w = xsize / 4
    for i in range(4):
        crop = img.crop((w * i, 0, (i + 1) * w, ysize))
        img_list[i].paste(crop, (0, 0, w, ysize))
    if not os.path.exists(dir + 'Cut/'):
        os.mkdir(dir + 'Cut/')
    for i, img in enumerate(img_list):
        img.save(dir + 'Cut/%s_%d.gif' % (file_name, i))


def image_filter(img):
    pix_data = img.load()
    image_size = img.size
    r_filter = 136
    g_filter = 136
    for y in xrange(image_size[1]):
        for x in xrange(image_size[0]):
            if pix_data[x, y][0] < r_filter:
                pix_data[x, y] = (0, 0, 0, 255)
    for y in xrange(image_size[1]):
        for x in xrange(image_size[0]):
            if pix_data[x, y][1] < g_filter:
                pix_data[x, y] = (0, 0, 0, 255)
    for y in xrange(image_size[1]):
        for x in xrange(image_size[0]):
            if pix_data[x, y][2] > 0:
                pix_data[x, y] = (255, 255, 255, 255)


def image_enhance(img):
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = image.convert('1')
    return img


def image_mean(img):
    pix_data = img.load()
    s = 0
    _y = 0
    _x = 0
    for y in xrange(img.size[0]):
        for x in xrange(img.size[1]):
            if pix_data[x, y]:
                _x += x
                _y += y
                s += 1
    return _x / float(s), _y / float(s)


def image_var(img):
    pix_data = img.load()
    s = 0
    mean_x, mean_y = image_mean(img)
    x2 = 0
    y2 = 0
    for y in xrange(img.size[0]):
        for x in xrange(img.size[1]):
            if pix_data[x, y]:
                x2 += (x - mean_x) ** 2
                y2 += (y - mean_y) ** 2
                s += 1
    return x2 / float(s), y2 / float(s)


def dist(x, y):
    return math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


image_path = '/home/kyo/Touro/Pictures/Random_Image/'
for i in range(130):
    image = Image.open(image_path + '%d.jpg' % i)
    image = image.convert('RGBA')
    image_filter(image)
    cut(image, '%d.jpg' % i, image_path)
    sys.stdout.flush()
    print("\rCutting image %d ..." % i, end='')
print('OK.')
'''
mean_list = []
var_list = []
count = 0
for i in range(10):
    for j in range(4):
        try:
            im = Image.open(image_path + 'tmp/%d_%d.gif' % (i, j))
            mean_list.append(image_mean(im))
            var_list.append(image_var(im))
            count += 1
        except:
            pass

for i in range(len(mean_list)):
    print(i, mean_list[i], var_list[i])
'''
