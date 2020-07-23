
with open("DifferenceTest.java", "rb") as f:
    dif = f.read()

with open("original.java", "rb") as f:
    orig = f.read()[:-1]

assert(len(dif) == len(orig))
l = len(dif)

errors = []
for i in range(l):
    if dif[i] != orig[i]:
        errors.append(dif[i] - orig[i])

print(errors)
for i in errors:
    print(chr(i), end="")
