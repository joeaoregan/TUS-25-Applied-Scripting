# Q2b(i)
from random import sample
numbers = sample(range(1,51),5)

# Q2b(ii)
user_input = input("Enter 5 numbers, separated by spaces: ")
users_numbers = [int(value) for value in user_input.split()]

matches = 0
for number in users_numbers:
    if number in numbers:
        matches += 1

print(f"Lottery Numbers: {sorted(numbers)}")

print(f"You matched: {matches} numbers")