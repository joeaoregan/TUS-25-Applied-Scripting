my_numbers = [1, 2, 3, 4, 5]

if len(my_numbers) < 6:
    print("a")

for number in my_numbers:
    print("b", end=" ")

while len(my_numbers) < 6:
    print("c", end = " ")

while len(my_numbers) <= 6:
    print("d", end=" ")