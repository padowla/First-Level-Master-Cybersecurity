from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hmac
import binascii
#import random #--> the random function is not suitable for crypto usage, because does not generate unpredictable sequences of bytes
import os

content_file_enc = ""
salt = ""
tag_from_file = ""
iv = ""
ct = "" #cyphertext
hash_HMAC = hashes.SHA256()
iterations_HMAC = 2**14
tag_size = hashes.SHA256.digest_size
salt_size = 16
iv_size = 16
password = input("Type the password to decrypt:").encode()
file_decrypted_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\Lesson2\\file.txt.enc.dec"
file_encrypted_hmac_path = "C:\\Users\\SamuelePadula\\Desktop\\Python\\Crypto\\Lesson2\\file.txt.enc.hmac"

#read encrypted file
with open(file_encrypted_hmac_path, "rb") as file_encrypted:
    content_file_enc = file_encrypted.read()
    print("----------------- Encrypted HMAC File -----------------")
    print(binascii.hexlify(content_file_enc))
    

if os.path.getsize(file_encrypted_hmac_path) % 16 != 0:
    print("Encrypted file must be multiple of 16 bytes in size!")
    os.exit()

#read SALT + TAG + IV + CT from file
with open(file_encrypted_hmac_path, "rb") as file_encrypted_hmac:
    salt = file_encrypted_hmac.read(salt_size)
    print("----------------- Salt (from file) -----------------")
    print(binascii.hexlify(salt))
    
    tag_from_file = file_encrypted_hmac.read(tag_size)
    print("----------------- HMAC (from file) -----------------")
    print(binascii.hexlify(tag_from_file))
    
    iv = file_encrypted_hmac.read(iv_size)
    print("----------------- IV (from file) -----------------")
    print(binascii.hexlify(iv))
    
    ct = file_encrypted_hmac.read()
    print("----------------- Ciphertext (from file) -----------------")
    print(binascii.hexlify(ct))
    
    print("----------------- Ciphertext Dimension in Byte -----------------")
    print(len(ct), "byte")
    

# derive a key using PBKDF2
kdf = PBKDF2HMAC(hashes.SHA256(),16,salt,iterations_HMAC)
key = kdf.derive(password)
print("----------------- Derived Key -----------------")
print(binascii.hexlify(key))


#verify authenticity of the file
hm = hmac.HMAC(key, hash_HMAC)
hm.update(salt)
hm.update(iv)
hm.update(ct)
hm.verify(tag_from_file) 
print("-----------------!! HMAC Verified !! -----------------")
print(binascii.hexlify(tag_from_file))


# If here without exception, HMAC is verified!, now decrypt

#decrypt cyphertext
cipher = Cipher(algorithms.AES(key),modes.CBC(iv))
#create an encryptor
dec = cipher.decryptor()
padded_plaintext = dec.update(ct)
p = padding.PKCS7(128).unpadder() #we must specify dimension of block in bit size that must be a 8-bit multiple
unpadded_plaintext = p.update(padded_plaintext) + p.finalize()
print("----------------- Plaintext unpadded decrypted -----------------")
print(binascii.hexlify(unpadded_plaintext))


print("----------------- Plaintext decrypted Dimension in Byte -----------------")
print(len(unpadded_plaintext), "byte")

#save decrypted cyphertext to an output file
with open(file_decrypted_path, "wb") as file_decrypted:
    file_decrypted.write(unpadded_plaintext)

#open file as text
with open(file_decrypted_path, "r", encoding="utf-8") as file_decrypted:
    print("----------------- Decrypted File (text) -----------------")
    print(file_decrypted.read())


