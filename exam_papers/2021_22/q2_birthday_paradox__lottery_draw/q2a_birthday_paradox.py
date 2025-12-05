# Q1a(i)
from random import randint
num_duplicates = 0

# Q1a(ii)
num_simulations = int(input("How many simulations? "))
num_people = int(input("How many people? "))

# Q1a(iii)
for i in range(num_simulations):
    birthdays = []

    for j in range(num_people):
        birthdays.append(randint(1,366))

    unique_values = set(birthdays)

    if len(unique_values) < num_people:
        num_duplicates += 1

# Q1a(iv)
print(f"Percentage of simulations with a duplicate: {num_duplicates/num_simulations:.1%}")