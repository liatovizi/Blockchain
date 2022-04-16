import hashlib

text = "hello".encode()
text2 = b"hello"
my_hash = hashlib.sha256(text)
my_hash2 = hashlib.sha256(text2)
print(my_hash.hexdigest())