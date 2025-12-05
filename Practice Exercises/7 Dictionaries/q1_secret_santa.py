from random import shuffle
from random import seed
seed(1)

def is_valid_allocation(allocation):
    for key in allocation:
        print(f"{key} : {allocation.get(key)}")
        if key == allocation.get(key):
            return False
    return True

def allocate_secret_santa(names):
    shuffle(names)
    allocation_dict = {}
    for i,name in enumerate(names):
        if i == len(names)-1:
            break
        
        allocation_dict[name] = names[i+1]
    allocation_dict[names[-1]] = names[0]
    return allocation_dict

allocation = {'Curly': 'Mo', 'Larry': 'Curly', 'Mo': 'Larry'}
allocation2 = {'Curly': 'Curly', 'Larry': 'Mo', 'Mo': 'Larry'}


print(f"{is_valid_allocation(allocation)=}")
print(f"{is_valid_allocation(allocation2)=}")