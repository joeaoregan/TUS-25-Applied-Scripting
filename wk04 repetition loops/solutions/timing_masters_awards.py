# Timing the Masters Award Versions
from time import perf_counter # ns = nanoseconds
from random import randint
num_sims = 1000000

# Version 1: Nested If (check valid first)
start = perf_counter()
for i in range(num_sims):
    mark = randint(-5,105)
    if 0 <= mark <= 100:
        if mark >= 70:    
            print("First Class Honours")
        elif mark >= 50:
            print("Second Class Honours")
        elif mark >= 40:
            print("Pass")
        else:
            print("No Award")
    else:
        print("Invalid Mark")
end = perf_counter()
elapsed_nested = end - start

# Version 2: If-elif-else (check invalid first)
start = perf_counter()
for i in range(num_sims):
    mark = randint(-5,105)
    if not 0 <= mark <= 100: 
        print("Invalid Mark")
    elif mark >= 70:    
        print("First Class Honours")
    elif mark >= 50:
            print("Second Class Honours")
    elif mark >= 40:
        print("Pass")
    else:
        print("No Award")
end = perf_counter()
elapsed_if_elif = end - start
    
# Version 3: match-case
start = perf_counter()
for i in range(num_sims):
    mark = randint(-5,105)
    match mark:
        case mark if not 0 <= mark <= 100:
            print("Invalid mark")
        case mark if mark >= 70:    
            print("First Class Honours")
        case mark if mark >= 50:
                print("Second Class Honours")
        case mark if mark >= 40:
            print("Pass")
        case _:
            print("No Award")
end = perf_counter()
elapsed_match_case = end - start

print("Results")
print(f"{elapsed_nested=:.3f} seconds")
print(f"{elapsed_if_elif=:.3f} seconds")
print(f"{elapsed_match_case=:.3f} seconds")