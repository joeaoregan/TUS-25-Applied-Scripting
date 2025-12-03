
total_space = int(input("Enter total space: "))
amount_used = int(input("Enter amount used: "))

if amount_used > total_space:
    print("Invalid input")
else:
    percent_free = 100 * (total_space - amount_used) / total_space
    print(f"The percentage free space is {percent_free:.1f}%")

    if percent_free == 0.0:
        print("Warning: system full")
    elif percent_free < 30:
        print("Warning, low disk space")
    else:
        print("System has sufficient disk space")