# Example: Using zip() for Parallel Lists
webhits = [859, 1257, 724, 1003, 982, 672, 598]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
print(f"{'Day':<4}{'Hits':>6}") # column headers
for day, hits in zip(days, webhits):
    print(f"{day:<4}{hits:>6}")