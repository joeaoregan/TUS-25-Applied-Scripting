# Question 14
# A variable numbers contains a list of integers.
# The following code uses a set to generate a list of the distinct numbers in the numbers list:
# distinct_numbers = set(numbers))


# Which of the following dictionary comprehensions will create a dictionary containing the frequencies of each distinct number?
# Try it with the following:
numbers = [6, 1, 5, 3, 1, 2, 6, 6, 3, 6]
distinct_numbers = set(numbers)

# number_frequencies = { number:distinct_numbers.count(number) for number in numbers } # AttributeError: 'set' object has no attribute 'count' 
# print(number_frequencies)

# number_frequencies = { number:number.count(numbers) for number in distinct_numbers } # AttributeError: 'int' object has no attribute 'count'
# print(number_frequencies)

number_frequencies = { number:numbers.count(distinct_numbers) for number in numbers }
print(number_frequencies) # wrong output

number_frequencies = { number:numbers.count(number) for number in distinct_numbers }
print(number_frequencies) # correct output: {1: 2, 2: 1, 3: 2, 5: 1, 6: 4}