import random
import base64
from pwn import *

r = remote("misc.2020.chall.actf.co", 20301)

while True:
    print(r.recv(0x100))
    r.sendline("2")
    r.sendline("T")

