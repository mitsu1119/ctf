import sys

def _rot(i, c):
    if "A" <= c and c <= "Z":
        return chr((ord(c) - ord("A") + i) % 26 + ord("A"))
    if "a" <= c and c <= "z":
        return chr((ord(c) - ord("a") + i) % 26 + ord("a"))
    return c

def rot(i, s):
    g = (_rot(i, c) for c in s)
    return "".join(g)

s = sys.argv[1]
for i in range(26):
    print(rot(i, s))
