import hashlib

#SHA-1 return 160 bit of digest but is obsolete
print(hashlib.md5(b"ciao, mondo!").hexdigest())

#SHA-1 return 160 bit of digest but is obsolete
print(hashlib.sha1(b"ciao, mondo!").hexdigest())

#SHA-2
print(hashlib.sha256(b"ciao, mondo!").hexdigest())

#SHA-3 differs from SHA-2 in that it was intended to have 
#a fallback solution in case SHA-2 fell victim to cryptanalytic attacks in the future. 
#By following 2 different mathematics they could not have suffered from the same vulnerability
print(hashlib.sha3_256(b"ciao, mondo!").hexdigest())

# ---------------------------------------------------------
print("\n\n\==================Context hashes==================\n")
from cryptography.hazmat.primitives import hashes
import binascii

#context reshuffling
h = hashes.Hash(hashes.SHA256())

#I provide chunks of the message at a time via incremental update functions
h.update(b"ciao, ")
#updates return nothing since it is necessary to have all the input to compute the digest
h.update(b"mondo!")
sha256 = h.finalize()
print(binascii.hexlify(sha256))

# Suppose we receive the message and calculate the hash and compare it with the one received to see if it matches
#sha256_ is a local hash calculated
sha256_ = hashlib.sha256(b"ciao, mondo!").digest()
print(sha256_)


if sha256 == sha256_:
    print("MATCH!")
else:
    print("NO MATCH!")

# ^^^^^^^^^^^^^^ THIS METHOD IS NOT SECURE 

# ---------------------------------------------------
print("\n\n=================Time-Constant Comparison Hashes===================\n")

from cryptography.hazmat.primitives import constant_time

if constant_time.bytes_eq(sha256_,sha256):
    print("MATCH!")
else:
    print("NO MATCH!")


#----------------------------------------------------
#The keyed hash functions, HMAC, are a kind of hash assembly. 
#HMAC is a way of mounting a hash by endowing it with a key. 
#The digest you get will be equal to that of the hash function used to mount.
#HMAC provides no constraints on the length of the key to be used. 

# ---------------------------------------------------
print("\n\n=================Keyed-hash functions===================\n")

from cryptography.hazmat.primitives import hmac

hm = hmac.HMAC(b"questa chiave qua",hashes.SHA256())
hm.update(b"ciao, mondo!")
tag = hm.finalize()
print("HMAC=",binascii.hexlify(tag))

#I can also configure the TLS protocol to not encrypt but only authenticate (HMAC) packets.

# ---------------------------------------------------
print("\n\n=================verify() HMAC===================\n")

hm = hmac.HMAC(b"questa chiave qua",hashes.SHA256())
hm.update(b"ciao, mondo!")
# to verify() I pass the tag received from the communication channel. 
# It consists of a finalize and a constant-time check. If the tag does not match it raises an exception:
# cryptography.exceptions.InvalidSignature: Signature did not match digest.
hm.verify(tag) 
print("MSG AUTENTICO!")


# ---------------------------------------------------
print("\n\n=================Key Derivation Function===================\n")
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

salt = os.urandom(16)
# you can choose a digest length in bytes and the number of iterations
kdf = PBKDF2HMAC(hashes.SHA256(),16,salt,2**14)
key = kdf.derive(b"1234")
print(binascii.hexlify(salt))
print(binascii.hexlify(key))