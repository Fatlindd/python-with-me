"""
Frequency Analysis of Tuple Values Using count()

Requirements
You are processing sensor data stored as an immutable sequence of status codes. Each reading is stored as a tuple of
integers ranging from 0 to 5. You must:
    - Write a function analyze_status_frequency(readings: tuple) -> dict
    - The function should return a dictionary where:
        - Keys are unique status codes (0 to 5)
        - Values are the number of times each status code appears in the tuple
    - Use the built-in count() method on the tuple to get the frequency.
"""
def analyze_status_frequency(readings: tuple) -> dict:
    return {code: readings.count(code) for code in readings}

# Example usage
sensor_data = (1, 2, 3, 1, 4, 0, 1, 2, 5, 3, 2, 0, 1)

result = analyze_status_frequency(sensor_data)
print("Status Code Frequencies: ", result)