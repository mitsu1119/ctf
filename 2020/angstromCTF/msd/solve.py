from PIL import Image
import re

im = Image.open("output.png")
im2 = Image.open("breathe.jpg")

width, height = im.size

flag = []
for j in range(height):
    for i in range(width):
        test = []
        r, g, b = im.getpixel((i, j))
        rp, gp, bp = im2.getpixel((i, j))

        if r == 255:
            flag.append("5")
        elif len(str(r)) == len(str(rp)):
            flag.append(list(str(r))[0])
        else:
            flag.append("0")

        if g == 255:
            flag.append("5")
        elif len(str(g)) == len(str(gp)):
            flag.append(list(str(g))[0])
        else:
            flag.append("0")

        if b == 255:
            flag.append("5")
        elif len(str(b)) == len(str(bp)):
            flag.append(list(str(b))[0])
        else:
            flag.append("0")

cnt = 0
res = []
flagp = []
b = 0
while cnt < len(flag) - 4:
    if flag[cnt] == "9" and flag[cnt+1] == "7" and flag[cnt+2] == "9" and flag[cnt+3] == "9":
        b = 1

    if flag[cnt] == "2" or flag[cnt] == "1":
        res.append(flag[cnt] + flag[cnt + 1] + flag[cnt + 2])
        if b == 1:
            flagp.append(flag[cnt])
            flagp.append(flag[cnt + 1])
            flagp.append(flag[cnt + 2])
        cnt += 2
    else:
        res.append(flag[cnt] + flag[cnt + 1])
        if b == 1:
            flagp.append(flag[cnt])
            flagp.append(flag[cnt + 1])
        cnt += 1

    cnt += 1

# print(flagp)

# print(data)
for i in res:
    print("{}".format(chr(int(i))), end="")

