from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import binascii
#import random #--> the random function is not suitable for crypto usage, because does not generate unpredictable sequences of bytes
import os

content_file_enc = ""
iv = ""
ct = "" #cyphertext
key = b"questa_La_chiave"
file_decrypted_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\file.txt.enc.dec"
file_encrypted_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\file.txt.enc"

#read encrypted file
with open(file_encrypted_path, "rb") as file_encrypted:
    content_file_enc = file_encrypted.read()
    print("----------------- Encrypted File -----------------")
    print(binascii.hexlify(content_file_enc))
    print("---------------------------------------------------")

if os.path.getsize(file_encrypted_path) % 16 != 0:
    print("Encrypted file must be multiple of 16 bytes in size!")
    os.exit()


#extract IV from encrypted file - the first 16 byte are IV
with open(file_encrypted_path, "rb") as file_encrypted:
    iv = file_encrypted.read(16)
    print("----------------- IV -----------------")
    print(binascii.hexlify(iv))
    print("---------------------------------------------------")
    ct = file_encrypted.read()
    print("----------------- Ciphertext -----------------")
    print(binascii.hexlify(ct))
    print("---------------------------------------------------")

    print("----------------- Ciphertext Dimension in Byte -----------------")
    print(len(ct), "byte")
    print("---------------------------------------------------")

#decrypt cyphertext
cipher = Cipher(algorithms.AES(key),modes.CBC(iv))
#create an encryptor
dec = cipher.decryptor()
padded_plaintext = dec.update(ct)
p = padding.PKCS7(128).unpadder() #we must specify dimension of block in bit size that must be a 8-bit multiple
unpadded_plaintext = p.update(padded_plaintext) + p.finalize()
print("----------------- Plaintext unpadded decrypted -----------------")
print(binascii.hexlify(unpadded_plaintext))
print("---------------------------------------------------")

print("----------------- Plaintext decrypted Dimension in Byte -----------------")
print(len(unpadded_plaintext), "byte")
print("---------------------------------------------------")

#save decrypted cyphertext to an output file
with open(file_decrypted_path, "wb") as file_decrypted:
    file_decrypted.write(unpadded_plaintext)

#open file as text
with open(file_decrypted_path, "r", encoding="utf-8") as file_decrypted:
    print("----------------- Decrypted File (text) -----------------")
    print(file_decrypted.read())
    print("---------------------------------------------------")

