
s = "th3 fl4g 1s n0t h3r3"
res = "0x"
for i in s:
    res += hex(ord(i))[2:]

print(res)

f = []
for i in s:
    f.append(hex(ord(i)))

ret = str(f).replace("'", "\"")
print(ret)
