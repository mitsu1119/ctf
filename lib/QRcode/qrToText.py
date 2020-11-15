from PIL import Image
import sys

image = Image.open(sys.argv[1])
image.convert("RGB")

imageSize = image.size
pixelSize = 1

white = 255 * 3
black = 0

rgbSum = []

for i in range(imageSize[0] // pixelSize):
    for j in range(imageSize[1] // pixelSize):
        r, g, b = image.getpixel((i * pixelSize, j * pixelSize))
        rgbSum.append(r + g + b)

with open("output", "w") as f:
    for x in range(imageSize[1] // pixelSize):
        for y in range(imageSize[0] // pixelSize):
            if rgbSum[(imageSize[0] // pixelSize) * y + x] == white:
                f.write("_")
            elif rgbSum[(imageSize[0] // pixelSize) * y + x] == black:
                f.write("#")
            else:
                f.write("?")
        f.write("\n")
