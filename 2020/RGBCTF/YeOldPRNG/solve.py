from pwn import *

base = 10

def sq(x, n):
    assert(n%2 == 0)
    xx = x**2
    mdig = n//2
    mid = str(xx).zfill(2*n)
    mid = mid[mdig: -mdig]
    return int(mid)

def MSM(seed, n):
    assert(n%2 == 0)
    x = seed
    return sq(x, n)

r = remote("challenge.rgbsec.xyz", 23456)
r.sendline("2")
for i in range(10):
    r.recvuntil("current")
    current = int(r.recvline().split()[2][:-1])
    log.info("current: {}".format(current))
    nex = MSM(current, 100)
    log.info("next: {}".format(nex))
    r.sendline(str(nex))

r.interactive()
