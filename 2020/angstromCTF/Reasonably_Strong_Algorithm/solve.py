from Crypto.PublicKey import RSA
import gmpy2
import re
import base64

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

def importPubKey(filename):
    with open(filename) as f:
        key = RSA.importKey(f.read())
    return key.n, key.e

def getBase64Cipher(string):
    c = base64.b64decode(string)
    return int.from_bytes(c, "big")

# factoring: msieve -q -v -e n
def pqAttack(p, q, e, c):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    return pow(c, d, n)

def lowExponentAttack(e, c):
    m, _ = gmpy2.iroot(c, e)
    return int(m)

def commonModulusAttack(n, e1, c1, e2, c2):
    _, x, y = egcd(e1, e2)
    x = pow(c1, x, n)
    y = pow(c2, y, n)
    return (x * y) % n

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

if __name__ == "__main__":
    n = 126390312099294739294606157407778835887
    e = 65537
    c = 13612260682947644362892911986815626931
    p = 9336949138571181619
    q = 13536574980062068373
    print(decodeM(pqAttack(p, q, e, c)))
