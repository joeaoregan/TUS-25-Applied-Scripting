# Example: Calculate the median of a list of numbers
sorted_numbers = [1,3,3,6,7,8,9]
print(len(sorted_numbers))

mid_index = int(len(sorted_numbers)/2)
print(f"{mid_index}, {sorted_numbers[mid_index]}")


sorted_numbers = [1,2,3,4,5,6,8,9]
print(len(sorted_numbers))

mid_index = int(len(sorted_numbers)/2)
print(f"{mid_index=}")

print(f"{sorted_numbers[mid_index]=} {sorted_numbers[mid_index+1]=}")
print((sorted_numbers[mid_index] + sorted_numbers[mid_index+1]) / 2)