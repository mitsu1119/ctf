from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from secret import password, flag
from hashlib import sha256

NB_ITERATIONS = 10871177237854734092489348927
e = 65538
N = 16725961734830292192130856503318846470372809633859943564170796604233648911148664645199314305393113642834320744397102098813353759076302959550707448148205851497665038807780166936471173111197092391395808381534728287101705


def derive_key(password):
	start = bytes_to_long(password)

	#Making sure I am safe from offline bruteforce attack
	
	for i in range(NB_ITERATIONS):
		start = start ** e
		start %= N
	
	#We are never too cautious let's make it harder
	
	key = 1
	for i in range(NB_ITERATIONS):
		key = key ** e
		key %= N
		key *= start
		key %= N
	
	return sha256(long_to_bytes(key)).digest()


assert(len(password) == 2)
assert(password.decode().isprintable())

key = derive_key(password)
IV = b"random_and_safe!"
cipher = AES.new(key, AES.MODE_CBC,IV)
enc = cipher.encrypt(pad(flag,16))

with open("flag.enc","wb") as output_file:
	output_file.write(enc)