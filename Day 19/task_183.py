"""
Use fromkeys() to Bootstrap Role-Based Permissions Dictionary

Requirements
You are designing an access control system for a SaaS application. Your task is to:
1. Define a list of user roles: "admin", "editor", "viewer".
2. Use the fromkeys() method to initialize a dictionary where each role maps to the same default permission set
(a list of permissions: ["read"]).
3. Demonstrate the pitfall of using a mutable default value across keys.
4. Fix the issue by using a dictionary comprehension to assign separate lists per role.
"""
# Roles and default permissions
roles = ["admin", "editor", "viewer"]
default_permissions = ["read"]

# Problematic usage
permissions_map = dict.fromkeys(roles, default_permissions)

# Modifying one role’s permission
permissions_map["admin"].append("write")

print("Shared default issue:")
print(permissions_map)
# All roles now have 'write' permission, which is unintended

# Correct way using dictionary comprehension
correct_permissions_map = {role: ["read"] for role in roles}

# Now safely modify 'admin'
correct_permissions_map["admin"].append("write")

print("\nFixed version:")
print(correct_permissions_map)
