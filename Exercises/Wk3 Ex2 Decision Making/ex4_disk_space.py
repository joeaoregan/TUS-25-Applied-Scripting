# A00258304

# An important System Administration task is to monitor the availability of disk space on a computer system:
# * If there is no free space, the system might crash;
# * If the percentage of free disk space is less than 5% then system performance degrades.
# * If at least 5% disk space is available, then system performance is unaffected.

# The formula to calculate the percentage free space is:
# percent free = 100 * (total disk space - amount used ) / total disk space

# Write and test a Python program which will input the total disk space and the amount used. The program should then
# * check if the amount used exceeds the total disk space; if it does, then a message should be displayed indicating that the input data is invalid;
# * otherwise calculate and display the percentage of free space to 1 decimal place. It should then determine and display a message based on the amount of free space.

# Input | Result
#-------|-----------------------------------
# 500   | Enter total space: 500
# 4500  | Enter amount used: 4500
#       | Invalid input
#-------|-----------------------------------
# 500   | Enter total space: 500
# 500   | Enter amount used: 500
#       | The percentage free space is 0.0%
#       | Warning: system full
#-------|-----------------------------------
# 500   | Enter total space: 500
# 489   | Enter amount used: 489
#       | The percentage free space is 2.2%
#       | Warning, low disk space
#-------|-----------------------------------
# 500   | Enter total space: 500
# 350   | Enter amount used: 350
#       | The percentage free space is 30.0%
#       | System has sufficient disk space


total_disk_space = 500
amount_used = 350

# total_disk_space = int(input("Enter total space: "))
# amount_used = int(input("Enter amount used: "))
percent_free = 0.0
message = ""

if amount_used > total_disk_space:
    print("Invalid input")
else:
    percent_free = 100 * ((total_disk_space - amount_used) / total_disk_space)
    if percent_free == 0:
        message = "Warning: system full"
    elif percent_free < 5:
        message = "Warning, low disk space"
    else:
        message = "System has sufficient disk space"
    
    print(f"The percentage free space is {percent_free:.1f}%")
    print(message)

