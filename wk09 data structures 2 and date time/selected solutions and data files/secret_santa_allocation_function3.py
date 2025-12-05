from random import choice

def allocate_secret_santa_v3(names):
    while True:
        allocation = {}

        for giver in names:
            #print(f"Starting allocation for {giver=}")
            possible_recipients = names.copy()
            possible_recipients.remove(giver)
            for assigned in allocation.values():
                if assigned in possible_recipients:
                    possible_recipients.remove(assigned) 

            if not possible_recipients: # empty list
                #print("No possible recipients, restart")
                break  # Dead end, retry outer loop

            receiver = choice(possible_recipients)
            allocation[giver] = receiver
            #print(f"{giver} gives to {receiver}")
        else:
            # Only reached if the for-loop completed without break
            return allocation

if __name__ == "__main__":
    # input names as a list, separated by spaces
    names_string = input("Enter the names, separated by spaces: ")  
    names = names_string.split()
    print(f"{allocate_secret_santa_v3(names)=}")
