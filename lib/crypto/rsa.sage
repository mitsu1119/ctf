from Crypto.Util.number import *

# -------------------------------- utils -------------------------------------------
def random_prime_bits(n, fac_dec=1):
    res = random_prime(2^n - 1, False, 2^(n - 1))
    while gcd(res - 1, fac_dec) != 1:
        res = random_prime(2^n - 1, False, 2^(n - 1))
    return res

# -------------------------------- base --------------------------------------------
def encrypt(m, e, p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = inverse_mod(e, phi)
    c = pow(m, e, n)
    return n, d, c

def decrypt(c, d, n):
    m = pow(c, d, n)
    return m

# -------------------------------- attack ------------------------------------------
def common_modulus_attack(n, e1, c1, e2, c2):
    _, x, y = xgcd(e1, e2)
    x = pow(c1, x, n)
    y = pow(c2, y, n)
    m = (x * y) % n
    return m

def common_private_exponent_attack(es, ns):
    M = round(sqrt(ns[-1]))
    B = matrix(ZZ, len(ns) + 1, len(ns) + 1, [[M, es[0], es[1], es[2]], [0, -ns[0], 0, 0], [0, 0, -ns[1], 0], [0, 0, 0, -ns[2]]])
    b = B.LLL()[0]
    d = round(abs(b[0]) / M)
    return d

# ------------------------------- check --------------------------------------------
# encryption and decryption
bits = 512
m = bytes_to_long(b"test_rsa")
e = 0x10001
p = random_prime_bits(bits)
q = random_prime_bits(bits)
n, d, c = encrypt(m, e, p, q)
print(long_to_bytes(decrypt(c, d, n)))

# common modulus attack
bits = 512
m = bytes_to_long(b"test_rsa")
e1 = 0x10001
e2 = 0x3
p = random_prime_bits(bits, e2)
q = random_prime_bits(bits, e2)
n, d, c1 = encrypt(m, e1, p, q)
n, d, c2 = encrypt(m, e2, p, q)
print(long_to_bytes(common_modulus_attack(n, e1, c1, e2, c2)))

# common private exponent attack
bits = 512
ms = [bytes_to_long(b"test_rsa"), bytes_to_long(b"test_rsa_2"), bytes_to_long(b"test_rsa_3")]
d = random_prime_bits(256)
ns = []
es = []
cs = []
for i in range(3):          # encrypt
    p = random_prime_bits(bits)
    q = random_prime_bits(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = inverse_mod(d, phi)
    ns.append(n)
    es.append(e)
    cs.append(pow(ms[i], e, n))
print(long_to_bytes(decrypt(cs[0], common_private_exponent_attack(es, ns), ns[0])))

