# P56: Nesting Lists and Tuples

nested_list = [[1,2],[3,4]]
nested_tuple = ((1,2),(3,4))
list_of_tuples = [(1,2),(3,4)]
tuple_of_lists = ([1,2],[3,4])
mixed_nest1 = [(1,2),[3,4]]
mixed_nest2 = ((1,2),[3.4])

# tuple_of_lists[0] = [9,9] # TypeError: 'tuple' object does not support item assignment

tuple_of_lists[0][0] = 99 # change item in inner list
tuple_of_lists[1].append(5) # add item to inner list
print(tuple_of_lists)