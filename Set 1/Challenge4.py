import funcs
import re

best_score_overall = 0
best_letter_overall = None
best_result_overall = None
best_line_idx = 0
best_line = None

with open('4.txt') as f:
    for line_idx, line in enumerate(f, start=1):
        line = line.strip()
        for letter in funcs.alphanumeric_characters:
            try:
                result = funcs.xor_simple_char(funcs.hex_str(line), letter)
            except UnicodeDecodeError as e:
                continue
            pretty_result = re.sub(r'[\x00-\x1F]+', '', result)
            score = funcs.get_score(pretty_result)
            if score > best_score_overall:
                best_score_overall = score
                best_result_overall = pretty_result
                best_letter_overall = letter
                best_line = line
                best_line_idx = line_idx
print(f'{best_line}, {best_line_idx}: {best_letter_overall}: {best_result_overall}, {best_score_overall}')
