"""
Format and Analyze Log Records with String Methods

Requirements
You’re maintaining a system that processes logs in the form of tab-separated strings and stores formatted summaries.
Your responsibilities:
1. Normalize tabbed logs for visibility using expandtabs().
2. Search for critical keywords like "ERROR" or "CRASH" using find() and index().
3. Format a summary string using both format() and format_map() for reporting.

logs = [
   "12:01\tINFO\tSystem boot complete",
   "12:02\tWARNING\tDisk space low",
   "12:03\tERROR\tFailed to load config",
   "12:04\tINFO\tListening on port 8080",
   "12:05\tCRASH\tUnhandled exception occurred"
]
"""
logs = [
   "12:01\tINFO\tSystem boot complete",
   "12:02\tWARNING\tDisk space low",
   "12:03\tERROR\tFailed to load config",
   "12:04\tINFO\tListening on port 8080",
   "12:05\tCRASH\tUnhandled exception occurred"
]

TAB_WIDTH = 4
report_template ="At {time}, a {level} event occurred: {message}"
total_errors = 0

for log in logs:
    # Expand tab characters to fixed-width spaces
    expanded = log.expandtabs(TAB_WIDTH)

    # Split into components
    parts = expanded.split(maxsplit=2)
    print(f"parts: {parts}")
    time, level, message = parts

    # Search for keywords
    error_found = "ERROR" in level or "CRASH" in level
    pos_error = log.find("ERROR")

    # Use format()
    summary_1 = "Formatted: {}".format(message)

    # Use format_map()
    summary_2 = report_template.format_map({
        "time": time,
        "level": level,
        "message": message
    })

    # Use index() safely (only if known to exist)
    try:
        crash_pos = log.index("CRASH")
    except ValueError:
        crash_pos = -1

    # Output
    print("Original log: ", log)
    print("Expanded log: ", expanded)
    print("Error found: ", error_found)
    print("Position of 'ERROR' (find): ", pos_error)
    print("Position of 'CRASH' (index): ", crash_pos)
    print("Summary (format): ", summary_1)
    print("Summary (format_map): ", summary_2)
    print("====")

    if error_found:
        total_errors += 1

print("Total critical errors: ", total_errors)