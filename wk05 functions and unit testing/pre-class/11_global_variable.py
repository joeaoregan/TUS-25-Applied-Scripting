def increment():
    global number
    number += 1


if __name__ == "__main__":
    number = 0
    print(f"Before: {number}")
    increment()
    print(f"After: {number}")