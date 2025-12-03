copies = int(input("Enter number of copies: "))

if copies <= 100:
    cost = copies * 0.05

if copies > 100:
    cost = 100 * 0.05 + (copies - 100) * 0.03

print(f"Cost is {cost:.2f}")
