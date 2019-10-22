flag = [0] * 32
x = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734292281, 1698182450, 1684289586]

for i in range(8):
    flag[i * 4] = x[i] >> 24
    flag[i * 4 + 1] = (x[i] >> 16) & 0xff
    flag[i * 4 + 2] = (x[i] >> 8) & 0xff
    flag[i * 4 + 3] = x[i] & 0xff

for i in flag:
    print(chr(i), end="")
