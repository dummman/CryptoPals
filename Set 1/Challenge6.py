import funcs
import base64

print(funcs.hamming_dist(b"this is a test", b"wokka wokka!!!") == 37)  # True

with open("6.txt") as input_file:
    # encrypted = f.read().strip().replace(r'\n', '')
    encrypted = base64.b64decode(input_file.read())
    average_distances = []
    for keysize in range(2, 41):
        distances = []
        chunks = [encrypted[i:i+keysize] for i in range(0, len(encrypted), keysize)]
        while True:
            try:
                chunk1 = chunks[0]
                chunk2 = chunks[1]
                distances.append(funcs.hamming_dist(chunk1, chunk2)/keysize)
                del chunks[0]
                del chunks[1]
            except Exception:
                break
        result = {'key': keysize, 'avg distance': sum(distances) / len(distances)}
        average_distances.append(result)
    possible_key_lengths = sorted(average_distances, key=lambda x: x['avg distance'])[0]
    possible_plaintext = []

    key = b''
    possible_key_length = possible_key_lengths['key']
    for i in range(possible_key_length):
        block = b''
        for j in range(i, len(encrypted), possible_key_length):
            block += bytes([encrypted[j]])
        key += bytes([funcs.bruteforce_single_char_xor(block)['key']])
    print(key)
    possible_plaintext.append((funcs.repeating_key_xor(encrypted, key), key))
# print(max(possible_plaintext, key=lambda x: get_english_score(x[0])))
print(possible_plaintext)

