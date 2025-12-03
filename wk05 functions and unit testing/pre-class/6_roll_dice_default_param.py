from random import randint


def roll(num_dice=2):
    total = 0

    for i in range(num_dice):
        number = randint(1,6)
        print("Rolled:", number)
        total += number

    print("Total", total)

if __name__ == "__main__":
    print("Rolling 3 dice")
    roll(3)
    print()
    print("Rolling 2 dice")
    roll()