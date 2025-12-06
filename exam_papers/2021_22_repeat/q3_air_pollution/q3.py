import matplotlib.pyplot as plt

try:
    # with open("air_pollution.csv") as data_file:
    with open("exam_papers\\2021_22_repeat\\q3_air_pollution\\air_pollution.csv") as data_file:
        pm10_list = []
        pm25_list = []
        # color_pm25_list = []
        # color_pm10_list = []
        color_pm10_list = ["yellow", "red", "orange", "green", "darkred", "darkorange"]
        color_pm25_list = ["yellow", "red", "orange", "green", "darkred", "darkorange"]

        _ = data_file.readline() # headers
        for line in data_file:
            try:
                # city, pm10, pm25, population, color_pm25, color_pm10 = line.strip().split(",")
                city, pm10, pm25, population = line.strip().split(",")

                try:
                    pm10_list.append(float(pm10))
                except ValueError:
                    print("pm10 value error")

                try:
                    pm25_list.append(float(pm25))
                except ValueError:
                    print("pm25 value error")

                # color_pm25_list.append(color_pm25)
                # color_pm10_list.append(color_pm10)

            
            except ValueError:
                print(f"bad line format: {line}")

        fig, ax = plt.subplots(3,1, figsize=(6,18))
        plt.suptitle("Air Pollution")

        ax[0].set_title("Scatter plot of pm25 vs pm10")
        ax[0].set_xlabel("pm10")
        ax[0].set_ylabel("pm25")
        ax[0].scatter(pm10_list, pm25_list, marker=".")

        ax[1].set_title("Pie Chart of pm10 Color Ratings")
        # ax[1].pie(color_pm25_list)
        pm10_colors = list(set(color_pm10_list))
        pm10_color_freqs_dict = { color:color_pm10_list.count(color) for color in pm10_colors }
        pie_chart_colors = pm10_color_freqs_dict.keys()    
        ax[1].pie(pm10_color_freqs_dict.values(),colors=pie_chart_colors, autopct="%.0f%%")

        ax[2].set_title("Bar Chart of pm25 Color Ratings")
        # ax[0].set_xlabel("")
        # ax[0].set_ylabel("")
        pm25_colors = sorted(list(set(color_pm25_list)))
        pm25_color_freqs_dict = { color:color_pm25_list.count(color) for color in pm25_colors }
        # Set the y position for the bars
        ypos = list(range(len(pm25_colors)))
        # set the y ticks
        ax[2].set_yticks(ypos)
        # Set the y-labels
        ax[2].set_yticklabels(pm25_color_freqs_dict.keys())
        # Draw the bar chart
        ax[2].barh(ypos, pm25_color_freqs_dict.values())

        plt.show()

except FileNotFoundError:
    print("file not found: air_pollution.csv")