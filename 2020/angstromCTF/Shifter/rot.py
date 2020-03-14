from pwn import *

def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

f = [Fib(n) for n in range(1,51)]

def _rot(i, c):
    if "A" <= c and c <= "Z":
        return chr((ord(c) - ord("A") + i) % 26 + ord("A"))
    if "a" <= c and c <= "z":
        return chr((ord(c) - ord("a") + i) % 26 + ord("a"))
    return c

def rot(i, s):
    g = (_rot(i, c) for c in s)
    return "".join(g)

if __name__ == "__main__":
    r = remote("misc.2020.chall.actf.co", 20300)

    for i in range(50):
        sleep(0.4)
        log.info(i + 1)
        r.recvuntil("Shift ")
        x = r.recvline().split()
        print(x)

        if x[2][0] == ord("n"):
            res = rot(f[int(x[2][2:].decode("utf-8"))], x[0].decode("utf-8"))
            print(res)
            r.sendline(res)

    r.interactive()
