from z3 import *

f_1 = "atd4`qdedtUpetepqeUdaaeUeaqau"
f_2 = "c`b bk`kj`KbababcaKbacaKiacki"

f1 = []
f2 = []
for i in range(len(f_1)):
    f1.append(ord(f_1[i]))
    f2.append(ord(f_2[i]))

fs = [BitVec("f%d" % i, 8) for i in range(len(f1))]

s = Solver()
for i in range(len(f1)):
    s.add((fs[i] & 0x75) == f1[i])
    s.add((fs[i] & 0xeb) == f2[i])

s.check()
print(s.model())

m = s.model()
for i in range(len(f1)):
    print(chr(m[fs[i]].as_long()), end="")
