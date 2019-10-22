with open("rev_this", "r") as f:
    buf = f.read()

flag = [0] * len(buf)

counter = 0
for i in range(8):
    flag[i] = buf[i]

counter = 8
for i in range(counter, 0x17):
    if (i & 1) == 0:
        flag[i] = chr(ord(buf[i]) - 5)
    else:
        flag[i] = chr(ord(buf[i]) + 2)

flag[0x17] = buf[0x17]
print("".join(flag))
