contacts = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}

print(contacts.values())
print(contacts.keys())
print(contacts.items())


results = {'Ailbhe': 5, 'Bláthnaid': 4, 'Joe': 1}

for candidate in sorted(results, key=results.get):
    print(f"{candidate} - {results[candidate]}")

print()

for candidate in sorted(results, key=results.get, reverse=True):
    print(f"{candidate} - {results[candidate]}")


eliminated = ['Ailbhe', 'Bláthnaid', 'Joe']
for round in range(0, len(eliminated),):
    print(f"{round+1:3} {eliminated[round]}")