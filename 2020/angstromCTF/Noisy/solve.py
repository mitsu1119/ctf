from decimal import Decimal, ROUND_HALF_UP
import sys

repeats = int(sys.argv[1])

def sum(li):
    res = 0
    for i in li:
        res += i
    return res

def mean(li):
    mm = Decimal(str(sum(li) / len(li))).quantize(Decimal("0"), rounding=ROUND_HALF_UP)
    return float(mm)

fsize = 28800
msize = fsize // 10

f = open("4ea.txt", "r")

x = msize // repeats
signals = []

for i in range(repeats):
    for j in range(x):
        points = []
        for _ in range(10):
            points.append(float(f.readline()) + 0.5)
        if i == 0:
            signals.append(points)
        else:
            signals[(i * x + j) % x] += points

morsebits = ""
for i in range(len(signals)):
    signal = mean(signals[i])
    if signal == 0.0:
        morsebits += "0"
    elif signal == 1.0:
        morsebits += "1"
    else:
        morsebits += str(int(signal))

print(morsebits)

morse = ""
i = 0
while i < len(morsebits):
    c = morsebits[i]
    print(c, end="")
    if i < len(morsebits) - 1 and c == "1" and morsebits[i + 1] == "1":
        morse += "-"
        i += 2 
    elif c == "1":
        morse += "."
        i += 1
    else:
        if i < len(morsebits) - 1 and morsebits[i + 1] == "0":
            morse += " "
        else:
            print("Error!")
        i += 2

    i += 1

print("")
print(morse)
    
f.close()    

# noisynoise
