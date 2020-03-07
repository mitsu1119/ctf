import re

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

f = open("./chall.txt", "r")

line = f.readline()
flag = ""
while line:
    x = int(line.strip())
    flag = str(x & 1) + flag
    line = f.readline()

flag = int(flag, 2)
print(decodeM(flag))
f.close()
