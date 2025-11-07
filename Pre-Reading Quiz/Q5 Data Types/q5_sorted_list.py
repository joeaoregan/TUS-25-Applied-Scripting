my_numbers = [2, 1, 7, 3, 5, 4]

print(my_numbers)

# a.
# my_numbers.sorted() # AttributeError: 'list' object has no attribute 'sorted'. Did you mean: 'sort'?

# b.
sorted_my_numbers = sorted(my_numbers)

# c.
# sort(my_numbers) # NameError: name 'sort' is not definted. Did you mean: 'sorted'?

# d.
# my_numbers.sort()
print(my_numbers)
print(sorted_my_numbers)