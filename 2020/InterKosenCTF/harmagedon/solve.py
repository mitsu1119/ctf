
def calc(ps):
    if len(ps) == 1:
        return 4 * (ps[0] + 1)

    return 4 * (calc(ps[1:]) + ps[0] + 1)

for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                for e in range(4):
                    for f in range(4):
                        for g in range(4):
                            for h in range(4):
                                for i in range(4):
                                    for j in range(4):
                                        for k in range(4):
                                            xxx = [a,b,c,d,e,f,g,h,i,j,k]
                                            m = calc(xxx[::])
                                            print(m)
                                            if m == 0xb77c7c:
                                                print(list(reversed(xxx)))
                                                exit(1)
# [1, 2, 0, 2, 0, 2, 1, 3, 0, 2, 2]
# KosenCTF{Ruktun0rDi3}

