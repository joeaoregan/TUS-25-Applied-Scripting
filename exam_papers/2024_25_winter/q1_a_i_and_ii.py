# Q1 (a)
# (i)
def check_valid_check_digit(imo):
    total = 0

    for i,digit in enumerate(imo):
        total += int(digit) * (7-i)        
        if i == 5: break

    return (total % 10) == int(imo[-1])

# (ii)
def check_valid_imo(imo):
    if len(imo) != 10:
        return False
    
    if imo[:3] != "IMO":
        return False
    
    if check_valid_check_digit(imo[3:]):
        return True
    return False 

if __name__ == "__main__":
    print(check_valid_check_digit("9074729"))
    print(check_valid_check_digit("9074728"))
    print()
    print(check_valid_imo("IMO9074729"))
    print(check_valid_imo("IMO9074728"))
    print(check_valid_imo("IMO19074729"))
    print(check_valid_imo("INO9074729"))