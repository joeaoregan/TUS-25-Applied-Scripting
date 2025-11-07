# A00258304

filename = input("Enter the filename: ")

with open(filename) as file:
    headings = file.readline()

    teams_list = []
    wins_list = []
    last_win_list = []
    win_percentages_list = []


    for line in file:
        team, wins, last_final_won, runners_up, last_final_lost, total_final_appearances = line.strip().split(",")
        
        teams_list.append(team)
        wins_list.append(int(wins))
        if last_final_won.isnumeric():
            last_win_list.append(int(last_final_won))
        else:
            last_win_list.append(0)

        win_percentages_list.append(int(100 * int(wins) / int(total_final_appearances)))

            

print(f"Number of Counties: {len(teams_list)}")
print(f"Total number of All-Ireland finals: {sum(wins_list)}")
print(f"Average number of wins per county: {(sum(wins_list) / len(teams_list)):.1f}")

current_champions = max(last_win_list)
index_current_champions = last_win_list.index(current_champions)
print(f"Current champions (winners in {max(last_win_list)}): {teams_list[index_current_champions]}")

most_wins = max(wins_list)
index_most_wins = wins_list.index(most_wins)
print(f"Most wins: {teams_list[index_most_wins]} with {most_wins} wins, most recently in {last_win_list[index_most_wins]}")

best_win_ratio = max(win_percentages_list)
index_best_win_ratio = win_percentages_list.index(best_win_ratio)
print(f"Highest Win Ratio: {teams_list[index_best_win_ratio]} with {best_win_ratio}%, most recently in {last_win_list[index_best_win_ratio]}")