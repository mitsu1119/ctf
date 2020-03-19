import sys
import re

BASE = 13
basechars = "angstromcXf20"
def getInd(ch):
    for i in range(len(basechars)):
        if basechars[i] == ch:
            return i
    print("getInd(ch) error")
    sys.exit(1)

def revBase(st):
    res = 0
    # print(st)
    for i in st:
        res *= BASE
        res += getInd(i)
    return res

def uloNot(x):
    return 0xffffffffffffffff - x

def uloMinus(x):
    return uloNot(x) + 1

def decodeM(m):
    s = hex(m)[2:]
    l = []
    if (len(s) & 1):
        l.append(chr(int(s[0], 16)))
        s = s[1:]
    ss = re.split("(..)", s)[1::2]
    for i in ss:
        l.append(chr(int(i, 16)))
    l.reverse()
    return "".join(l)

def solve(target):
    return revBase(target)

# n1
n1s = []
t = "artomtf2srn00tgm2f"
n1s.append(decodeM(solve(t)))
t = "artomtf2srn00Xgm2f"
n1s.append(decodeM(solve(t)))
t = "artomXf2srn00tgm2f"
n1s.append(decodeM(solve(t)))
t = "artomXf2srn00Xgm2f"
n1s.append(decodeM(solve(t)))
t = "arXomtf2srn00tgm2f"
n1s.append(decodeM(solve(t)))
t = "arXomtf2srn00Xgm2f"
n1s.append(decodeM(solve(t)))
t = "arXomXf2srn00tgm2f"
n1s.append(decodeM(solve(t)))
t = "arXomXf2srn00Xgm2f"
n1s.append(decodeM(solve(t)))
print("n1")
print(n1s)
print()

# n2
n2s = []
t = "ng0fa0mat0tmmmra0c"
n2s.append(decodeM(uloNot(solve(t))))
t = "ng0fa0mat0Xmmmra0c"
n2s.append(decodeM(uloNot(solve(t))))
t = "ng0fa0maX0tmmmra0c"
n2s.append(decodeM(uloNot(solve(t))))
t = "ng0fa0maX0Xmmmra0c"
n2s.append(decodeM(uloNot(solve(t))))
print("n2")
print(n2s)
print()

# n3
n3s = []
t = "ngnrmcornttnsmgcgr"
n3s.append(decodeM(uloMinus(solve(t) - 0x1337)))
t = "ngnrmcorntXnsmgcgr"
n3s.append(decodeM(uloMinus(solve(t) - 0x1337)))
t = "ngnrmcornXtnsmgcgr"
n3s.append(decodeM(uloMinus(solve(t) - 0x1337)))
t = "ngnrmcornXXnsmgcgr"
n3s.append(decodeM(uloMinus(solve(t) - 0x1337)))
print("n3")
print(n3s)
print()

# n4
n4s = []
t = "a0fn2rfa00tcgctaot"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00tcgctaoX"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00tcgcXaot"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00tcgcXaoX"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00Xcgctaot"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00XcgctaoX"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00XcgcXaot"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
t = "a0fn2rfa00XcgcXaoX"
n4s.append(decodeM((solve(t) + 0x4242) ^ 0x1234567890abcdef))
print("n4")
print(n4s)
print()

# n3,n4が奇数番目の文字、n1,n2が偶数番目の文字
#  n3n4
# n1n2  
#  r4_43twt __3trc1d
# getprn_1h4bt3_hl
# gre4t_p4r3nt_w1th_4_b3tt3r_ch1ld

