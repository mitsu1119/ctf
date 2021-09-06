from Crypto.Util.number import long_to_bytes

with open("output.txt") as f:
	buf = f.read().split("\n")

p = eval(buf[0])
g = eval(buf[1])
cs = eval(buf[2])

m1 = ord("C")
m2 = ord("a")

_, s1, s2 = xgcd(m1, m2)
gr = (pow(cs[0], s1, p) * pow(cs[1], s2, p)) % p
print(gr)

m = ""
for c in cs:
	for i in range(1, 0xff):
		if c == pow(gr, i, p):
			m += chr(i)
			print(m)
			break
