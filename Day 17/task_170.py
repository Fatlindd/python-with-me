"""
Manage a To-Do List with append()

Requirements
You are building a simple command-line To-Do List app. Your job is to:
1. Initialize an empty list called todo_list.
2. Ask the user to input 3 tasks using the input() function.
3. Use the append() method to add each task to the todo_list.
4. After all tasks are added, print the final to-do list clearly.
"""
todo_list = []

print("Enter 3 tasks for your To-Do List:")
for i in range(3):
    task = input(f"Task {i + 1}: ")
    todo_list.append(task)

print("\nYour To-Do List:")
for task in todo_list:
   print(f"- {task}")
