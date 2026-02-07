"""
Sort a List of Dictionaries by Multiple Fields Using sort()

Requirements
You are given a list of employee records, where each record is a dictionary containing:
    - name: a string
    - department: a string
    - salary: an integer

Your task is to:
1. Sort the list in-place using sort() such that:
    - Employees are grouped by department (alphabetically).
    - Within each department, they are sorted by salary (descending).
2. Write a function sort_employees(employees: list) -> None that performs the sorting.
3. Do not return a new list — use the sort() method properly.

employees = [
   {"name": "Alice", "department": "Sales", "salary": 60000},
   {"name": "Bob", "department": "Engineering", "salary": 80000},
   {"name": "Charlie", "department": "Sales", "salary": 70000},
   {"name": "Dana", "department": "Engineering", "salary": 75000}
]
"""
def sort_employees(employees):
    employees.sort(key=lambda e: (e["department"], -e["salary"]))

# Example usage
employees = [
   {"name": "Alice", "department": "Sales", "salary": 60000},
   {"name": "Bob", "department": "Engineering", "salary": 80000},
   {"name": "Charlie", "department": "Sales", "salary": 70000},
   {"name": "Dana", "department": "Engineering", "salary": 75000}
]

sort_employees(employees)
for emp in employees:
    print(emp)