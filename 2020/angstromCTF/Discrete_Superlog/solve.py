"""
*** This program uses the msieve for calc phi(n)
*** Before run thi program, wget the msieve-1.53

for x in range(10):
    print(x, a^^x % p)
"""

import math
from fractions import Fraction
from pwn import *

# Euler's totient function
def phi(n):
    r = process(["./msieve-1.53/msieve", "-v", "-e", "-q", str(n)])
    print(r.recvuntil("p"))
    buf = r.recvall()[:-2].decode("utf-8")
    print(buf)
    r.close()
    buf = buf.split()
    factors = []
    for i in range(len(buf) // 2):
        if buf[i * 2 + 1].isdecimal():
            factors.append(int(buf[i * 2 + 1]))
    factors = list(set(factors))

    print("calc phi({})".format(n))
    print("factors:", factors)

    res = Fraction(n, 1)
    for i in factors:
        pk = i
        res *= Fraction(pk - 1, pk)
    print("phi = {}".format(int(res)))
    return int(res)

# modtetration
# a ^^ b mod c
def tetration(a, b, c):
    if c == 1:
        return 0
    if a == 1:
        return 1

    if b == 0:
        return 1
    if b == 1:
        return a % c
    g = math.gcd(pow(a, int(math.log2(c)), c), c)
    pg = phi(c // g)

    if g == c:
        return 0

    res = pow(a, tetration(a, b - 1, pg) + pg, c)
    return res

p = int(input())
a = int(input())

buf = []
for i in range(1, 11):
    buf.append(tetration(a, i, p))

for i in range(len(buf)):
    print(i + 1, buf[i])
