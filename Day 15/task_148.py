"""
Use memoryview() to Modify a Bytearray Without Copying
You're given a bytearray of ASCII values for the word "Hello". Your task is to:
Create a memoryview of the bytearray.
Change the first character from 'H' to 'J' using the memoryview.
Print the updated bytearray as a string.
"""
# Step 1: Create a bytearray
data = bytearray(b"Hello")

# Step 2: Create a memoryview
mv = memoryview(data)

# Step 3: Modify the first byte (ASCII for 'J' is 74)
mv[0] = 74

# Step 4: Print the updated bytearray as string
print(data.decode('utf-8')) # Output: Jello