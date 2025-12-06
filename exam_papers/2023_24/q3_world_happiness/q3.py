# Q3a(i)
import matplotlib.pyplot as plt
# Q3a(ii)
try:
    # with open("happiness.csv") as data_file:
    with open("exam_papers\\2023_24\\q3_world_happiness\\happiness.csv") as data_file:
        # Q3b
        region_freq_dict = {}
        region_total_dict = {}
        happiness_list = []
        economy_list = []

        # Q3c(i)
        _ = data_file.readline() # headers
        for line in data_file:
            try:
                country, region, happiness, economy, = line.strip().split(",")
                region_freq_dict[region] = region_freq_dict.get(region, 0) + 1
                region_total_dict[region] = region_total_dict.get(region, 0) + float(happiness)
                happiness_list.append(float(happiness))
                economy_list.append(float(economy))
            except ValueError:
                print(f"Line is not in suitable format {line}")

        # Q3c(ii)
        region_average_dict = { region: region_total_dict[region] / region_freq_dict[region] for region in sorted(region_freq_dict)}

        # Q3d(i)
        fig, ax = plt.subplots(3,1, figsize=(10,30))
        # Q3d(ii)
        fig.suptitle("Happiness Index")

        # Q3e
        ax[0].set_title("Histogram of Happiness Scores")
        ax[0].set_xlabel("Happiness Score")
        ax[0].set_ylabel("Frequency")
        intervals = range(0,10)
        ax[0].set_xticks(intervals)
        ax[0].hist(happiness_list, ec="black", bins=intervals)
        
        ax[1].set_title("Scatter plot of Happiness vs Economy")
        ax[1].set_xlabel("Economy Score")
        ax[1].set_ylabel("Happiness Score")
        ax[1].scatter(economy_list, happiness_list, marker=".")
        
        ax[2].set_title("Happiness by Region")
        ax[2].set_xlabel("Happiness Score (Average by Country)")
        ax[2].set_ylabel("Region")
        ax[2].barh(list(region_average_dict.keys()), region_average_dict.values())

        plt.show()
except FileNotFoundError:
    print("Unable to open the file happiness.csv")
except:
    print("other issue")
