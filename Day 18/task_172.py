"""
Modify a Copy of User Roles Without Altering the Original List

Requirements
You are working on an RBAC (Role-Based Access Control) system. You need to:
1. Maintain a master list of default roles: ["Admin", "Editor", "Viewer"]
2. Create a copy of the list to customize it for a specific client without changing the original.
3. Modify the copy by:
    - Adding a new role "Analyst"
    - Removing the "Viewer" role
4. Print both the modified list and the original to confirm only the copy changed.
"""
default_roles = ["Admin", "Editor", "Viewer"]
client_roles = default_roles.copy()  # Safe copy

# Customize the client-specific roles
client_roles.append("Analyst")
client_roles.remove("Viewer")

print("Default Roles:", default_roles)
print("Client Roles:", client_roles)