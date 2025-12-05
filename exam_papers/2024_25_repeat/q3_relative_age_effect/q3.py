# 3a
import matplotlib.pyplot as plt
try:
    # with open("footballer_data.csv") as data_file:
    with open("exam_papers\\2024_25_repeat\\q3_relative_age_effect\\footballer_data.csv") as data_file:
        # 3b
        months_freq_dict = {i:0 for i in range(1,13)}
        quarters_freq_dict = {i:0 for i in range(1,5)}
        games_played_by_quarter_dict = {i:[] for i in range(1,5)}

        # Q3c
        _ = data_file.readline() # headers
        for line in data_file:
            try:
                year, month, day, quarter, games = line.split(",")
                months_freq_dict[int(month)] += 1
                quarters_freq_dict[int(quarter)] +=1
                games_played_by_quarter_dict[int(quarter)].append(int(games))
            except ValueError:
                print(f"Line is not suitable format: {line}")

        # Q3d
        fig, ax = plt.subplots(3, figsize=(10,40))
        fig.suptitle("Relative Age Effect in Football")

        # Q3e
        ax[0].set_title("Players by Birth Month")
        ax[0].set_ylabel("Number of Players")
        ax[0].set_xlabel("Birth Month")
        ax[0].set_xticks(list(months_freq_dict.keys()))
        ax[0].bar(months_freq_dict.keys(), months_freq_dict.values())

        ax[1].set_title("Players by Birth Quarter")
        ax[1].pie(quarters_freq_dict.values(), labels=quarters_freq_dict.keys(), autopct="%.0f%%")

        ax[2].set_title("Games Played by Birth Quarter")
        ax[2].set_ylabel("Games Played")
        ax[2].set_xlabel("Birth Quarter")
        ax[2].boxplot(games_played_by_quarter_dict.values(), games_played_by_quarter_dict.keys())

        plt.show()

except FileNotFoundError:
    print("Unable to open the file footballer_data.csv")
