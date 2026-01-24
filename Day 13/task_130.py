"""
Check Common Courses Between Students (Immutable Set)
Create a Python script that checks for common courses between two students.
Use regular set for the initial course lists.
Convert both course lists to frozenset to simulate immutability and ensure data isn't accidentally modified.
Display the common courses using set intersection.
"""
# Initial course selections
student_a_courses = {"Math", "Biology", "Chemistry", "English"}
student_b_courses = {"History", "Biology", "English", "Art"}

# Convert to frozenset to make them immutable
a_set = frozenset(student_a_courses)
b_set = frozenset(student_b_courses)

# Find common courses (intersection)
common_courses = a_set & b_set

# Output result
print("Common courses between Student A and Student B:")
for course in common_courses:
   print("-", course)