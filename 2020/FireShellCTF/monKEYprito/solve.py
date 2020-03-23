
troll_string = "MmMmMmMmoOoOoOOoOOonnnNnNNnkkKkKkKkKkkkekeekEKkekekEYyYyyYyyYYYYYYYYYY!!!!!!!!!!!!222@@@@@@2XDDDDDDDD" * 6156

array = []
rainbow = 1
with open("you_was_monkeyd.enc", "rb") as f:
    for byte in f.read():
        array.append(hex((byte-ord(troll_string[(rainbow-1)%(len(troll_string)-1)])-rainbow%256)%256))
        rainbow += 1
    
    with open('dec.zip', 'wb') as output:
        output.write(bytearray(int(i, 16) for i in array))


