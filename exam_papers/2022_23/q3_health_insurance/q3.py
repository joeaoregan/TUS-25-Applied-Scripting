# 3a
import matplotlib.pyplot as plt
# 3b
try:
    # with open("insurance.csv") as data_file:
    with open("exam_papers\\2022_23\\q3_health_insurance\\insurance.csv") as data_file:
        # 3c
        age_list = []
        charges_list = []
        smokers_dict = {}
        region_dict = {}

        # Q3d
        _ = data_file.readline() # headers
        for line in data_file:
            try:
                age, smoker, region, charges = line.strip().split(",")

                try:
                    age_list.append(int(age))
                except ValueError:
                    print("age can not be converted")

                try:
                    charges_list.append(float(charges))
                except ValueError:
                    print("charge can not be converted")

                smokers_dict[smoker] = smokers_dict.get(smoker, 0) + 1
                region_dict[region] = region_dict.get(region, 0) + 1
            except ValueError:
                print(f"Bad line {line}")
        
        fig, ax = plt.subplots(2,2, figsize=(12,12))
        plt.suptitle("Visualisation of Insurance Customer Data")

        ax[0,0].set_title("Histogram of Customer Ages")
        ax[0,0].set_xlabel("Age")
        ax[0,0].set_ylabel("Number of Customers")
        bins = range(0, max(age_list) +10, 10)
        ax[0,0].set_xticks(bins)
        ax[0,0].hist(age_list, bins, ec="black")
        
        ax[0,1].set_title("Box Plot of Charges")
        ax[0,1].set_ylabel("Charges ($)")
        ax[0,1].boxplot(charges_list, showmeans=True, meanline=True)
        
        ax[1,0].set_title("Bar Chart of Smokers/Non-Smokers")
        ax[1,0].set_xlabel("Number of Customers")
        ax[1,0].set_ylabel("Smokers")
        ypos = (0,1)
        ax[1,0].set_yticks(ypos)
        ax[1,0].set_yticklabels(smokers_dict.keys())
        ax[1,0].barh(ypos, smokers_dict.values())

        
        ax[1,1].set_title("Pie Chart of Regions")
        ax[1,1].pie(region_dict.values(), labels=region_dict.keys(), autopct="%.0f%%")

        plt.show()
except FileNotFoundError:
    print("File not found: insurance.csv")
