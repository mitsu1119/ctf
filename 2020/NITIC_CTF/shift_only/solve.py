
flag = "6}bceijnob9h9303h6yg896h0g896h0g896h01b40g896hz"

shift_table = "abcdefghijklmnopqrstuvwxyz0123456789{}_"
def decrypt(text: str, shift: int) -> str:
    # assert(0 <= shift <= 9)
    res = ""
    for c in text:
        ind = shift_table.index(c) - shift
        if ind >= len(shift_table):
            ind = ind % len(shfit_table)
        res += shift_table[ind]
    return str(shift) + res

cnt = 0
while True:
    print("dec:", flag[2 * cnt])
    flag = decrypt(flag, int(flag[2 * cnt]))
    cnt += 1
    print(flag)

