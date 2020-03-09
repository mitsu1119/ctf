M   print mem   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
+s+>s   reg = 2
        p = 1
        mem = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0]
>++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        p = 2
        reg = 62

[s<<l>*<s>>l-]
    # [62, 1]
    for i in range(62, 1):
        mem[2] = i
        mem[0] *= mem[1]
    reg = 0

    => mem[0] = pow(2, 62)
       mem[2] = 1
       reg = 0

<<  p = 0
l-  reg = mem[0] - 1
s   mem[0] -= 1
>   p = 1

l*- reg = mem[1] * mem[1] - 1
s   mem[1] = reg
*-  reg = mem[1] * mem[1] - 1 
s   mem[1] = reg
*-  reg = mem[1] * mem[1] - 1
s   mem[1] = reg
*-  reg = mem[1] * mem[1] - 1
s   mem[1] = reg
*-  reg = mem[1] * mem[1] - 1
s   mem[1] = reg
*-  reg = mem[1] * mem[1] - 1
s   mem[1] = reg

>   p = 2
l*+++++
    reg = mem[2] * mem[2] + 5
s   mem[2] = reg
*-----
    reg = reg * mem[2] - 5
s   mem[2] = reg
****    reg *= pow(mem[2], 4)
s   mem[2] = reg

>>  p = 4
l+  reg = mem[4] + 1
s   mem[4] = reg

[Ml-s<<l>,[<<*>>s<<<l>>>%<s>>l<s>l+s<l] >l]
while reg != 0:
    print mem
    mem[4] -= 1
    reg = mem[2]
    a = input()
    if not a:
        reg = 0
    else:
        reg += ord(a)
    while reg != 0:
        mem[2] = (reg * mem[1]) % mem[0]
        mem[3] = mem[4]
        mem[4] += 1
        reg = mem[3]
    reg = mem[4]

<<  p = 2
l   reg = mem[p]
p   print reg
