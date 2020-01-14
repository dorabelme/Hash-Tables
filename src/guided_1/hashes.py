import time
import hashlib

n = 1000000
key = b"STR"

for i in range(10):
    print(int(hashlib.sha256(key).hexdigest(), 16) % 8)
