from Crypto.PublicKey import RSA

def import_pubkey(filename):
    with open(filename) as f:
        key = RSA.importKey(f.read())
    return key.n, key.e

