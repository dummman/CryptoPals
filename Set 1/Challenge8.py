block_size = 16
with open("8.txt") as fb:
    repititions =[]
    for ciphertext in fb.readlines():
        ciphertext = bytes.fromhex(ciphertext)
        chunks = [ciphertext[i:i+block_size] for i in range(0, len(ciphertext), block_size)]
        num_repititions = len(chunks) - len(set(chunks))
        result = {'ciphertext': ciphertext, 'repititions': num_repititions}
        repititions.append(result)
    most_repititions = sorted(repititions, key=lambda x: x["repititions"], reverse=True)[0]
    print(most_repititions)
