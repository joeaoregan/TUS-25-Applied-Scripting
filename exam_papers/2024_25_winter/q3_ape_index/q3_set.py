# Q3a(i)
import matplotlib.pyplot as plt
# Q3a(ii)
try:
    # with open("climbing.csv") as data_file:
    with open("exam_papers\\2024_25_winter\\q3_ape_index\\climbing.csv") as data_file:
        # Q3b
        ages_list = []
        height_list = []
        armspans_list = []
        apeindex_list = []

        # Q3c
        _ = data_file.readline() # headings
        for line in data_file:
            try:
                age, height, armspan = line.split(",")
                ages_list.append(int(age))
                height_list.append(float(height))
                armspans_list.append(float(armspan))
                apeindex_list.append(float(armspan)/float(height))
            except ValueError:
                print(f"Line is not suitable for format: {line}")

        # Q3d(i)
        fig, ax = plt.subplots(3, figsize=(10,30))
        # Q3d(ii)
        fig.suptitle("Visualisations fo Rock Climber Data")

        # Q3e
        ax[0].set(title="Scatter Plot Arm Span vs Height", ylabel="Arm Span", xlabel="Height")
        ax[0].scatter(x=height_list, y=armspans_list, s=5)

        ax[1].set(title="Box Plot of Ape Index", ylabel="Ape Index")
        ax[1].boxplot(apeindex_list)

        ax[2].set(title="Histogram of Ages", ylabel="Frequency", xlabel="Age")
        bins = range(0, max(ages_list)+10,10)
        ax[2].hist(ages_list,bins,ec="black")
        
except FileNotFoundError:
    print(f"Unable to open the file climbing.csv")


# show
plt.show()
# fig.savefig('exam_papers\\2024_25_winter\\q3_ape_index\\q3_plots.png', bbox_inches='tight')