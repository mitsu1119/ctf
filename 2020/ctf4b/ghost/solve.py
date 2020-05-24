from pwn import *

output = ["3417", "61039", "39615", "14756", "10315", "49836", "44840", "20086", "18149", "31454", "35718", "44949", "4715", "22725", "62312", "18726", "47196", "54518", "2667", "44346", "55284", "5240", "32181", "61722", "6447", "38218", "6033", "32270", "51128", "6112", "22332", "60338", "14994", "44529", "25059", "61829", "52094"]

ch = "!abcdefghijklmnopqrstuvwxyz_0123456789{}"
flag = "ctf4b{st4ck_m4ch1n3_1s_4_l0t_0f_fun!}"

cnt = 0
while True:
    r = process(["gs", "chall.gs"])
    sleep(0.3)
    r.recv(0x100)

    r.sendline(flag)
    out = r.recvline()[:-1].decode("utf-8")
    # log.info("recv: {}".format(out))

    out = out.split()
    if out[-1] != output[len(out) - 1]:
        flag = flag[:-1]
        cnt += 1
        flag += ch[cnt]
        print("Error:", flag)
    else:
        cnt = 0
        flag += "a" 
        log.info("Success: {}".format(flag))

    r.close()

