# Program to compare Forecast weather vs actual weather
# Example of zip to traverse multiple lists simulataneously

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
forecasts = ["cloudy", "rain", "rain", "fair", "cloudy", "cloudy","fair"]
actuals = ["rain", "rain", "rain", "cloudy", "cloudy", "rain", "cloudy"]

correct_count = 0
# # Iterate through each day with its forecast and actual weather

for day, forecast_value, actual_value in zip(days, forecasts, actuals):
    # check if the forecast and actual values match for this day
    if forecast_value == actual_value: 
        correct_count += 1
        print(f"Correct prediction for {day}: {forecast_value}")

print(f"Total correct predictions: {correct_count}")

