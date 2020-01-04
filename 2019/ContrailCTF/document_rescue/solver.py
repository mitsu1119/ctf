import sys
from z3 import *
import subprocess

def mask(pad):
    if pad == 0:
        return 0xffffffff
    if pad == 1:
        return 0xffffff
    if pad == 2:
        return 0xffff
    if pad == 3:
        return 0xff

def revmask(pad):
    if pad == 0:
        return 0xffffffff
    if pad == 1:
        return 0xffffff00
    if pad == 2:
        return 0xffff0000
    if pad == 3:
        return 0xff000000

def sign(x):
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1

with open("flag.www", "rb") as f:
    data = bytearray(f.read())


data_len = len(data)
lcm = data_len // 4

m = pow(2, 32)
xs = [0] * lcm

for i in range(lcm):
    xs[i] = int.from_bytes(data[i * 4: i * 4 + 4], "big")

modi = b"%PDF-9.9"
padding = int(sys.argv[1])
EOF = int.from_bytes(b"%EOF", "big")

ps = [0] * lcm
ps[0] = int.from_bytes(modi[0:4], "big")
ps[1] = int.from_bytes(modi[4:8], "big")
ps[lcm - 2] = BitVec("pl_1", 64)
ps[lcm - 1] = BitVec("pl", 64)

aa = BitVec("a", 64)
bb = BitVec("b", 64)
s = Solver()
s.add(ps[lcm - 1] > 0)
s.add(ps[lcm - 1] < m)
s.add(aa > 0)
s.add(aa < m)
s.add(bb > 0)
s.add(bb < m)

s.add(((xs[lcm - 1] ^ ps[lcm - 1]) - (xs[1] ^ ps[1])) % m == (aa * (xs[lcm - 2] - xs[0])) % m)
s.add((revmask(padding) & ps[lcm - 1]) == ((EOF & mask(padding)) << (padding * 8)))

if padding !=  0:
    s.add(((~revmask(padding)) & ps[lcm - 2]) == ((EOF & (~mask(padding))) >> ((4 - padding) * 8)))
    s.add((ps[lcm - 2] & (0xff << (padding * 8))) == (0x25 << (padding * 8)))

s.add(xs[1] ^ ps[1] == (aa * xs[0] + bb) % m)
s.add(xs[lcm - 1] == (((aa * xs[lcm - 2] + bb) % m) ^ ps[lcm - 1]))
s.add(xs[lcm - 2] == (((aa * xs[lcm - 3] + bb) % m) ^ ps[lcm - 2]))

print(s.check())
while s.check() == sat:
    a = s.model()[aa].as_long()
    b = s.model()[bb].as_long()
    print("a = {}, b = {}".format(a, b))

    g = open("flag.dec", "wb")
    x = ps[0]
    g.write(x.to_bytes(4, "big"))

    for i in range(1, lcm):
        enc = (a * xs[i - 1] + b) % m
        x = xs[i] ^ enc
        g.write(x.to_bytes(4, "big"))
        
    g.close()

    try:
        out = subprocess.check_output("hexdump -C 'flag.dec' | grep '%%EOF'", shell=True)
        if len(out) > 0:
            print("Found!")
            exit(0)
    except subprocess.CalledProcessError:
        print("Not Found")

    s.add(Or(s.model()[aa] != aa, s.model()[bb] != bb))

