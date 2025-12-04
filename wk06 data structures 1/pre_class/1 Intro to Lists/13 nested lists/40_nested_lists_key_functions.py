from random import shuffle

data_points = [[0,0], [1,3], [2,5], [3,6], [4,8]]
shuffle(data_points)
print(data_points)

data_points.sort(key=lambda point: point[1])
print(data_points)

data_points.sort(key=lambda point: point[1], reverse=True)
print(data_points)

