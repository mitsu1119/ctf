with open("kitters.jpg", "rb") as f:
    kitters = f.read()

with open("cattos.jpg", "rb") as f:
    cattos = f.read()

for i in range(len(kitters)):
    if kitters[i] != cattos[i]:
        print(chr(cattos[i]), end="")
