from random import sample

def homo_sub_cipher(frequencies):
    digit_pairs = [f"{x:02d}" for x in range(100)]
    # print(digit_pairs)
    cipher_key = {}
    for letter in frequencies:
        items = sample(digit_pairs, k=int(frequencies[letter]))
        cipher_key[letter] = items

        for item in items:
            if item in digit_pairs:
                digit_pairs.remove(item)
    return cipher_key
        

