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