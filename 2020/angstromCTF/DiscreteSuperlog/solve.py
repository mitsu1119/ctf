"""
*** This program uses the msieve for calc phi(n)
*** Before run thi program, wget the msieve-1.53

for x in range(10):
    print(x, a^^x % p)
"""

import math
from fractions import Fraction
from pwn import *

# Miller Rabin test
def isPrime(n):
    if n == 2:
        return True
    if n == 1:
        return False
    if n & 1 == 0:
        return False

    d = (n - 1) >> 1
    while d & 1 == 0:
        d //= 2

    for i in range(100):
        a = random.randint(1, n - 1)
        x = pow(a, d, n)
        t = d

        while t != n - 1 and x != 1 and x != n - 1:
            x = pow(x, 2, n)
            t *= 2

        if x != n - 1 and x & 1 == 0:
            return False
    return True

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
