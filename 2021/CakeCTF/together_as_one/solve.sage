from Crypto.Util.number import *

with open("output.txt") as f:
	buf = f.read().split("\n")

n = eval(buf[0].split()[2])
c = eval(buf[1].split()[2])
x = eval(buf[2].split()[2])
y = eval(buf[3].split()[2])
e = 0x10001

q = gcd(y - x, n)
print(q)

pr = n // q

r = gcd(y - x + q, pr)
print(r)

p = pr // r

phi = (p - 1) * (q - 1) * (r - 1)
d = inverse_mod(e, phi)

m = pow(c, d, n)
print(long_to_bytes(m))
