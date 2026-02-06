"""
Inject Audit Entries into a Time-Ordered Event Log

Requirements
You’re working with a system log that stores a list of user actions in the order they occurred. Sometimes, delayed
audit events arrive later and must be inserted into their correct chronological position.
Your task:
1. Define a list of system events where each event is a tuple: (timestamp, action).
2. Write a function insert_audit_event(log, event) that:
    - Accepts the current log and a delayed event.
    - Uses insert() to place the event into the correct index based on timestamp.
    - Returns the updated log.
3. Demonstrate it with:
    - One event that should go in the middle
    - One event that should go at the beginning
    - One event that should go at the end
"""
def insert_audit_event(log, event):
    for i, existing_event in enumerate(log):
        if event[0] < existing_event[0]:
            log.insert(i, event)
            return log

    log.append(event) # If no earlier timestamp, append at the end
    return log

# Simulated event log (sorted by timestamp)
event_log = [
   (100, "login"),
   (150, "view_dashboard"),
   (200, "logout")
]

# Delayed events
late_event_1 = (130, "2FA_check")     # Should go in the middle
late_event_2 = (90, "security_check") # Should go at the beginning
late_event_3 = (250, "session_end")   # Should go at the end

# Insert delayed events
event_log = insert_audit_event(event_log, late_event_1)
event_log = insert_audit_event(event_log, late_event_2)
event_log = insert_audit_event(event_log, late_event_3)

# Print updated log
for e in event_log:
   print(e)