# Q1 (a)
# (i)
def check_imo_test_digit(imo):
    total = 0

    for i in range(len(imo)-1):
        total += int(imo[i]) * (7 - i)

    if total % 10 == int(imo[-1]):
        return True
    return False

# (ii)
def chack_valid_imo_number(imo):
    if len(imo) != 10:
        return False
    
    if "IMO" not in imo:
        return False
    
    return check_imo_test_digit(imo[3:])

if __name__ == "__main__":
    print(check_imo_test_digit("9074729"))
    print(check_imo_test_digit("9074728"))
    print()
    print(chack_valid_imo_number("IMO9074729"))
    print(chack_valid_imo_number("IMO9074728"))
    print(chack_valid_imo_number("IMO19074729"))
    print(chack_valid_imo_number("INO9074729"))