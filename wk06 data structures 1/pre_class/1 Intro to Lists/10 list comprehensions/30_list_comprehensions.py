# List Comprehensions

squares = []
for i in range(11):
    squares.append(i ** 2)    
print(squares)

squares = [x**2 for x in range(11)]
print(squares)

squares = [x**2 for x in range(11) if x % 2 == 0]
print(squares)