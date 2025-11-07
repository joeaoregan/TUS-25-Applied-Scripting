# A00258304

filename = input("Enter the filename: ")

with open(filename) as file:
    headings = file.readline()

    number_of_counties = 0
    total_number_of_finals = 0
    last_final = 0
    current_champions = ""
    most_wins = 0
    most_successful_team = ""
    successful_team_last_final = ""
    best_win_ratio = 0.0
    best_win_ratio_team = ""
    best_win_ratio_last_final = ""


    for line in file:
        number_of_counties += 1
        team, wins, last_final_won, runners_up, last_final_lost, total_final_appearances = line.strip().split(",")

        # print(f"Team: {team:<9} Wins: {wins:>2} Runners-up: {runners_up:>2} Last Final Won: {last_final_won:>4} Last Final Lost: {last_final_lost}, Total Final Appearances: {total_final_appearances:>2}")
        total_number_of_finals += int(wins)

        # Current Chapmpions
        if last_final_won.isnumeric():
            if int(last_final_won) > last_final:
                last_final = int(last_final_won)
                current_champions = team

        # Most Wins
        if int(wins) > most_wins:
            most_wins = int(wins)
            most_successful_team = team
            successful_team_last_final = last_final_won

        # Highest Win Ratio
        # win_ratio = (int(wins) / int(total_final_appearances)) * 100
        win_ratio = int((100 * int(wins)) / int(total_final_appearances))
        if win_ratio > best_win_ratio:
            best_win_ratio = win_ratio
            best_win_ratio_team = team
            best_win_ratio_last_final = last_final_won
            

print(f"Number of Counties: {number_of_counties}")
print(f"Total number of All-Ireland finals: {total_number_of_finals}")
print(f"Average number of wins per county: {total_number_of_finals / number_of_counties:.1f}")
print(f"Current champions (winners in {last_final}): {current_champions}")
print(f"Most wins: {most_successful_team} with {most_wins} wins, most recently in {successful_team_last_final}")
print(f"Highest Win Ratio: {best_win_ratio_team} with {best_win_ratio}%, most recently in {best_win_ratio_last_final}")