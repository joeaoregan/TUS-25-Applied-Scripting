#  Example: Sorting hexadecimal numbers by converting to in
lambda x: int(x, 16)

red_values = ["0xFF", "0x7F", "0x4B", "0x00", "0x84"]
red_values.sort(key=lambda x: int(x, 16))
print(f"{red_values=}")


