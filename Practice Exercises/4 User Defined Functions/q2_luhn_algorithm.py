def calc_luhn_sum(digits):
    luhn = ""

    for i,char in enumerate(digits[::-1]):
        if i % 2 == 0:
            luhn += char
        else:
            luhn += str(int(char) * 2)
    
    total = 0
    for char in luhn:
        total += int(char)
    return total

def is_valid_sin(sin):
    return len(sin) == 9 and sin.isdigit() and calc_luhn_sum(sin) % 10 == 0
