from pwn import *
from binascii import unhexlify, hexlify

r = remote("crypto.kosenctf.com", 13005)

msg = b"ohayougozaimasu"
r.sendline(hexlify(msg))

r.interactive()

# KosenCTF{ahhhh_ochazuke_oisi_geho!geho!!gehun!..oisii...}
