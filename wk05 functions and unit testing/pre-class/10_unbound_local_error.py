def increment():
    number += 1 # UnboundLocalError: cannot access local variable 'number' where it is not associated with a value


if __name__ == "__main__":
    number = 0
    print(f"Before: {number}")
    increment()
    print(f"After: {number}")