"""
Locate First Occurrence of Critical Error Code in Log Stream

Requirements
You are given a tuple of log entries representing status/error codes emitted by a live telemetry system. You must:
    - Write a function find_first_occurrence(logs: tuple, target_code: int) -> int
    - The function should:
        - Search for the first occurrence of target_code in the tuple logs
        - Return the index (position) where the value was found
        - Raise a ValueError if the code is not present (let Python handle this by default)
"""
def find_first_occurrence(logs: tuple, target_code: int) -> int:
    return logs.index(target_code)

# Example usage
logs = (200, 302, 404, 200, 500, 302, 500, 404)
print("First index of 500:", find_first_occurrence(logs, 500))
