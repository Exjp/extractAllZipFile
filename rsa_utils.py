from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as cipher_algorithm
from OpenSSL import crypto
import base64

def encrypt(data, certPath):
    str_cert = open(certPath, 'rt').read()
    cert = crypto.load_certificate(crypto.FILETYPE_PEM, str_cert)
    pKey = cert.get_pubkey()
    pKeyString = crypto.dump_publickey(crypto.FILETYPE_PEM,pKey)
    public = RSA.importKey(pKeyString)

    cipher = cipher_algorithm.new(public)
    cipher_text = cipher.encrypt("Hello World!".encode())
    sign = base64.b64encode(cipher_text)

    return sign

def decrypt(cipherText, keyPath):
    with open(keyPath,'rb') as fk:
    	priv = fk.read()
    	fk.close()
    privat = RSA.importKey(priv)

    cipher = base64.b64decode(cipherText)
    pr = cipher_algorithm.new(privat)
    x = pr.decrypt(cipher, "error")
    x = x.decode('utf-8')

    return x

#str = "Hello World!"
#print(str)
#print()
#enc_str = encrypt(str, 'ca_crt.pem')
#print(enc_str)
#print()
#print(decrypt(enc_str, 'ca_key.pem'))
