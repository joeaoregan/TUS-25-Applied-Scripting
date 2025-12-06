import matplotlib.pyplot as plt

try:
    # with open("TOP500_2021.csv") as data_file:
    with open("exam_papers\\2021_22\\q3_top500_supercomputers\\TOP500_2021.csv") as data_file:
        year_freqs = {}
        area_freqs = {}
        total_cores_list = []
        rmax_values_list = []

        segments_list = []

        _ = data_file.readline() # headers
        for line in data_file:
            try:
                name, year, area, total_cores, rmax = line.strip().split(",")

                try:
                    total_cores_list.append(int(total_cores))
                except ValueError:
                    print("total_cores values error")

                try:
                    rmax_values_list.append(float(rmax))
                except ValueError:
                    print("rmax value error")

                year_freqs[year] = year_freqs.get(year, 0) + 1
                area_freqs[area] = area_freqs.get(area, 0) + 1

                segments_list.append(area)
            except ValueError:
                print(f"line error: {line}")

        fig, ax = plt.subplots(3,1, figsize=(6,20))
        plt.suptitle("Top 500 Supercomputers")

        ax[0].set_title("Scatter plot of Rmax vs Total Cores")
        ax[0].set_xlabel("Total Cores")
        ax[0].set_ylabel("Rmax")
        ax[0].scatter(total_cores_list, rmax_values_list, marker=".")

        ax[1].set_title("Pie Chart of Segments")
        # ax[1].pie(area_freqs.values(), labels=area_freqs.keys(), autopct="%.0f%%")
        unique_segments = list(set(area_freqs))
        segment_freqs_dict = {segment:segments_list.count(segment) for segment in unique_segments}
        ax[1].pie(segment_freqs_dict.values(), labels=segment_freqs_dict.keys(), autopct="%.0f%%")

        ax[2].set_title("Bar Chart of Installation by Year")
        ax[2].set_xlabel("Number of Supercomputers")
        ax[2].set_ylabel("Year")
        ypos = list(range(len(year_freqs)))
        ax[2].set_yticks(ypos)
        ax[2].set_yticklabels(year_freqs.keys())        
        ax[2].barh(ypos, year_freqs.values())

        plt.show()
except FileNotFoundError:
    print("Can't find csv file")