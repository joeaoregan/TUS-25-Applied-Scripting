days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']

for i,day in enumerate(days):
    print(f"Day {i} is {day}")

print()

# start
for i,day in enumerate(days,start=1):
    print(f"Day {i} is {day}")

print()

webhits = [859, 1257, 724, 1003, 982, 672, 598]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fr', 'Sat', 'Sun']
print(f"{'Day':<4}{'Hits':>6}") # Header
for i,hits in enumerate(webhits):
    print(f"{days[i]:<4}{hits:>6}")