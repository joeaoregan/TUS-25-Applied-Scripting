import matplotlib.pyplot as plt
try:
    # with open("titanic.csv") as data_file:
    with open("exam_papers\\2022_23_repeat\\q3_titanic\\titanic.csv") as data_file:

        age_list = []
        fares_list = []
        survived_dict = {}
        pclass_dict = {}

        _ = data_file.readline() # header
        for line in data_file:
            try:
                age, fare, pclass, survived = line.strip().split(",")
                
                try:
                    age_list.append(int(age))
                except ValueError:
                    print(f"Unable to convert age value {age}")

                try:
                    fares_list.append(float(fare))
                except ValueError:
                    print(f"Unable to convert fare value {fare}")

                survived_dict[survived] = survived_dict.get(survived,0) + 1
                pclass_dict[pclass] = pclass_dict.get(pclass,0) + 1
            except ValueError:
                print(f"Line not suitable: {line}")
    
        fig, ax = plt.subplots(2,2, figsize=(12,12))
        plt.suptitle("Visualisation of Titanic Passenger Data")

        ax[0,0].set_title("Histogram of Passenger Ages")
        ax[0,0].set_xlabel("Age")
        ax[0,0].set_ylabel("Number of Passengers")
        bins = range(0, max(age_list) +10, 10)
        ax[0,0].set_xticks(bins)
        ax[0,0].hist(age_list, bins, ec="black")
        
        ax[0,1].set_title("Box Plot of Ticket Fares")
        ax[0,1].set_xlabel("")
        ax[0,1].set_ylabel("Ticket Fare (£)")
        ax[0,1].boxplot(fares_list, showmeans=True, meanline=True)
        
        ax[1,0].set_title("Bar Chart of Survival")
        ax[1,0].set_xlabel("Number of Passengers")
        ax[1,0].set_ylabel("Survived")
        ypos = (0,1)
        ax[1,0].set_yticks(ypos)
        ax[1,0].set_yticklabels(survived_dict.keys())
        ax[1,0].barh(ypos, survived_dict.values())
        
        ax[1,1].set_title("Pie Chart of Passenger Class")
        ax[1,1].pie(pclass_dict.values(), labels=pclass_dict.keys(), autopct="%.0f%%")

        plt.show()
except FileNotFoundError:
    print("File not found: titanic.csv")