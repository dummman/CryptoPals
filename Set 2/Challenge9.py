from Crypto.Util.Padding import pad

key = b"YELLOW SUBMARINE"
blocksize = 20

result = pad(key, blocksize)
print(result)
