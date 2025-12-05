import sys

results = {}

# Q2a
while True:
    candidate = input("Enter candidate's name or q to continue: ")
    if candidate == 'q': break
    elif candidate in results:
        print("Candidate exists")
    else:
        results[candidate] = 0

if len(results) == 0:
    print("No candidates entered, quitting")
    sys.exit()

# Q2b
round = 1
eliminated = []

while True:
    print(f"\nRound: {round}")
    for candidate in sorted(results):
        results[candidate] = int(input(f"Enter number of votes for {candidate}: "))

    print(f"Number of Candidates: {len(results)}")
    total_votes = sum(results.values())
    print(f"Total Votes: {total_votes}")

    for candidate in sorted(results, key=results.get, reverse=True):
        print(f"{candidate}: {results[candidate]} {results[candidate] / total_votes:.1%}")

    leader = max(results, key=results.get)
    print(f"Candidate with most votes: {leader}")

    if results[leader] / total_votes > 0.5: 
        break
    else:
        loser = min(results, key=results.get)
        print(f"Eliminating candidate with least votes: {loser}")
        del results[loser]
        eliminated.append(loser)
        round += 1

# Q2c
print(f"\nWinner {leader}")
if len(eliminated) > 0:
    print("Eliminated Candidates")
    print("Round Candidate")
    for round in range(0, len(eliminated)):
        print(f"{round+1:3} {eliminated[round]}")