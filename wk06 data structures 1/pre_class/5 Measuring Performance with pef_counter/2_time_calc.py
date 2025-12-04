from time import perf_counter
from random import randint

def time_calc_mode(mode_function, reps, list_size, min_value, max_value):
    start = perf_counter() # start the timer

    # Run the simulation a specified number of times
    for i in range(reps):
        numbers = [randint(min_value, max_value) for i in range(list_size)]
        mode_function(numbers)

    end = perf_counter() # stop the timer

    return end - start


if __name__ == "__main__":
    num_sims = 100000
    list_size = 50
    min_value = 0
    max_value = 10

    print("Timing calc_model")
    duration1 = time_calc_mode(calc_mode1, num_sims, list_size, min_value, max_value)
    print(f"Time taken: {duration1:.3f} seconds {num_sims} repitions")

    print()
    print("Timing calc_mode2")
    duration2 = time_calc_mode(calc_mode2, num_sims, list_size, min_value, max_value)
    print(f"Time taken: {duration2:.3f} seconds {num_sims} repitions")