"""
Implement a Custom Undo Stack Using pop()

Requirements
You are building a simple text editor module that supports Undo functionality. Every user action (e.g., typing a
character, deleting a line, pasting content) is stored in an undo stack. When the user presses Undo, the most recent
action should be removed from the stack and reversed (simulated).

Your goal:
1. Create a class UndoManager that:
    - Has a list undo_stack to track actions.
    - Has a method add_action(action: str) to record an action.
    - Has a method undo_last() that uses pop() to remove the most recent action and returns a message: "Undoing:
    <action>".
    - If no actions remain, return "Nothing to undo."
2. Show usage by simulating at least 3 actions and undoing them one by one.
"""
class UndoManager:
    def __init__(self):
        self.undo_stack = []

    def add_action(self, action):
        self.undo_stack.append(action)

    def undo_last(self):
        if self.undo_stack:
            last_action = self.undo_stack.pop()
            return f"Undoing: {last_action}"
        else:
            return "Nothing to undo."

# Demo usage
manager = UndoManager()

manager.add_action("Typed 'Hello'")
manager.add_action("Deleted line 3")
manager.add_action("Pasted text")

print(manager.undo_last())  # Undoing: Pasted text
print(manager.undo_last())  # Undoing: Deleted line 3
print(manager.undo_last())  # Undoing: Typed 'Hello'
print(manager.undo_last())  # Nothing to undo.