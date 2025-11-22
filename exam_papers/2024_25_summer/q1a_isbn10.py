# Summer Examinations 2024/25

# Q1(a)

# International Standard Book Number (ISBN-10) is a 10-character identifier for books, which consists of 
# 9 digits followed by a check character, which is either a digit or the letter 'X' (representing 10).

# The integrity of an ISBN-10 can be verified using its check digit. This is done by multiplying each of the 
# first 9 digits by a factor of 10 to 2 corresponding to their position from left to right. The results are added 
# together and the total is divided by 11. The remainder modulo 11 is then subtracted from 11 to get the 
# check character.  If the result is 10, the check character is 'X'.  If the result is 11, the check character is 0. 
# (See Figure 1 overleaf for a worked example).

# (ii)
# Write a Python function which takes a single string parameter representing the first nine digits of 
# an ISBN-10 and returns a string representing the calculated check character.  Include a suitable 

# documentation string for this function.  

# e.g.:
# 030640615
# 11 - ((0 * 10 + 3 * 9 + 0 * 8 + 6 * 7 + 4 * 6 + 0 * 5 + 6 * 4 + 1 * 3 + 5 * 2) % 11)
# 11 - (0 + 27 + 0 + 42 + 24 + 0 + 24 + 3 + 10) % 11
# 11 - (130 % 11)
# 11 - 9
# 2

# 2024-25 summer 1(a)(i)
def calculated_check_character(isbn10_first9):
    total = 0
    # for digit in isbn10_first9:
    number = int(isbn10_first9)
    for factor in range(2,11):
        # print(digit)
        total += ((number % 10) * factor)
        # print(total)
        number //= 10 # integer division
        # print(number)

    # print(total) # 130
    check_character = 11 - (total % 11)
    # return check_character

    if check_character == 10:
        return 'X'
    elif check_character == 11:
        return '0'
    else:
        return str(check_character)


# print(calculated_check_character("030640615")) # 2
# print(calculated_check_character("567725696")) # X
# print(calculated_check_character("134524298")) # 0

# (ii)
# Write a Python function which takes a single string parameter representing an ISBN-10 and 
# returns a boolean value indicating whether or not it is a valid ISBN-10, according to the above 
# definition.  Include a suitable documentation string for this function. 


def check_valid_isbn10(isbn10):    
    # print(isbn10[0:9])
    # print(calculated_check_character(isbn10[:9]))

    if calculated_check_character(isbn10[:9]) in ("X", "0"):
        return False

    return True


# print(check_valid_isbn10("0306406152"))
# print(check_valid_isbn10("10306406152"))
# print(check_valid_isbn10("567725696Y"))
