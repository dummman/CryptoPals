import base64
from Crypto.Cipher import AES

encrypted = base64.b64decode(open("7.txt").read())
key = b"YELLOW SUBMARINE"
decipher = AES.new(key, AES.MODE_ECB)
msg: bytes = decipher.decrypt(encrypted)
print(msg)