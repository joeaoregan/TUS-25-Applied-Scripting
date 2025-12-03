from random import randint

def roll(num_dice):
    total = 0

    for i in range(num_dice):
        number = randint(1, 6)
        print("Rolled:", number)
        total += number
    print("Total", total) 


if __name__ == "__main__":
    roll(3)