from time import perf_counter

def calculated_check_character(isbn10_first9):
    total = 0
    number = int(isbn10_first9)
    for factor in range(2,11):
        total += ((number % 10) * factor)
        number //= 10 # integer division

    check_character = 11 - (total % 11)

    if check_character == 10:
        return 'X'
    elif check_character == 11:
        return '0'
    else:
        return str(check_character)


def measure_execution_time():
    start = perf_counter()
    calculated_check_character("030640615")
    end = perf_counter()
    return end - start


if __name__=="__main__":
    print(f"calculated_check_character() execution time: {measure_execution_time()}")