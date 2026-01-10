"""
You are building a system for tracking employees in a company. Your goals:
- Create a class Employee with attributes like name and position.
- Maintain a class-level count of how many employees have been created.
- Implement a @classmethod called get_employee_count() that returns the current count.
- Allow multiple instances to be created, and verify that the count updates correctly.
"""
class Employee:
   total_employees = 0

   def __init__(self, name, position):
       self.name = name
       self.position = position
       Employee.total_employees += 1

   @classmethod
   def get_employee_count(cls):
       return f"Total employees created: {cls.total_employees}"

# Creating some employees
e1 = Employee("Alice", "Manager")
e2 = Employee("Bob", "Engineer")
e3 = Employee("Charlie", "Analyst")

# Using the class method
print(Employee.get_employee_count())
