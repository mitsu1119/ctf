import binascii

chs = b"\x00\x00\x00\x00\x00\x00\x00\x00\x42\x09\x4a\x49\x35\x43\x0a\x41\xf0\x19\xe6\x0b\xf5\xf2\x0e\x0b\x2b\x28\x35\x4a\x06\x3a\x0a\x4f"
chs = [chs[i: i+8] for i in range(0, len(chs), 8)]

badflag = b"zer0pts{********CENSORED********}"
badflag = [badflag[i: i+8] for i in range(0, len(badflag), 8)]

flag = b""
for i in range(len(chs)):
    x = int.from_bytes(chs[i], "little")
    x += int.from_bytes(badflag[i], "little")
    x &= 0xffffffffffffffff
    flag += x.to_bytes(8, "little")
    print(flag)

flag += b"}"
print(flag)
