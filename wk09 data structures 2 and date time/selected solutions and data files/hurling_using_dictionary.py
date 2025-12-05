# Analyse the Data on All-Ireland Hurlijng Finalists
# Source: Wikipedia https://en.wikipedia.org/wiki/All-Ireland_Senior_Hurling_Championship
# Version2: Using a Dictionary (No Exception Handling)

# Create empty dictionary
results = {}

# filename = "hurling_2025.csv" # input("Enter the filename: ")
filename = "./wk09 data structures 2 and date time/selected solutions and data files/hurling_2025.csv" # input("Enter the filename: ")

# Open the file for reading
with open(filename) as data_file:
    # Read in the first line containing the column headings
    _ = data_file.readline()
    # For each subsequent line of the file
    for line in data_file:
        # Split the line into components
        team, wins, last_win, _, _, win_ratio = line.split(",")
        # Insert into dicitonary, converting as necessary
        results[team] = (int(wins), last_win, int(win_ratio.strip("%\n")))

# Determine and display results
print(f"Number of Counties: {len(results)}")
total_finals = sum([value[0] for value in results.values()])
print(f"Total number of All-Ireland finals: {total_finals}")
print(f"Average number of wins per county: {total_finals/len(results):.1f}")

# Current champions
champions = max(results, key=lambda k: int(results[k][1]) if results[k][1].isdigit() else 0)
print(f"Champions in {results[champions][1]}: {champions}")

# To find the county with the most wins, and their most recent win
team_most_wins = max(results, key=lambda k: int(results[k][0]))
print(f"Most wins: {team_most_wins} with {results[team_most_wins][0]} wins, most recently in {results[team_most_wins][1]}")

# Find the county with the highest percentage of final wins
winningest_team = max(results, key=lambda k: int(results[k][2]))
print(f"Highest Win Ratio: {winningest_team} with {results[winningest_team][2]}%, most recently in {results[winningest_team][1]}")

