# Program to calculate amount of data transferred in xferlog log file

# Import the re module
import re

# Open the 'xferlog' file
with open('xferlog') as logfile:
	# Read in the entire contents
	contents = logfile.read()	

	# Use a regex "(\d+) /" to search for the data transfer and return a list of the values
	data_transfers = re.findall(r"(\d+) /", contents)
	
	# the values are stored in the list as strings
	#print(data_transfers)

	# calculate the total of the data transfers
	#total = 0
	#for value in data_transfers:
	#	total += int(value)
	#print("Total data transferred:",total, "bytes")
	
	# turn the values into numbers in one go using a list comprehension
	data_numbers = [ int(value) for value in data_transfers ]

	print("Total data transferred:     ",sum(data_numbers), "bytes")

	# calculate the largest value
	print("Maximum single data transfer: ",max(data_numbers), "bytes")


