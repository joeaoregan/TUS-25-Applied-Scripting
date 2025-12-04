# Input the winning numbers as a single string, separated by spaces
winning_numbers = input("Enter the winning lotto numbers: ")
# Create a list containing the individual winning numbers, using 
winning_list = winning_numbers.split()
# Input the player's numbers as a single string, separated by spaces
player_numbers = input("Enter your numbers: ")
# Create a list containing the player's numbers (in the same way as the second step, above)
player_list = player_numbers.split()
# Initialise a variable count to zero; this will count how many numbers have been matched
count = 0
# For each of the player's numbers
for number in player_list:
#     If the player's number is in the winning numbers list:
    if number in winning_list:
#         Increase count by 1
        count += 1
# Display how many numbers the player matched
print(f"You matched {count} numbers")