import funcs
import string
import re

in_hex = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


best_score = 0
best_letter = None
best_result = None
for letter in string.ascii_letters:
    result = funcs.xor_simple_char(funcs.hex_str(in_hex), letter)
    # remove ascii control chars
    pretty_result = re.sub(r'[\x00-\x1F]+', '', result)
    # print the result and the corresponding letter used to decode
    score = funcs.get_score(pretty_result)
    if score > best_score:
        best_score = score
        best_result = pretty_result
        best_letter = letter
print(f'{best_letter}: {best_result}, {best_score}')
