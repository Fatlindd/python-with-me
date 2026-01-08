"""
You are working on a weather data analysis tool. For each day, the deviation between the predicted and actual
temperature is recorded. You want to calculate how far off each prediction was—regardless of whether it was too high
or too low. Use the abs() function to convert those deviations into positive numbers for easier analysis and reporting.
"""
def calculate_absolute_deviation(deviations):
    absolute_values = [abs(d) for d in deviations]
    return absolute_values

# Sample data
deviations = [3, -2, 0, -5, 4]
absolute = calculate_absolute_deviation(deviations)

# Print summary
print(f"Original deviations: {deviations}")
print(f"Absolute deviations: {absolute}")
print(f"Average deviation: {sum(absolute)/len(deviations)}")