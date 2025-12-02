#copies = int(input("Enter number of copies: "))

copies = 51

if copies <= 50:
    cost = copies * 0.11
elif copies <= 100:
    cost = copies * 0.1
elif copies <= 1000:
    cost = copies * 0.09
else:
    cost = copies * 0.08
    
print(f"Cost is {cost:.2f}")