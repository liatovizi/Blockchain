import hashlib
import timeit

hash_ = hashlib.sha256(b'test')
start_time = timeit.default_timer()
difficulty = 3
nonce = 0

while hash_.hexdigest()[0:difficulty] != "0"*difficulty:
    hash_ = hashlib.sha256(("test" + str(nonce)).encode())
    nonce +=1

end_time = timeit.default_timer() - start_time
print(end_time)
print(nonce)
print(hash_.hexdigest())

