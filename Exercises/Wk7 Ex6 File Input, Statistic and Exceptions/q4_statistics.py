# A00258304

filename = input("Enter the filename: ")

electors_list = []

try:
    with open(filename) as file:
        headings = file.readline()

        for line in file:
            try:
                state, population, electors = line.strip().split(",")
            except ValueError:
                print(f"Line has invalid format: {line.strip()}")
                continue

            try:
                electors_list.append(int(electors))
            except ValueError:
                print(f"Invalid or missing number of electors for {state}")

    # Calulate mean
    mean = float(sum(electors_list)) / len(electors_list)

    # Calculate median
    if len(electors_list) % 2 == 1:
        median = sorted(electors_list)[len(electors_list) // 2]
    else:
        mid_index = len(electors_list) // 2
        median = (sorted(electors_list)[mid_index - 1] + sorted(electors_list)[mid_index]) / 2

    # Calculate mode
    values = sorted(set(electors_list))
    frequencies = [ electors_list.count(value) for value in values]
    max_frequency = max(frequencies)
    mode_index = frequencies.index(max_frequency)
    mode = values[mode_index]

    print(f"Mean electors per State/District: {mean:.1f}")
    print(f"Median electors per State/District: {median:.1f}")
    print(f"Mode of electors per State/District: {mode}")
except FileNotFoundError:
    print(f"Unable to open the file {filename}")
