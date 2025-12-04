data_points = [[0,0], [1,3], [2,5], [3,6], [4,8]]
print(data_points[2])

point = data_points[2]
print(point[0])
print(point[1])

print(data_points[2][0])
print(data_points[2][1])

print()

# Iterate through each data point (sublist in the list)
for point in data_points:
    print(f"x = {point[0]}, y = {point[1]}")

# Using tuple unpacking
for x, y in data_points:
    print(f"{x=}, {y=}")

# Nested loop: iterate through each sublist and then each element
for point in data_points:
    for value in point:
        print(value, end=" ")
    print() # new line after each sublist


# List comprehension
data_points = [[0,0], [1,3], [2,5], [3,6], [4,8]]
x_values = [point[0] for point in data_points]
print(x_values)

y_values = [point[1] for point in data_points]
print(y_values)

x_values = [x for x,y in data_points]
print(x_values)
y_values = [y for x,y in data_points]
print(y_values)

data_points = [[0,0], [1,3], [2,5], [3,6], [4,8]]
print(data_points)
data_points.sort()
print(data_points)
# .sort(reverse=True) will sort the list in reverse order by x-values, highest to lowest
data_points.sort(reverse=True)
print(data_points)
