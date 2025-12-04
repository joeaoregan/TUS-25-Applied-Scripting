# The program should:
# Create an empty list for the marks
marks = []
# Repeat while the length of the list is less than 6:
while (len(marks) < 6):
#     Input the mark as an integer
    mark = int(input("Enter the mark: "))
#     If the mark is between 0 and 100, inclusive:
#         Add the mark to the list
    if 0 <= mark <= 100:
        marks.append(mark)
#     Otherwise:
#         Display the message "Invalid mark"
    else:
        print(f"Invalid mark: {mark}")
# Display the number of valid marks (the number of values in the list)
print(f"Number of marks: {len(marks)}")
# Display the average mark to the nearest integer
print(f"Average mark: {sum(marks) / len(marks):.0f}")
# Display the highest mark
print(f"Highest mark: {max(marks)}")
# Display the lowest mark
print(f"Lowest mark: {min(marks)}")