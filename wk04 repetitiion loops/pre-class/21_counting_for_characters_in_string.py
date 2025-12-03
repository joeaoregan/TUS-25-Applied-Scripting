# Example Program: Display each character and its index in a string

message = input("Enter message: ")

for i in range(len(message)):
    print(f"{i=:>2} {message[i]=}")