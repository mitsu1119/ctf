from numpy import *
from PIL import Image

# a * x0 + b * y0 = gcd(a, b)
# return gcd(a,b), x0, y0
def egcd(a, b):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a // b, b, a % b)
        (x0, x1, y0, y1) = (x1, x0 - q * x1, y1, y0 - q * y1)
    return (a, x0, y0)

def modinv(a, mod):
    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception("Modinv does not exist")
    return x % mod

flag = Image.open(r"enc.png")
img = array(flag)

key = [41, 37, 23]
key = [23, 37, 41]

a, b, c = img.shape

for x in range (0, a):
    for y in range (0, b):
        pixel = img[x, y]
        for i in range(0,3):
            pixel[i] = (pixel[i] * modinv(key[i], 251)) % 251
        img[x][y] = pixel

enc = Image.fromarray(img)
enc.save('dec.png')
