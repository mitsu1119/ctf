from Crypto.Util.number import *

c = 0x58566f59979e98e5f2f3ecea26cfb0319bc9186e206d6b33e933f3508e39e41bb771e4af053

def get_top(i):
	return int(("0" + bin(c)[2:])[i])

ss = b"CakeCTF{"
mm = int.from_bytes(ss, "little")

cs = []
cnt = 0
while mm:
	cc = get_top(cnt) ^^ (mm & 1)
	cs.append(cc)
	cnt += 1
	mm >>= 1

for rbits in reversed(range(63, 64)):
	csr = [1] + list(reversed(cs[:rbits]))
	for i in range(len(csr)):
		csr[i] = str(csr[i])
	r = int("".join(csr), 2)
	print(r)
	
	rs = []
	for i in range(300):
		rs.append(r & 1)
		b = (r & 1) ^^ ((r & 2) >> 1) ^^ ((r & 8) >> 3) ^^((r & 16) >> 4)
		r = (r >> 1) | (b << 63)

	print(rs)

	m = ""
	for i in range(len(bin(c)[2:])):
		m += str(get_top(i) ^^ rs[i])
	
	print("")
	print(long_to_bytes(int(m[::-1], 2))[::-1])

