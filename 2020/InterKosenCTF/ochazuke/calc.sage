from Crypto.Util.number import bytes_to_long
from binascii import unhexlify
from hashlib import sha1

EC = EllipticCurve(
    GF(0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff),
    [-3, 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b]
)
n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551 # EC.order()
Zn = Zmod(n)
G = EC((0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
        0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5))

msg = b"ohayougozaimasu"

print("ohayougozaimasu_hash")
r = ZZ(input("r: "))
s = ZZ(input("s: "))
h = Zn(ZZ(sha1(msg).hexdigest(), 16))

d = (bytes_to_long(msg) * (h * s - r) ** (-1)) % n

print("d: {}".format(d))
# d = 313681195146870630150443675574660225833


def sign(private_key, message):
    z = Zn(bytes_to_long(message))
    k = Zn(ZZ(sha1(message).hexdigest(), 16)) * private_key
    assert k != 0
    K = ZZ(k) * G
    r = Zn(K[0])
    assert r != 0
    s = (z + r * private_key) / k
    assert s != 0
    return (r, s)

target = b"ochazuke"
r, s = sign(d, target)
print()
print("ochazuke_signature")
print("r: {}".format(r))
print("s: {}".format(s))
