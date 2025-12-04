# Example: Calculating the Median using a list slice
sorted_numbers = [1,3,3,6,7,8,9]
mid_index = int(len(sorted_numbers)/2)
median = sum(sorted_numbers[mid_index-1:mid_index+1]) / 2

sorted_numbers = [672, 724, 859, 982, 1003, 1257]
mid_index = int(len(sorted_numbers)/2)
print(mid_index)
print(sorted_numbers[mid_index-1:mid_index+1])

sorted_numbers = [598, 672, 724, 859, 982, 1003, 1257]
print(len(sorted_numbers))
mid_index = int(len(sorted_numbers)/2)
print(mid_index)

lower_half = sorted_numbers[:mid_index]
upper_half = sorted_numbers[mid_index+1:]
print(f"{lower_half=} {upper_half=}")

sorted_numbers = [672, 724, 859, 982, 1003, 1257]
print(len(sorted_numbers))

mid_index = int(len(sorted_numbers)/2)
print(mid_index)

lower_half = sorted_numbers[:mid_index]
upper_half = sorted_numbers[mid_index:]
print(f"{lower_half=} {upper_half=}")
