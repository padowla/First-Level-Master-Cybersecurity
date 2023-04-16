from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import binascii
#import random #--> the random function is not suitable for crypto usage, because does not generate unpredictable sequences of bytes
import os


iv = os.urandom(16)
#create a cypher
c = Cipher(algorithms.AES(b"questa_La_chiave"),modes.CBC(initialization_vector=iv))

#create an encryptor
enc = c.encryptor()

# if we try to encrypt a block by not aligning it to the 16 bytes defined in the AES standard, the bytes are not encrypted

ct = enc.update(b"quest")

print(binascii.hexlify(ct)) # return no ciphertext

#encrypt a block
ct = enc.update(b"questo_il_blocco") #array of bytes not modifiable of 16 bytes

print(binascii.hexlify(ct)) #print the first cryptogram

ct += enc.update(b"0123456789012345")

print(binascii.hexlify(ct)) ##print the first cryptogram + second cryptogram

ct += enc.update(b"0123456789012345")

print(binascii.hexlify(ct)) ##print the first cryptogram + second cryptogram + third cryptogram by hidden patterns using IV

#create an decryptor
dec = c.decryptor()

pt = dec.update(ct)

#==================================================================================
# If we have a second remote program that needs to decrypt the message.
# We need to receive the IV from who have encrypted the bytes, and IV can be send in cleartext


#============================ padding

print("PADDING - Encryption ---")

p = padding.PKCS7(128).padder() #we must specify dimension of block in bit size that must be a 8-bit multiple

padded_text = p.update(b"questo_il_blocco123") #is not multiple of 8 byte
padded_text += p.update(b"45")
padded_text += p.finalize() # finalize() alerts the padder that it is the last block and then returns the last block that will contain the padding bytes

print(padded_text) # --> b'questo_il_blocco12345\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b' 0xb = 11 because we had 11 bytes to pad


iv = os.urandom(16)
#create a cypher
c = Cipher(algorithms.AES(b"questa_La_chiave"),modes.CBC(iv))
#create an encryptor
enc = c.encryptor()
ct = enc.update(padded_text)
print(binascii.hexlify(ct))

print("---- PADDING Decryption ---")

c2 = Cipher(algorithms.AES(b"questa_La_chiave"),modes.CBC(iv))
#create an encryptor
dec = c.decryptor()
pt = dec.update(ct)
print(pt)


# ===================================== CRT/CCM usato in mondo IoT
# it is a byte-oriented mode of encryption and not block-oriented therefore padding is not necessary
print("------ CRT Exercices----")
nonce = os.urandom(16)
c = Cipher(algorithms.AES(b"questa_La_chiave"),modes.CTR(nonce))
enc = c.encryptor()
ct = enc.update(b"blabla")
print(ct)