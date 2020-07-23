from pwn import *
from PIL import Image
import zxing

r = remote("qr-generator.ctf.defenit.kr", 9000)

r.recvuntil("name? ")

name = "test"
r.sendline(name)

cnt = 0
reader = zxing.BarCodeReader()
while True:
    cnt += 1
    if cnt == 101:
        break

    try:
        r.recvuntil("< QR >")
        r.recvline()

        f = open("qr", "wb")
        length = 0
        while True:
            row = r.recvline()
            if len(row) <= 1:
                break

            row = b"".join(row.split())
            row = row.replace(b"1", b"X")
            row = row.replace(b"0", b"_")
            row = b"_"*5 + row + b"_"*5
            print(row)

            if length == 0:
                length = len(row)
                for i in range(5):
                    f.write(b"_" * length + b"\n")

            f.write(row + b"\n")

        for i in range(5):
            f.write(b"_" * length + b"\n")

        r.recvline()
        f.close()

        with open("qr") as f:
            buf = f.read().split()
        print(buf)

        img = Image.new("RGB", (length + 10, length + 10), (0xff, 0xff, 0xff))

        for y in range(length):
            for x in range(length):
                if buf[y][x] == "X":
                    img.putpixel((x + 5, y + 5), (0, 0, 0))
        img.save("qr.png")

        print("cnt:", cnt)
        dec = process(["convert", "-scale", "500%", "qr.png", "out.png"])
        sleep(0.3)
        dec.close()

        barcode = reader.decode("out.png")
        data = barcode.parsed
        print("data:", data)
        r.sendline(data)

        print("test:", r.recvline())
        sleep(0.3)
    except:
        break

r.interactive()

