from pwn import *
from fractions import Fraction

def getLSB(c):
    r = remote("18.179.178.246", 3001)
    r.sendline("2")
    r.sendline(hex(c)[2:])
    r.sendline("58cfe4f1")
    r.recvuntil("!= ")
    sig = int(r.recvline(), 16)
    print(hex(sig))
    r.close()
    return sig & 1

n = 0x6d70b5a586fcc4135f0c590e470c8d6758ce47ce88263ff4d4cf49163457c71e944e9da2b20c2ccb0936360f12c07df7e7e80cd1f38f2c449aad8adaa5c6e3d51f15878f456ceee4f61547302960d9d6a5bdfad136ed0eb7691358d36ae93aeb300c260e512faefe5cc0f41c546b959082b4714f05339621b225608da849c30f
e = 0x10001
c = 0x3cfa0e6ea76e899f86f9a8b50fd6e76731ca5528d59f074491ef7a6271513b2f202f4777f48a349944746e97b9e8a4521a52c86ef20e9ea354c0261ed7d73fc4ce5002c45e7b0481bb8cbe6ce1f9ef8228351dd7daa13ccc1e3febd11e8df1a99303fd2a2f789772f64cbdb847d6544393e53eee20f3076d6cdb484094ceb5c1

def lsbdec(c):
    bounds = [0, Fraction(n)]

    i = 0
    while True:
        print(i)
        i += 1

        c2 = (c * pow(2, e, n)) % n
        lsb = getLSB(c2)
        print("lsb = {}".format(lsb))
        if lsb == 1:
            bounds[0] = sum(bounds)/2
        else:
            bounds[1] = sum(bounds)/2
        diff = bounds[1] - bounds[0]
        diff = diff.numerator // diff.denominator
        if diff == 0:
            m = bounds[1].numerator // bounds[1].denominator
            return m
        c = c2

def decodeM(m):
    s = hex(m)[2:]
    l = []
    if (len(s) & 1):
        l.append(chr(int(s[0], 16)))
        s = s[1:]
    ss = re.split("(..)", s)[1::2]
    for i in ss:
        l.append(chr(int(i, 16)))
    return "".join(l)

print(len(bin(c)) - 2)
m = lsbdec(c)

print(decodeM(m))
# zer0pts{n3v3r_r3v34l_7h3_LSB}

