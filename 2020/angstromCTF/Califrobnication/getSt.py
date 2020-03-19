with open("c2", "rb") as f:
    buf = f.read()[len("Here's your encrypted flag: "):-1]
res = ""
for i in buf:
    res += chr(42 ^ i)
print(res)
