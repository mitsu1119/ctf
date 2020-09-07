from pwn import *
import string
from Crypto.Util.number import *


target = "111100101101111011100110110100001101001011010110110100101101110011001110010110000100000011001110110100101110110011001010010000001101101011001010010000001110101011100100010000001100110011011000110000101100111"

test = b"1" * target.count("1") + b"0" * target.count("0")
print(target.count("1"))
print(target.count("0"))

r = remote("crypto.kosenctf.com", 13003)

r.sendline(b"\x02")

zeros = [1]
for i in range(2, target.count("0") + 2):
    zeros += [i ** 2]

ones = [2]
for i in range(2, target.count("1") + 2):
    ones += [2 * (i ** 2)]

solve = []
for i in target:
    if i == "1":
        solve += [ones[0]]
        ones = ones[1:]
    else:
        solve += [zeros[0]]
        zeros = zeros[1:]

r.sendline(str(solve).replace(" ", ""))

r.interactive()
# KosenCTF{yoshiking_is_clever_and_wild_god_of_crypt}
