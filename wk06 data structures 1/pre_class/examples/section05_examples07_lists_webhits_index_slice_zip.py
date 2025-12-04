# Program to analyse web hits per day
# Example of  list indexing, slicing and zip

# Days of the week and corresponding website hits
days     = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
webhits  = [859, 1257, 724, 1003, 982, 672, 598]

# Indexing
print(f"Hits on {days[0]}: {webhits[0]}")      # First item
print(f"Hits on {days[-1]}: {webhits[-1]}")    # Last item (negative index)

# List slicing
print(f"\nWeekdays hits: {webhits[0:5]}")        # First 5 items
print(f"Weekend hits: {webhits[5:]}")            # Slice from Saturday onward
print(f"First half of week: {webhits[:3]}")      # Defaults start at 0
print(f"Second half of week: {webhits[3:]}")     # Defaults end at len(list)

# Iterating with zip()
print("\nWebsite hits by day:")
for day, hits in zip(days, webhits):
    print(f"{day}: {hits}")

