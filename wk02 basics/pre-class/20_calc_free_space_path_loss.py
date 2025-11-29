# Example Program: Calculate Free Space Path Loss
#  In telecommunication, free-space path loss (FSPL) is the loss in 
# signal strength of an electromagnetic wave that would result from a 
# line-of-sight path through free space (usually air).

from math import pi, log10

# Input distance
distance = float(input("Enter the distance from the tranmitter in meters: "))

# Input frequency
frequency = float(input("Enter the signal frequency in Hertz: "))

# Calculate the free space path loss
fspl = (4 * pi * distance * frequency / 300000000) ** 2
# Print the free space path loss
print(f"The Free Space Path Loss is {fspl:.3f}")

# Calculate the free space path loss in decibels
fspldb = 20 * log10(distance) + 20 * log10(frequency) - 147.55
# Print the free space path loss in decibels
print(f"The Free Space Path Loss in Decibels is {fspldb:.3f} dB")