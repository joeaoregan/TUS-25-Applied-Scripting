# P53 - Tuples

print(divmod(7,3))

quotient, remainder = divmod(7,3)
print(quotient, remainder)

print()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for i,day in enumerate(days):
    print(f"Day {i} is {day}")

print()

forecasts = ["cloudy", "rain", "rain", "fair", "cloudy", "cloudy", "fair"]
actuals = ["rain", "rain", "rain", "cloudy", "cloudy", "rain", "cloudy"]
correct_count = 0
for day, forecast_value, actual_value in zip(days, forecasts, actuals):
    # check if the forecast and actual values match for this day
    if forecast_value == actual_value:
        correct_count += 1
        print(f"Crorect prediction for {day}: {forecast_value}")

# Creating a Tuple
vowels = "a", "e", "i", "o", "u"
print(vowels)

# single-value tuple
single = ("a",)
print(single)
print(type(single))
single = ("a")
print(single)
print(type(single))

# single-value tuple
the_answer = (42,)
print(the_answer)
print(type(the_answer))
the_answer = (42)
print(the_answer)
print(type(the_answer))

# Empty Tuple
result = ()
print(result)
print(type(result))

# tuple()
empty = tuple()
print(empty)

# convert iterable with tuple()
vowels = tuple("aeiou")
print(vowels)

numbers = tuple(range(5))
print(numbers)
