from time import perf_counter


def time_allocation_function(allocator, names, reps=1000):
    start = perf_counter()
    for _ in range(reps):
        allocator(names)
    end = perf_counter()
    return end - start