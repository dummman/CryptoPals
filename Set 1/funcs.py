from base64 import b64encode, b64decode
from itertools import cycle
import string
import re

monogram_frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074 ]
alphanumeric_characters = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "


def hex_byte(hex_string: str) -> str:
    return bytes.fromhex(hex_string)


def byte_hex(byte_string: str) -> str:
    return bytes.hex(byte_string)


def hex_str(hex_string: str) -> str:
    # return bytes.fromhex(hex_string).decode('utf-8')
    return bytes.fromhex(hex_string).decode('ascii')


def hex_b64(hex_string: str) -> str:
    raw_byte = hex_byte(hex_string)
    b64 = b64encode(raw_byte)
    return b64.decode()


def b64_hex(b64_string: str) -> str:
    return b64decode(b64_string.encode()).hex()


def xor_bytestr(first: str, second: str) -> str:
    return bytes(i ^ j for i, j in zip(first, second))


def xor_simple_bytestr(input_bytes: str, char_value: str) -> str:
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def xor_simple_char(str_string: str, byte: str) -> str:
    return "".join(chr(ord(c) ^ ord(byte)) for c in str_string)


def xor_str(first: str, key: str) -> str:
    result = "".join(chr(ord(c) ^ ord(byte)) for c, byte in zip(first, cycle(key)))
    return result.encode("utf-8").hex()


def repeating_key_xor(message_bytes, key):
    """Returns message XOR'd with a key. If the message, is longer
    than the key, the key will repeat.
    """
    output_bytes = b''
    index = 0
    for byte in message_bytes:
        output_bytes += bytes([byte ^ key[index]])
        if (index + 1) == len(key):
            index = 0
        else:
            index += 1
    return output_bytes


def get_score(result: str) -> int:
    score = 0
    for c in result:
        if c == ' ':
            score += 13
            continue
        try:
            idx = string.ascii_lowercase.index(c.lower())
        except ValueError:
            continue
        score += monogram_frequencies[idx]
    return score


def bruteforce_single_char_xor(input_string: str) -> dict:
    potential_messages = []
    for letter in alphanumeric_characters:
        try:
            # if type(input_string) == hex:
            #     result = xor_simple_char(hex_str(input_string), letter)
            # else:
            byte_result = xor_simple_bytestr(input_string, ord(letter))
            result = ''
            for b in byte_result:
                result += chr(b)
        except UnicodeDecodeError as e:
            continue
        pretty_result = re.sub(r'[\x00-\x1F]+', '', result)
        score = get_score(pretty_result)
        data = {
            'message': pretty_result,
            'score': score,
            'key': ord(letter)
        }
        potential_messages.append(data)
    return sorted(potential_messages, key=lambda x: x['score'])[-1]


def hamming_dist(first: str, second: str) -> int:
    return bin(int.from_bytes(xor_bytestr(first, second), "little")).count("1")


