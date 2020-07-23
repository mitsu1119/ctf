from os import environ
"""
flag = environ["FLAG"]
format = environ["FORMAT"]
"""
flag = "nitctf"
format = range(10)

shift_table = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
def encrypt(text: str, shift: int) -> str:
    assert  0 <= shift <= 9
    res = ""
    for c in text:
        res += shift_table[(shift_table.index(c)+shift)%len(shift_table)]
    return str(shift) + res
for shift in format:
    flag = encrypt(flag, int(shift))
print(flag)
