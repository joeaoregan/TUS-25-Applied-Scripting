total = 0
point = 0

# Check if the player has won on the first roll
if total == 7 or total == 11:
    print("You win")

# Check if the player has lost on the first roll
elif total == 2 or total == 3 or total == 12:
    print("You lose")

# Using a list

if total in [7,11]:
    print("You win")

elif total in [2,3,12]:
    print("You lose")


# Keep rolling until player wins or loses
while total != 7 and total != point:
    input("Press Enter to roll the dice ")

# Using a list
while total not in [7,point]:
    input("Press Enter to roll the dice ")