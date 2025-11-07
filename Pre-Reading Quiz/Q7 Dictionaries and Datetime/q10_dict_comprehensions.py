# Question 10
# Which of the following dictionary comprehensions will create a dictionary containing {1:10, 2:20, ... 10:100}?

dict1 = { i:i*10 for i in range(1,11) }
dict2 = { i:i*i for i in range(1,11) }
dict3 = { i:i*i for i in range(1,11) }
dict4 = { i:i*10 for i in range(1,10) }

print(type(dict1))
print(type(dict2))
print(type(dict3))
print(type(dict4))

print(dict1)
print(dict2)
print(dict3)
print(dict4)