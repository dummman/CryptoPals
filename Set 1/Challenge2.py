#  Fixed XOR
from funcs import hex_byte, byte_hex, xor_bytestr

hex1 = "1c0111001f010100061a024b53535009181c"
hex2 = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"

b64_1 = hex_byte(hex1)
b64_2 = hex_byte(hex2)

xored = xor_bytestr(b64_1, b64_2)
print(byte_hex(xored) == expected)
print(xored)
