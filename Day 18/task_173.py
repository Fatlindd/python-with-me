"""
Analyze Frequency of Statuses in an Audit Log

Requirements
You are building an internal audit tool for a multi-user SaaS platform. The audit log system records user actions and
assigns statuses such as "success", "error", "pending", etc.
You need to:
1. Simulate a list of status entries from audit logs.
2. Use the count() method to:
    - Determine how many times "success" appeared.
    - Determine how many times "error" appeared.
3. Generate a basic summary report for log analysis.
"""
# Simulated audit log statuses
audit_log_statuses = [
   "success", "success", "error", "success", "pending",
   "error", "success", "success", "error", "success"
]

# Use count() to get frequencies
success_count = audit_log_statuses.count("success")
error_count = audit_log_statuses.count("error")

# Print summary
print(f"✅ Success Count: {success_count}")
print(f"❌ Error Count: {error_count}")