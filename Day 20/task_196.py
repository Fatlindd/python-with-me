"""
Validate Role Hierarchies & Clean Permission Sets

Requirements
You are working on a permissions engine for a large-scale enterprise application. Each role in the system has a set
of permissions. Your task is to:
1. Validate if the admin_permissions fully include (i.e., are a superset of) the editor_permissions using issuperset().
2. Ensure that admin_permissions is a proper superset of editor_permissions using the > operator.
3. Simulate random permission rotation by removing one element from the auditor_permissions using pop().
4. Remove a deprecated permission ("DEPRECATED") from editor_permissions using remove(), and handle it properly if it’s
not there.
    - admin_permissions = {"READ", "WRITE", "DELETE", "EXPORT", "SHARE"}
    - editor_permissions = {"READ", "WRITE", "SHARE"}
    - auditor_permissions = {"READ", "EXPORT", "LOG"}
"""
admin_permissions = {"READ", "WRITE", "DELETE", "EXPORT", "SHARE"}
editor_permissions = {"READ", "WRITE", "SHARE"}
auditor_permissions = {"READ", "EXPORT", "LOG"}

# 1. Check if admin includes all of editor permissions
is_superset = admin_permissions.issuperset(editor_permissions)
print("Admin ⊇ Editor:", is_superset)

# 2. Check if admin is a proper superset (not equal) of editor
is_proper_superset = admin_permissions > editor_permissions
print("Admin ⊃ Editor:", is_proper_superset)

# 3. Remove and return a random element from auditor_permissions
removed = auditor_permissions.pop()
print("Removed from auditor_permissions (random):", removed)

# 4. Try removing a deprecated permission
try:
   editor_permissions.remove("DEPRECATED")
   print("Deprecated permission removed.")
except KeyError:
   print("Deprecated permission not found. Skipped.")
