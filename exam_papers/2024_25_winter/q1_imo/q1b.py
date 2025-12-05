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
    while(True):
        imo = input("Enter the IMO number or q to quit: ")
        if imo.lower() == "q":
            break
        
        if check_valid_imo(imo):
            print("Valid IMO number")
        else:
            print("Not a valid IMO number")
