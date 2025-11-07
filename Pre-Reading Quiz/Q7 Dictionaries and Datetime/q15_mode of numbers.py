# Question 15
# Which of the following will provide the mode of the numbers list (the most common number)? (Assume there's only a single mode)

numbers = [6, 1, 5, 3, 1, 2, 6, 6, 3, 6]
distinct_numbers = set(numbers)

number_frequencies = { number:numbers.count(number) for number in distinct_numbers }
print(number_frequencies)

# a
# print(max(number_frequencies.values()))
# print("a:", number_frequencies.values())

# b
print(max(number_frequencies,key=number_frequencies.get)) # Correct
# print("b:",number_frequencies,key=number_frequencies.get)
# print(min(number_frequencies,key=number_frequencies.get))

# c
print(max(number_frequencies))
# print("c:", number_frequencies)
# print(min(number_frequencies))

# d
# print(max(number_frequencies.keys())) 
# print(number_frequencies.keys())
# print(type(number_frequencies.keys()))
# print(min(number_frequencies.keys())) 
