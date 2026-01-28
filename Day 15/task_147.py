"""
Find the Highest Scoring Student
You are given a list of students, each with a name and a test score.
Use the max() function to identify the student with the highest score.
Your function should return both the name and the score of the top student.
"""
# Step 1: Define the student list
students = [
   {"name": "Anna", "score": 88},
   {"name": "Ben", "score": 92},
   {"name": "Clara", "score": 85},
   {"name": "David", "score": 90}
]

# Step 2: Use max() with key argument
top_student = max(students, key=lambda x: x["score"])

# Step 3: Display the result
print(f"Top student: {top_student['name']} with score: {top_student['score']}")
