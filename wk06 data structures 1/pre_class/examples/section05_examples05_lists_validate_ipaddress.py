# Purpose: to validate an IP address
# Example of: spliting a string into a list, for loop

# input the ip address
ip = input("Enter the IP address: ")

# Split into octects
octets_list = ip.split(".")

# check the number of octets
if len(octets_list) != 4:
    print("Invalid IPv4 address")

# it has 4 octets, so it's ok (so far)
else:
    # check each octet number
    for octet in octets_list:
        # is it in the correct range
        if not 0 <= int(octet) <= 255:
            # if not, it"s invalid
            print(f"Invalid octet {octet} in IP address")
            break
    else:
        # the 4 octet numbers are valid
        print (f"{ip} is a valid IP address")


