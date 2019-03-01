from PIL import Image
import argparse

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
im = Image.open('C:\\Users\\welink\\Pictures\\ascii_dora.png')
print(im.getpixel((0,1)))
print(im.getbands())
print(im.getbbox())
width = im.getbbox()[2]
height = im.getbbox()[3]
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1) / length
    return ascii_char[int(gray / unit)]

txt =''
for i in range(height):
    for j in range(width):
        txt +=get_char(*im.getpixel((j,i)))
    txt += '\n'

with open('ascii.txt','w') as f:
    f.write(txt)

import requests
from urllib import request
request.urlretrieve('https://m10.music.126.net/20190228152428/f6b7161c97c307aea2716dc73110c773/ymusic/0f0b/0609/015c/8a6a8ac59c1ce4f63e75668f4c3a16ca.mp3','1.mp3')