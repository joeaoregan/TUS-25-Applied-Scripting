# A00258304

# filename = input("Enter the filename: ")
filename = "rajya_sabha_elections_errors.csv"

members_retiring_list = []

try:
    with open(filename) as file:
        headings = file.readline()

        for line in file:
            try:
                state, members_retiring, date_of_retirement = line.strip().split(",")
            except ValueError:
                print(f"Line has invalid format: {line.strip()}")
                continue
                
            try:
                # if members_retiring.isnumeric():
                members_retiring_list.append(int(members_retiring))
            except ValueError:
                print(f"Invalid or missing number of members for {state}")

           

    # mean = sum(members_retiring_list) / len(members_retiring_list)
    mean = float(sum(members_retiring_list)) / len(members_retiring_list)
    # median = sorted(members_retiring_list)[len(members_retiring_list) // 2]
    if len(members_retiring_list) % 2 == 1:
        median = sorted(members_retiring_list)[len(members_retiring_list) // 2]
    else:
        mid_index = len(members_retiring_list) // 2
        median = (sorted(members_retiring_list)[mid_index - 1] + sorted(members_retiring_list)[mid_index]) / 2
    # mode = max(set(members_retiring_list), key=members_retiring_list.count)
    values = sorted(set(members_retiring_list))
    frequencies = [ members_retiring_list.count(value) for value in values]
    max_frequency = max(frequencies)
    mode_index = frequencies.index(max_frequency)
    mode = values[mode_index]

    print(len(members_retiring_list))
    # print(members_retiring_list)
    # print(sum(members_retiring_list))

    print(f"Mean Members Retiring per State: {mean:.1f}")
    print(f"Median Members Retiring per State: {median:.1f}")
    print(f"Mode of Members Retiring per State: {mode}")

except FileNotFoundError:
    print(f"Unable to open the file {filename}")