import angr
import glob
from pwn import *
import sys
import claripy

addr_succeeded = 0x1230
addr_failed = 0x1229
tokenLen = 0x20

r = remote("tasks.aeroctf.com", 44324)

idx = 1
while True:
    log.info("idx = {}".format(idx))
    if idx == 31:
        print(r.recv(0x100))
    r.recvuntil("<")
    fname = "./files/" + r.recvline()[:-2].decode("utf-8")

    p = angr.Project(fname, main_opts={"base_addr": 0}, auto_load_libs=False)
    state = p.factory.entry_state()
    simgr = p.factory.simulation_manager()

    simgr.explore(find=addr_succeeded, avoid=[addr_failed])
    found = simgr.found[0]
    token = found.posix.dumps(0)[:tokenLen].decode("utf-8")
    print("name = " + fname)
    print("token = " + token)

    r.sendline(token)
    print(r.recv(0x100))
    idx += 1

# flag = Aero{0f9e7ddd2be70f58b86f8f6589e17f182fc21c71437c2d9923fefa7ae281712b}
