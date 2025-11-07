# A00258304

# Guess the Number is a simple guessing game. The computer “thinks” of a number, and the player has ten attempts to guess it. 
# If the player guesses the number, s/he wins. Otherwise, the computer tells the player if the guess was too high or too low, and s/he can guess again.

# Write a program to implement the game.

# Important: You must use randint() to generate the random number for the game.

# A suggested approach is as follows:
# Generate a random number between 1 and 100
# Repeat 10 times
#     Input the player’s guess
#     Increase number of guesses
#     If the guess is correct 
#         Display "You win, you got it in X guesses"
#         Break from the loop
#     Otherwise if the guess is too high
#         Display "Too high"
#     Otherwise
#         Display "Too low"
# If the user fails to guess in 10 attempts
#         Display "You lose, the number was X"

# Test                                      | Input	| Result
# ----------------------------------------- | ----- | --------------------------------
# Player Loses                              | 75    | Enter your guess: 75
# from random import randint, seed; seed(1) | 70    | Too high
#                                           | 60    | Enter your guess: 70
#                                           | 50    | Too high
#                                           | 40    | Enter your guess: 60
#                                           | 30    | Too high
#                                           | 20    | Enter your guess: 50
#                                           | 10    | Too high
#                                           | 11    | Enter your guess: 40
#                                           | 12    | Too high
#                                           |       | Enter your guess: 30
#                                           |       | Too high
#                                           |       | Enter your guess: 20
#                                           |       | Too high
#                                           |       | Enter your guess: 10
#                                           |       | Too low
#                                           |       | Enter your guess: 11
#                                           |       | Too low
#                                           |       | Enter your guess: 12
#                                           |       | Too low
#                                           |       | You lose, the number was 18
# ----------------------------------------- | ----- | --------------------------------
# Player Wins                               | 50    | Enter your guess: 50
# from random import randint, seed; seed(1) | 25    | Too high
#                                           | 12    | Enter your guess: 25
#                                           | 18    | Too high
#                                           |       | Enter your guess: 12
#                                           |       | Too low
#                                           |       | Enter your guess: 18
#                                           |       | You win, you got it in 4 guesses

from random import randint, seed
seed(1)

random_number = randint(1, 100)

for i in range(10):
    guess_number = int(input("Enter your guess: "))
    
    if guess_number == random_number:
        print(f"You win, you got it in {i + 1} guesses")
        break
    elif guess_number > random_number:
        print("Too high")
    elif guess_number < random_number:
        print("Too low")
else:
    print(f"You lose, the number was {random_number}")