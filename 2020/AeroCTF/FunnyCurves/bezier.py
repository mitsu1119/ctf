import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import base64
import bz2
import sys
from pwn import *

def ev(form, t):
    if form[0] == "{":
        return list(eval(form))[0]
    return eval(form)

def getimg(f):
    x = base64.b85decode(f)
    f = bz2.decompress(x)
    with open("form", "wb") as fi:
        fi.write(f)

    f = open("form", "r")
    buf = f.readline()  # t=>[0;1]

    x = []
    y = []
    buf = f.readline()
    idx = 0
    while buf:
        buf = buf[8:-2]
        buf = buf.replace("^", "**")
        buf = buf.split("; ")
        # print(buf)

        for i in range(1, 1001):
            t = 1 / i
            if idx == 0:
                x.append([ev(buf[0], t)])
                y.append([ev(buf[1], t)])
            else:
                x[i - 1].append(ev(buf[0], t))
                y[i - 1].append(ev(buf[1], t))
        buf = f.readline()
        idx += 1

    plt.tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False)
    plt.tick_params(bottom=False, left=False, right=False, top=False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.plot(x, y, color="black", linewidth=4)
    plt.savefig("fig.png")

    im = Image.open("fig.png")
    im_flip = ImageOps.flip(im)
    im_flip.save("fig.png")
    im_flip.close()
    im.close()

    plt.close()

    """
    import pyocr
    import pyocr.builders
    tools = pyocr.get_available_tools()
    tool = tools[0]
    langs = tool.get_available_languages()
    lang = langs[0]
    token = tool.image_to_string(Image.open("fig.png"), lang=lang, builder=pyocr.builders.TextBuilder())

    print(token)
    """

r = remote("tasks.aeroctf.com", 40001)
print(r.recv(0x100))
r.sendline("Y")
sleep(0.2)

idx = 1
while True:
    f = r.recvline()[:-1]
    r.recv(0x100)        # Result: 
    # print(f)
    getimg(f)
    log.info("idx = {}".format(idx))
    if idx == 100:
        break
    token = input("token: ")
    r.sendline(token)
    idx += 1

r.interactive()
# flag:Aero{e5767426d10e0f4bc4e131e0bb6d509ccad5a8decdf81a70b4f5ddb202441a09}
