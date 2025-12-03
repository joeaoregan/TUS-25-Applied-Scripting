from time import perf_counter
from q1_a_imo_number import check_imo_test_digit

start = perf_counter()
check_imo_test_digit("9074729")
end = perf_counter()
elapsed_time = end - start
print(f"Elapsed time: {elapsed_time:.6f} seconds")
print(f"Elapsed time: {elapsed_time:.7f} seconds")
print(f"Elapsed time: {elapsed_time:.8f} seconds")