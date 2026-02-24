"""
Low-Level File I/O Inspection and Stream Handling

Requirements
You are building a logging system that:
1. Writes log messages to a file.
2. Ensures flushing happens after each write.
3. Checks whether the file is connected to an interactive terminal.
4. Uses fileno() to inspect the OS-level file descriptor.
5. Uses detach() in a controlled test to access the raw buffer (in text mode).
6. Properly closes all file streams at the end.

Your task is to write a Python script that:
- Opens a file for logging.
- Writes and flushes a message.
- Displays whether the stream is interactive (using isatty()).
- Shows the file descriptor.
- Demonstrates how to detach() a text wrapper (only in a test or controlled environment).
- Closes the file stream gracefully.
"""
import io

def file_stream_inspector(file_path: str):
    print("Opening file...")
    f = open(file_path, mode="w+", encoding="utf-8", buffering=1) # Line-buffered

    print("Writing to file...")
    f.write("System initialized.\n")
    f.flush()

    print("Is interactive stream:", f.isatty())  # Usually False unless connected to TTY
    print("OS-level file descriptor:", f.fileno())

    # Detach example (advanced use, typically for experimentation)
    # WARNING: After detach, f is unusable.
    print("\nDetaching the buffer...")
    try:
        raw = f.detach()  # returns underlying BufferedWriter
        print("Detached stream:", type(raw))
        raw.write(b"Detached raw binary write\n")
        raw.flush()
        raw.close()
    except io.UnsupportedOperation as e:
        print("Detach not supported in this mode:", e)

    print("\nStream detached. Original file object is no longer usable.")
    print("\nFile operations completed.")

file_stream_inspector("log_output.txt")