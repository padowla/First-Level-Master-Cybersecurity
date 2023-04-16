from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hmac
import binascii
#import random #--> the random function is not suitable for crypto usage, because does not generate unpredictable sequences of bytes
import os

content_file = ""
tag = ""
hash_HMAC = hashes.SHA256()
iterations_HMAC = 2**14
salt_size = 16
iv_size = 16
password = input("Type the password to encrypt:").encode()
file_plaintext_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\Lesson2\\file.txt"
file_encrypted_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\Lesson2\\file.txt.enc"
file_encrypted_hmac_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\Lesson2\\file.txt.enc.hmac"

#open plaintext file as text
with open(file_plaintext_path, "r", encoding="utf-8") as file_to_enc:
    print("----------------- Plaintext File (text) -----------------")
    print(file_to_enc.read())
    


#open plaintext file as byte
with open(file_plaintext_path, "rb") as file_to_enc:
    content_file = file_to_enc.read()
    print("----------------- Plaintext File (Byte) -----------------")
    print(binascii.hexlify(content_file))
    

print("----------------- Plaintext File Dimension in Byte -----------------")
print(os.path.getsize(file_plaintext_path), "byte")



# derive a key using PBKDF2
salt = os.urandom(salt_size)
kdf = PBKDF2HMAC(hashes.SHA256(),16,salt,iterations_HMAC)
key = kdf.derive(password)
print("----------------- Salt -----------------")
print(binascii.hexlify(salt))

print("----------------- Derived Key -----------------")
print(binascii.hexlify(key))



#padding of file with PKCS#7

p = padding.PKCS7(128).padder() #we must specify dimension of block in bit size that must be a 8-bit multiple
padded_text = p.update(content_file) + p.finalize()
print("----------------- Padded Text -----------------")
print(binascii.hexlify(padded_text))

print("----------------- Padded Plaintext Dimension in Byte -----------------")
print(len(padded_text), "byte")


#encrypt with AES in CBC mode with IV and KEY

iv = os.urandom(iv_size)
print("----------------- IV -----------------")
print(binascii.hexlify(iv))

print("----------------- IV Dimension in Byte -----------------")
print(len(iv), "byte")


cipher = Cipher(algorithms.AES(key),modes.CBC(iv))
enc = cipher.encryptor()
ct = enc.update(padded_text)
print("----------------- Ciphertext -----------------")
print(binascii.hexlify(ct))


print("----------------- Ciphertext Dimension in Byte -----------------")
print(len(ct), "byte")



# compute MAC on SALT+IV+CT using encrypted file of as input of HMAC

hm = hmac.HMAC(key,hash_HMAC)
hm.update(salt)
hm.update(iv)
hm.update(ct)
tag = hm.finalize()
print("----------------- HMAC Encrypted File (SALT + IV + CT) -----------------")
print(binascii.hexlify(tag))

print("----------------- HMAC Dimension in Byte -----------------")
print(len(tag), "byte")


#save SALT + HMAC + IV + CT to an output file
with open(file_encrypted_hmac_path, "wb") as file_encrypted_hmac:
    file_encrypted_hmac.write(salt)
    file_encrypted_hmac.write(tag)
    file_encrypted_hmac.write(iv)
    file_encrypted_hmac.write(ct)

#read encrypted hmac file
with open(file_encrypted_hmac_path, "rb") as file_encrypted_hmac:
    content_file_enc_hmac = file_encrypted_hmac.read()
    print("----------------- Encrypted HMAC File -----------------")
    print(binascii.hexlify(content_file_enc_hmac))
    

print("----------------- Encrypted HMAC File Dimension in Byte -----------------")
print(os.path.getsize(file_encrypted_hmac_path), "byte")

