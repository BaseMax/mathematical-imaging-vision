# Max Base
# 2021-01-14
# https://github.com/BaseMax/mathematical-imaging-vision

from PIL import Image
from math import sqrt

# output color sets
colors = [
    # r,g,b
    (0,0,0),
    (250,250,250)
]

# find close color of a pixel
def close_color(pixel, colors):
    close = (0, 0, 0) # default color
    minDiff = 1000
    for color in colors:

        # color RGB
        r = color[0]
        g = color[1]
        b = color[2]

        # pixel RGB
        pr =pixel[0]
        pg = pixel[1]
        pb = pixel[2]

        # diff RGB
        dr = r - pr
        dg = g - pg
        db = b - pb

        # Why squrt? read: https://en.wikipedia.org/wiki/Color_difference
        sum = dr**2 + dg**2 + dg**2
        diff = sqrt(sum)
        if(diff < minDiff):
            minDiff = diff
            close = color

    return close

# read input image fle
image = Image.open("5.png")
width, height = image.size[0], image.size[1]
pixels = list(image.getdata())
image.close()

# modify/calc
for y in range(int(height)): # y
    for x in range(int(width)): #x
        i = x + y * width # ith pixel
        pixels[i] = close_color(pixels[i], colors)

# save output
output = Image.new("RGB", image.size)
output.putdata(pixels)
output.save("demo.png")
