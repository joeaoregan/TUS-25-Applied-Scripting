numbers = [3,9,5,6,6,9,3,6]
mode = numbers[0]
max_freq = numbers.count(mode)
print(f"{mode=} {max_freq=}")

for num in numbers[1:]:
    count = numbers.count(num)
    print(f"{num=} {count=}")
    if count > max_count:
        max_count = count
        mode = num
        print(f"New mode: {mode=} {max_count=}")