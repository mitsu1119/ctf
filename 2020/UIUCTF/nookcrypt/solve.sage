from Crypto.Util.number import *

flag = (0xf31ce7cb1f2c6e7107318d76bdda50c5, 0x02d979fc3122bbaffcc1111953bc184f)

points = [
(0x77e035861860b2983de922db1bd78f97, 0xf9729a3afef0fd168948269fb696022c),
(0x4cf5afcc9bc1db0118172129b713d86a, 0xe41d8761370768aa9694b164c843dde9),
(0x5c0e90cf1b85ef039d00d4135ebafb96, 0xc2b44596292db4b088b85aed5c373a36),
(0x08679ea474860ad8e37bc7a89673028a, 0xc0d314f6dcbcda282d0113e9f5bf800c),
(0x07bc066ac9e9afb834673820f0b3dd0b, 0xd73c66a038cad6fc5916a48c8d93622c),
(0xb2ef02d32a36f5e9998fbe1698890cc2, 0x5c5f95fd18948f9e96127b21e78f827f),
(0xfa3312b976174edf358675a395fa303c, 0x3f4f5751db0520531fa27ef37bb9b098),
(0xf656c1dafef695dea1e67c7af0268acb, 0xcef1fbe4f0f29035929551131b88c077)
]

xs = []
ys = []
for i in points:
	xs.append(i[0])
	ys.append(i[1])

zs = []
for x, y in zip(xs, ys):
	zs.append(y ** 2 - x ** 3)

zps = []
for i in range(len(zs) - 1):
	zps.append(zs[i] - zs[i + 1])

Ts = []
for i in range(len(zps) - 1):
	Ts.append(zps[i] * (xs[i + 1] - xs[i + 2]) - zps[i + 1] * (xs[i] - xs[i + 1]))

p = gcd(Ts)
print("p: {}".format(hex(p)))

a = (zps[0] * inverse_mod(xs[0] - xs[1], p)) % p
print("a: {}".format(hex(a)))

b = (zs[0] - a * xs[0]) % p
print("b: {}".format(hex(b)))

F = GF(p)

for p in points:
	x = F(p[0])
	y = F(p[1])
	assert(y ** 2 == x ** 3 + a * x + b)

EC = EllipticCurve(F, [a, b])

# base point
g = (0x7b6aa5d85e572983e6fb32a7cdebc140, 0x27b6916a894d3aee7106fe805fc34b44)

flagp_s = [
(0x83a4f1cf0bc0a0702c5b145a1d87f7ad, 0x2b81add91aee8a3d4c0b5aeff9e2e91f),
(0x5826ee0cadd89342809e9899289e2293, 0xba746bd2a9fb7064dfad290428f8b4c1),
(0x65c27b7515bfcb99e2b3db84a9c4f06b, 0xe5f38190748b22fa5b5a5c4a70ae98c9)
]
hellop_s = [
(0x2b031af58bd0fca29347445ad100deac, 0x341f3fc18c76e37ba7c5bacbcda4926e),
(0xe2b7cbfc1998bed9cf9bfff9cfd8802b, 0x112558c42e14c26a65583fb951a2ec80),
(0x6a1c74b3dafbe1cc4df1cc5252d215e2, 0xa4c979fff57bbed0145414d708efc92b)
]

ak = []
pk = []
for flagp_, hellop_ in zip(flagp_s, hellop_s):
	T = []
	T.append(flagp_[1] ** 2 - flagp_[0] ** 3 - a * flagp_[0] - g[1] ** 2 + g[0] ** 3 + a * g[0])
	T.append(hellop_[1] ** 2 - hellop_[0] ** 3 - a * hellop_[0] - g[1] ** 2 + g[0] ** 3 + a * g[0])

	p_ = gcd(T)
	factors = factor(p_)
	print("p_: {} = {}".format(hex(p_), factors))

	b_ = (g[1] ** 2 - g[0] ** 3 - g[0] * a) % p_
	print("b_: {}".format(hex(b_)))

	print("")
	for fac, _ in factors:
		print("factor: {}".format(fac))
		E = EllipticCurve(Zmod(fac), [a, b_])
		P = E(g)
		ordg = P.order()
		print("	ordg: {}".format(ordg))
		Q = E(flagp_)
		m = discrete_log(Q, P, ordg, operation = "+")
		print("	m: {}".format(m))
		assert(m * P == Q)

		ak.append(m)
		pk.append(ordg)
	print("")

print("ak: {}".format(ak))
print("pk: {}".format(pk))
flag = crt(ak, pk)
print("flag: {}".format(flag))
print(long_to_bytes(flag))
