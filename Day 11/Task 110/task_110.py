"""
You’re developing a logging tool that processes user-submitted content from multiple languages. Your goal is to:
Take a list of user-submitted strings that may contain non-ASCII characters.
Safely export them to a .txt log file.
Use ascii() to convert all strings into ASCII-safe representation before writing to the file.
Ensure all strings are ASCII-only before storing, so the log file can be safely parsed in systems that don’t support
UTF-8 or Unicode.
"""
def export_ascii_log(text_list, filename="ascii_log.txt"):
   with open(filename, 'w', encoding='utf-8') as f:
       for line in text_list:
           safe_line = ascii(line)
           f.write(safe_line + '\n')
   print(f"✅ Log saved to {filename}")

# Example input
user_inputs = [
   "Hello",
   "Ça va bien",
   "München",
   "你好",
   "¡Hola señor!"
]

export_ascii_log(user_inputs)
