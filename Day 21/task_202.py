"""
Log Message Processor for Audit System

Requirements
Build a LogProcessor class to analyze system log strings. It should:
1. Clean each log message by trimming whitespace from the right using rstrip().
2. Split log entries from a long multiline string using rsplit('\n', maxsplit=5) to get the most recent 5 logs.
3. For each log:
    - Right-align the severity level (e.g., "ERROR", "INFO") using rjust(10) for console display.
    - Use rfind() and rindex() to locate the last timestamp or marker in the log.
    - Use rpartition() to split the log into: text before timestamp, the timestamp itself, and any trailing message.

The final report should include:
  - Cleaned and justified logs
  - Positions of the last markers (found using rfind and rindex)
  - rpartitioned structure for each log line
"""
class LogProcessor:
   def __init__(self, raw_logs):
       self.raw_logs = raw_logs

   def process_logs(self):
       # Step 1: Trim trailing whitespace
       cleaned = self.raw_logs.rstrip()

       # Step 2: Take last 5 log entries
       recent_logs = cleaned.rsplit('\n', maxsplit=5)

       report = []

       for log in recent_logs:
           # Right-justify the log level
           if "ERROR" in log:
               level = "ERROR"
           elif "INFO" in log:
               level = "INFO"
           elif "WARNING" in log:
               level = "WARNING"
           else:
               level = "UNKNOWN"

           justified_level = level.rjust(10)

           # Find last occurrence of timestamp pattern (e.g., [2025-09-27])
           last_bracket_pos = log.rfind('[')
           last_index_pos = log.rindex(']') if ']' in log else -1

           # Split using rpartition on space before timestamp
           before, sep, after = log.rpartition('[')

           report.append({
               "original": log,
               "justified_level": justified_level,
               "rfind_position": last_bracket_pos,
               "rindex_position": last_index_pos,
               "rpartition_result": (before.strip(), sep + after if sep else after, "")
           })

       return report

# Example usage
raw_logs = """
INFO  System started successfully   [2025-09-26]
WARNING  Low disk space [2025-09-26]
ERROR  Failed to load config file [2025-09-26]
INFO  Cleanup completed     [2025-09-27]
ERROR  Timeout while connecting to DB [2025-09-27]
DEBUG  Test message [2025-09-27]
"""

processor = LogProcessor(raw_logs)

from pprint import pprint
pprint(processor.process_logs())

