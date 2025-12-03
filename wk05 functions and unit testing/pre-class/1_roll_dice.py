from random import randint

def roll_dice():
    input("Press Enter to roll the dice ")
    roll1 = randint(1,6)
    roll2 = randint(1,6)
    total = roll1 + roll2
    print(f"You rolled: {roll1} and {roll2}, Total: {total}")    
    return total

total = roll_dice()

amount = 0
bet = 0

if total == 7 or total == 11:
    print("You win")
    amount += bet * 2

elif total == 2 or total == 3 or total == 12:
    print("You lose")

else:
    point = total
    total = 0
    print(f"Roll your point {point} to win, or 7 to lose.")

    while total != 7 and total != point:
        total = roll_dice()
