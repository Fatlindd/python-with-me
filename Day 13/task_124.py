"""
Given a list of to-do items, print each task with its corresponding number starting from 1.
Use the enumerate() function to handle automatic indexing.
Format the output like:
 - Buy groceries
 - Call John
 - Finish Python project
"""
def display_todo_list(tasks):
    print("Your To-Do List: ")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

# Example usage
todo_items = [
    "Buy groceries",
    "Call John",
    "Finish Python project"
]

display_todo_list(todo_items)