results = {}

# Q2a
while True:
    candidate = input("Enter candidate's name or q to continue: ")
    if candidate == 'q': break
    elif candidate in results:
        print("Candidate already included")
    else:
        results[candidate] = 0

# Q2b
    for candidate in sorted(results):
        results[candidate] = int(input(f"Enter number of votes for {candidate}: "))

# Q2c
    print(f"\nNumber of Candidates: {len(results)}")
    total_votes = sum(results.values())
    print(f"Total Votes: {total_votes}")

    for candidate in sorted(results, key=results.get, reverse=True):
        print(f"{candidate}: {results[candidate]} ({results[candidate]/total_votes:.1%})")

#Q2d
    leader = max(results, key=results.get)
    print(f"Candidate with most votes: {leader}")

    if results[leader] / total_votes > 0.5:
        print(f"Winner: {leader}")
    else:
        results2 = {}
        del results[leader]
        results2[leader] = 0

        runner_up = max(results, key=results.get)
        results2[runner_up] = 0

        print("\nRun-off")
        for candidate in sorted(results2):
            results2[candidate] = int(input(f"Enter number of votes for {candidate}: "))

        for candidate in sorted(results2, key=results2.get, reverse=True):
            print(f"{candidate}: {results2[candidate]} ({results2[candidate] / total_votes:.1%})")

        winner = max(results2, key=results2.get)
        print(f"Winner {winner}")
