from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import math
from fractions import Fraction
from pwn import *
from hashlib import sha256
import string

NB_ITERATIONS = 10871177237854734092489348927
e = 65538
N = 16725961734830292192130856503318846470372809633859943564170796604233648911148664645199314305393113642834320744397102098813353759076302959550707448148205851497665038807780166936471173111197092391395808381534728287101705

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

# Euler's totient function
def phi(n):
    if n == N:
        factors = [5, 23, 61, 701, 3401303653335128045797695889757092041482905417443555040334558532965054282731962107934457608241787496903277518095440908429024366794265591370988690049385889315571999029546461360356028016426404879577552560904181947]
    else:
        r = process(["msieve", "-v", "-e", "-q", str(n)])
        # print(r.recvuntil("p"))
        buf = r.recvall()[:-2].decode("utf-8")
        # print(buf)
        r.close()
        buf = buf.split()
        factors = []
        for i in range(len(buf) // 2):
            if buf[i * 2 + 1].isdecimal():
                factors.append(int(buf[i * 2 + 1]))
        factors = list(set(factors))

    # print("calc phi({})".format(n))
    # print("factors:", factors)

    res = Fraction(n, 1)
    for i in factors:
        pk = i
        res *= Fraction(pk - 1, pk)
    # print("phi = {}".format(int(res)))
    return int(res)

# a^(b^c) mod n
# gcd(a, n) = 1
def modpowpow(a, b, c, n):
    expmod = phi(n)
    exp = pow(b, c, expmod)
    return pow(a, exp, n)

def derive_key_easy(password):
    password = bytes_to_long(password)
    start = modpowpow(password, e, NB_ITERATIONS, N)
    print("step 1: start =", start)

    phiN = phi(N)

    # x = (e^NB_ITERATIONS - 1) mod phiN
    x = pow(e, NB_ITERATIONS, phiN)
    if x == 0:
        x = phiN
    x -= 1

    # exp = 1 + e + ... + e^(NB_ITERATIONS - 1) mod phiN
    exp = (x * modinv(e - 1, phiN)) % phiN

    key = pow(start, exp, N)
    print("step 2: key =", key)

    return sha256(long_to_bytes(key)).digest()

with open("flag.enc","rb") as f:
        m = f.read()

IV = b"random_and_safe!"
for i in string.printable:
    for j in string.printable:
        password = i + j
        print("password:", password)
        key = derive_key_easy(password.encode("utf-8"))
        cipher = AES.new(key, AES.MODE_CBC,IV)
        dec = cipher.decrypt(m)
        print("dec:", dec)

