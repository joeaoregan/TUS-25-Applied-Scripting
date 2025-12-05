from random import shuffle

def is_valid_allocation(allocation):
    for key in allocation:
        # print(f"{key} : {allocation.get(key)}")
        if key == allocation.get(key):
            return False
    return True

def allocate_secret_santa(names):
    # shuffle(names.copy())
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

# Test Cases
print("\nTest Cases")
	
# Valid allocation dictionary, 3 names
allocation = {'Curly': 'Mo', 'Larry': 'Curly', 'Mo': 'Larry'}
print(f"{is_valid_allocation(allocation)=}") # True

# Invalid allocation dictionary, 3 names
allocation = {'Curly': 'Curly', 'Larry': 'Mo', 'Mo': 'Larry'}
print(f"{is_valid_allocation(allocation)=}") # False

# Valid allocation dictionary, 4 names
allocation = {'Ashok': 'Carla', 'Bláthnaid': 'Dawid', 'Carla': 'Bláthnaid', 'Dawid': 'Ashok'}
print(f"{is_valid_allocation(allocation)=}") # True

# Invalid allocation dictionary, 4 names
allocation = {'Ashok': 'Dawid', 'Bláthnaid': 'Bláthnaid', 'Carla': 'Ashok', 'Dawid': 'Carla'}
print(f"{is_valid_allocation(allocation)=}") # False

# Valid allocation dictionary, 5 names
allocation = {'Chico': 'Harpo', 'Groucho': 'Zeppo', 'Gummo': 'Groucho', 'Harpo': 'Gummo', 'Zeppo': 'Chico'}
print(f"{is_valid_allocation(allocation)=}") # True

# Invalid allocation dictionary, 5 names
allocation = {'Chico': 'Chico', 'Groucho': 'Gummo', 'Gummo': 'Harpo', 'Harpo': 'Groucho', 'Zeppo': 'Zeppo'}
print(f"{is_valid_allocation(allocation)=}") # False

# 3 names, Allocation 1
from random import seed; seed(1)
names = ['Curly', 'Larry', 'Moe']
my_allocation =  {'Larry': 'Moe', 'Moe': 'Curly', 'Curly': 'Larry'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")

# 3 names, Allocation 2
from random import seed; seed(10)
names = ['Curly', 'Larry', 'Moe']
my_allocation =  {'Larry': 'Curly', 'Curly': 'Moe', 'Moe': 'Larry'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")

# 4 names, Allocation 1
from random import seed; seed(20)
names = ['Ashok', 'Bláthnaid', 'Carla', 'Dawid']
my_allocation =  {'Carla': 'Ashok', 'Ashok': 'Dawid', 'Dawid': 'Bláthnaid', 'Bláthnaid': 'Carla'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")

# 4 names, Allocation 2
from random import seed; seed(30)
names = ['Ashok', 'Bláthnaid', 'Carla', 'Dawid']
my_allocation =  {'Bláthnaid': 'Ashok', 'Ashok': 'Dawid', 'Dawid': 'Carla', 'Carla': 'Bláthnaid'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")

# 5 names, Allocation 1
from random import seed; seed(40)
names = ['Chico', 'Harpo', 'Gummo', 'Groucho', 'Zeppo']
my_allocation =  {'Gummo': 'Harpo', 'Harpo': 'Zeppo', 'Zeppo': 'Chico', 'Chico': 'Groucho', 'Groucho': 'Gummo'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")

# 5 names, Allocation 2
from random import seed; seed(50)
names = ['Chico', 'Harpo', 'Gummo', 'Groucho', 'Zeppo']
my_allocation =  {'Zeppo': 'Chico', 'Chico': 'Harpo', 'Harpo': 'Gummo', 'Gummo': 'Groucho', 'Groucho': 'Zeppo'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")