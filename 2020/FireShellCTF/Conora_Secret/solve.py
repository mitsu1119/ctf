from Crypto.PublicKey import RSA
from functools import reduce
import math
import gmpy2
import re

# a * x0 + b * y0 = gcd(a, b)
# return gcd(a,b), x0, y0
def egcd(a, b):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while b != 0:
        (q, a, b) = (a // b, b, a % b)
        (x0, x1, y0, y1) = (x1, x0 - q * x1, y1, y0 - q * y1)
    return (a, x0, y0)

# a^(-1) % mod
def modinv(a, mod):
    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception("Modinv does not exist")
    return x % mod

# return x s.t.
# x = y[0] mod n[0]
# x = y[1] mod n[1]
# ...
def chinese_remainder(ns, ys):
    s = 0
    mulmul = reduce(lambda a, b: a * b, ns)
    for n, a in zip(ns, ys):
        p = mulmul // n
        s += a * modinv(p, n) * p
    return s % mulmul

# Baby step Giant step
# g^x = y mod p
def BsGs(g, y, p, q):
    m = int(math.sqrt(q) + 1)

    # Baby step
    baby = {}
    b = 1
    for i in range(m):
        baby[b] = i
        b = (b * g) % p

    # Giant step
    gm = pow(modinv(g, p), m, p)
    giant = y
    for i in range(m):
        if giant in baby:
            x = i * m + baby[giant]
            return x
        else:
            giant = (giant * gm) % p
    print("Error: BsGs")
    return -1

# Pohling-Hellman
def PH(p, g, y, phip_factors):
    bn = []
    for i in range(len(phip_factors) - 1):
        pk = phip_factors[i]
        phippk = (p - 1) // pk
        bk = BsGs(pow(g, phippk, p), pow(y, phippk, p), p, pk)
        bn.append(bk)

    # big factor
    bn.append(68891157682107548008597666707891616)

    print("bn: {}".format(bn))
    x = chinese_remainder(phip_factors, bn)
    return x

# decrypt
def decryption(c1, c2, x, p):
    m = ((c2 % p) * pow(c1, x * (p - 2), p)) % p
    return m

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

g = 271288297309032254959087925221099038857108692921
p = 1102599800392365312390928345103450099096472467311
h = 434975788934893935486812987784904932345816911149
c2 = 16411897893431398084407358496852070907176230853
c1 = 170780066307111969073123095839072967904862735531
bobc = 673443080181189918056298223003913178931188451777
phi_p = [2, 3, 5, 1093, 1223, 67103, 409739750867624373064553668058242381]
ell = 409739750867624373064553668058242381

"""
## from cado-nfs
## x value is incorporated in Pohlig-Hellman
log_h = 89312554803004771914370169287990323
log_g = 49442345370660375073521009173730491
x = log_h * modinv(log_g, ell) % ell
x = 68891157682107548008597666707891616
"""

x = PH(p, g, h, phi_p)
print("x: {}".format(x))
m = decryption(c1, c2, x, p)
print(m)
print(decodeM(m))

m = decryption(c1, bobc, x, p)
print(m)
print(decodeM(m))

