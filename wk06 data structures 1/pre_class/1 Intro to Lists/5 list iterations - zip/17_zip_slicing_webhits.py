# Program to analyse web hits per day
# Example of list indexing, slicing and zip

# Days of the week and corresponding website hits
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
webhits = [859, 1257, 724, 1003, 982, 672, 598]

# Indexing
print(f"Hits on {days[0]}: {webhits[0]}")
print(f"Hits on {days[-1]}: {webhits[-1]}")

# List slicing
print(f"\nWeekdays hits: {webhits[0:5]}")
print(f"Weekend hits: {webhits[5:]}")
print(f"First half of week: {webhits[:3]}")
print(f"Second half of week: {webhits[3:]}")

# Iterating with zip()
print("\nWebsite hits by day:")
for day, hits in zip(days, webhits):
    print(f"{day}: {hits}")