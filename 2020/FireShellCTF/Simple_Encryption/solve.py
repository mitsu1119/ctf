import re

chs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[]^_`{|}~ '0123456789a"
ind = "3d3b39373533312f2d2b29272523211f1d1b19171513110f0d0b7d7b79777573716f6d6b69676563615f5d5b59575553514f4d4bbdb9b7b5b3afadaba9a7a5a3a18b89878583817f494543413f09070503ebbfb19f9d9b99979593918f8d"

ind = re.split('(..)', ind)[1::2]
ind = list(map(lambda ch: chr(int(ch, 16)), ind))

db = {}
for i in range(len(chs)):
    db[ind[i]] = chs[i]

with open("flag.enc", "rb") as f:
    buf = f.read()

flag = ""
for i in buf:
    flag += db[chr(i)]
    print(flag)

print(db)
print(flag)
