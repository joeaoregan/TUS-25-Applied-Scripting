# 2024/25 Winter
# Q2(c)

from random import choice

def encipher_text(plaintext, cipher_key={}):
    ciphertext = ""
    for char in plaintext.lower():
        if char.islower():
            # print(char)
            letter = choice(cipher_key[char])
            ciphertext += letter + " "
    # print(ciphertext)
    return ciphertext



test_dict = {"a": ['86', '85', '77', '24', '43', '17', '76'],
             "d": ['99','73','37','98'],
             "e": ['11','83','22','50','30','09','94','39','51','49'],
             "h": ['45','56','23','63','36','13'],
             "l": ['44','01','57','06'],
             "o": ['27','65','26','78','97','04','80'],
             "r": ['15','35','60','10','93'],
             "w": ['72','18']}


print(encipher_text("Hello World", test_dict))