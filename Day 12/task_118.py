"""
You’re building a simple dynamic code executor. Your goals:
Create a string containing Python code (e.g. "result = 10 + 20").
Use the built-in compile() function to convert this string into executable code.
Execute the code using exec() and then print the result.
Extend the task to allow compiling code in 'eval', 'exec', and 'single' modes.
"""
# Define a source code string
source_code = "result = 10 + 20"

# Compile the source code into a code object (mode='exec' for statements)
code_object = compile(source_code, filename="<string>", mode="exec")

# Define a namespace (dictionary) to store variables
namespace = {}

# Execute the compiled code object
exec(code_object, namespace)

# Access the result from the namespace
print("Result:", namespace['result'])


# Different Mode
# eval mode: for single expressions
expression = "5 * 3"
compiled_expr = compile(expression, "<string>", "eval")
print("Eval result:", eval(compiled_expr))

# single mode: for a single interactive statement (like print)
code = "print('Hello from single mode!')"
compiled_single = compile(code, "<string>", "single")
exec(compiled_single)
