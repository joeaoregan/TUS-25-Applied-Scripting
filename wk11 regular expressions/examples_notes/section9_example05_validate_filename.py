# Program to validate a filename
# Example of regular expression with an escaped meta-character \.
import re

# keep going until the user watchs to stop
while True:
	filename = input("Enter a filename or q to quit: ")
	
	if filename == "q":
		break # break from the loop

	# apply the regular expression
	match = re.fullmatch(r"\w+.\w+", filename)

	# check if it matches
	if match:
		print("Valid filename")
	else:
		print("Not a valid filename")

