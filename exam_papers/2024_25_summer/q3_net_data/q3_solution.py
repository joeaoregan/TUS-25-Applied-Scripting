import matplotlib.pyplot as plt

events_dict = {}
duration_list = []
protocol_dict = {}
sPackets_list = []
rPackets_list = []
event_type_dict = {}

filename = "exam_papers/2024_25_summer/q3_net_data/net_data.csv"

try:
    # with open("net_data.csv") as data_file:
    # with open("exam_papers/2024_25_summer/q3_net_data/net_data.csv") as data_file:
    with open(filename) as data_file: # 3(a)(i)
        _ = data_file.readline() # headers


        for line in data_file:
            try:
                minute, protocol, duration, sPackets, rPackets, event_type = line.strip().split(",")

                events_dict[minute] = events_dict.get(minute, 0) + 1
                duration_list.append(float(duration))
                sPackets_list.append(float(sPackets))
                rPackets_list.append(float(rPackets))
                protocol_dict[protocol] = protocol_dict.get(protocol,0) + 1
                event_type_dict[event_type] = event_type_dict.get(event_type,0) + 1
            except ValueError:
                print(f"Unable to split {line.strip()}, skipping")
        
        # # Q3c
        fig, ax = plt.subplots(2,3, figsize=(15,12))
        fig.suptitle("Network Data")

        ax[0,0].set_title("Events")
        ax[0,0].set_xlabel("Minute")
        ax[0,0].set_ylabel("Number of Events")
        ax[0,0].set_xticks(range(0,10))
        ax[0,0].plot(events_dict.values())

        bins = [i/10 for i in range(6)]
        ax[0,1].set_title("Event Duration")
        ax[0,1].set_xlabel("Time in Seconds")
        ax[0,1].set_ylabel("Frequency")
        ax[0,1].set_xticks(bins)
        ax[0,1].hist(duration_list,bins,edgecolor="black")

        ax[0,2].set_title("Event Type")
        ax[0,2].pie(event_type_dict.values(), labels=event_type_dict.keys(), autopct="%.0f%%")
        
        ax[1,0].set_title("Protocols")
        ax[1,0].set_ylabel("Frequency")
        ax[1,0].set_xlabel("Protocol")
        ax[1,0].bar(protocol_dict.keys(), protocol_dict.values())

        ax[1,1].set_title("Packets: Box Plots")
        ax[1,1].set_ylabel("Number of Packets")
        ax[1,1].boxplot([sPackets_list,rPackets_list], labels=["Sent","Recieved"],
                        showmeans=True, meanline=True)
        
        ax[1,2].set_title("Packets: Scatter Plot")
        ax[1,2].set_xlabel("Sent")
        ax[1,2].set_ylabel("Recieved")
        ax[1,2].scatter(x=sPackets_list,y=rPackets_list,s=2)

        plt.show()
        
except:
    print("Unable to open file net_data.csv")