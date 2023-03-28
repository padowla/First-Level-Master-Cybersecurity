from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import binascii
#import random #--> the random function is not suitable for crypto usage, because does not generate unpredictable sequences of bytes
import os

content_file = ""
key = b"questa_La_chiave"
file_plaintext_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\file.txt"
file_encrypted_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\file.txt.enc"

#open file as text
with open(file_plaintext_path, "r", encoding="utf-8") as file_to_enc:
    print("----------------- Plaintext File (text) -----------------")
    print(file_to_enc.read())
    print("---------------------------------------------------")


#open file as byte
with open(file_plaintext_path, "rb") as file_to_enc:
    content_file = file_to_enc.read()
    print("----------------- Plaintext File (Byte) -----------------")
    print(binascii.hexlify(content_file))
    print("---------------------------------------------------")

print("----------------- Plaintext File Dimension in Byte -----------------")
print(os.path.getsize(file_plaintext_path), "byte")
print("---------------------------------------------------")


#padding of file with PKCS#7

p = padding.PKCS7(128).padder() #we must specify dimension of block in bit size that must be a 8-bit multiple

padded_text = p.update(content_file) + p.finalize()

print("----------------- Padded Text -----------------")
print(binascii.hexlify(padded_text))
print("---------------------------------------------------")

print("----------------- Padded Plaintext Dimension in Byte -----------------")
print(len(padded_text), "byte")
print("---------------------------------------------------")

#encrypt with AES in CBC modewith IV and KEY

iv = os.urandom(16)
print("----------------- IV -----------------")
print(binascii.hexlify(iv))
print("---------------------------------------------------")

print("----------------- IV Dimension in Byte -----------------")
print(len(iv), "byte")
print("---------------------------------------------------")

cipher = Cipher(algorithms.AES(key),modes.CBC(iv))
enc = cipher.encryptor()
ct = enc.update(padded_text)
print("----------------- Ciphertext -----------------")
print(binascii.hexlify(ct))
print("---------------------------------------------------")

print("----------------- Ciphertext Dimension in Byte -----------------")
print(len(ct), "byte")
print("---------------------------------------------------")

#save IV and ciperthext to an output file
with open(file_encrypted_path, "wb") as file_encrypted:
    content_file_enc = file_encrypted.write(iv)
    content_file_enc = file_encrypted.write(ct)

#read encrypted file
with open(file_encrypted_path, "rb") as file_encrypted:
    content_file_enc = file_encrypted.read()
    print("----------------- Encrypted File -----------------")
    print(binascii.hexlify(content_file_enc))
    print("---------------------------------------------------")

print("----------------- Plaintext File Dimension in Byte -----------------")
print(os.path.getsize(file_encrypted_path), "byte")
print("---------------------------------------------------")