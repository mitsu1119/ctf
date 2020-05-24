from pwn import *
import numpy as np

r = remote("noisy-equations.quals.beginners.seccon.jp", 3000)
coeffs1 = eval(r.recvline())
answers1 = eval(r.recvline())
r.close()

r = remote("noisy-equations.quals.beginners.seccon.jp", 3000)
coeffs2 = eval(r.recvline())
answers2 = eval(r.recvline())
r.close()


dots = [a - b for a, b in zip(answers1, answers2)]

factors = [[a - b for a, b in zip(coeffs1[i], coeffs2[i])] for i in range(len(coeffs1))]

factors = np.matrix(factors).astype(np.float64)
dots = np.matrix(dots).astype(np.float64).transpose()

flag = np.linalg.inv(factors) * dots
flag = list(flag.tolist())

for i in flag:
    print(chr(round(i[0])), end="")

