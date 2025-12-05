# Q3a(i)
import matplotlib.pyplot as plt
# Q3a(ii)
try:
    # with open("hosting_performance.csv") as data_file:
    with open("exam_papers\\2023_24_repeat\\q3_hosting_data\\hosting_data.csv") as data_file:
        # Q3b
        total_list = []
        dns_list = []
        connect_list = []
        os_freq_dict = {}

        # Q3c
        _ = data_file.readline() # headers
        for line in data_file:
            try:
                company, os, dns, connect, total = line.strip().split(",")
                os_freq_dict[os] = os_freq_dict.get(os,0) + 1
                dns_list.append(float(dns))
                connect_list.append(float(connect))
                total_list.append(float(total))
            except ValueError:
                print(f"Line is not in suitable format: {line}")

        # Q3d
        fig, ax = plt.subplots(2,2, figsize=(40,40))
        fig.suptitle("Hosting Performance of Fortune 100 Websites")

        # Q3e
        ax[0,0].set_title("Histogram of Total Times")
        ax[0,0].set_xlabel("Total Time")
        ax[0,0].set_ylabel("Frequency")
        intervals = [x/10 for x in range(0,16)]
        ax[0,0].set_xticks(intervals)
        ax[0,0].set_yticks(range(16))
        ax[0,0].hist(total_list, ec="black", bins=intervals)

        ax[0,1].set_title("Box Plot of Total Times")
        ax[0,1].set_ylabel("Time in Seconds")
        ax[0,1].boxplot(total_list, labels=["Total Time"], showmeans=True, meanline=True)

        ax[1,0].set_title("Scatter plot of DNS Time vs Connect Time")
        ax[1,0].set_xlabel("Connect Time")
        ax[1,0].set_ylabel("DNS Lookup Time")
        ax[1,0].scatter(x=connect_list, y=dns_list, marker=".")
        # print(len(connect_list), len(dns_list))

        ax[1,1].set_title("Operating Systems Share")
        ax[1,1].pie(os_freq_dict.values(), labels=os_freq_dict.keys(), autopct="%.0f%%")

        plt.show()

except FileNotFoundError:
    print("Unable to open the file hosting_performance.csv")