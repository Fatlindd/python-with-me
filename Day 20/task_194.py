"""
Set Operations in a Role-Based Access Control (RBAC) System

Requirements
You are building part of a backend system to manage permissions for user roles in a Role-Based Access Control (RBAC)
system.
1. Start with two sets:
    - admin_permissions: Set of permissions assigned to admin users.
    - guest_permissions: Set of permissions for guest users.
2. Perform the following:
    - Use add() to add a new permission ("EXPORT_REPORTS") to admin_permissions.
    - Create a backup of the guest_permissions set using copy().
    - Use difference() to find permissions that admin has but guest doesn't.
    - Use difference_update() to remove from admin_permissions all permissions that guests also have.
    - Use clear() to remove all permissions from the guest backup.
"""
# Initial sets
admin_permissions = {"READ", "WRITE", "DELETE", "SHARE"}
guest_permissions = {"READ", "WRITE"}

# 1. Add a new permission to admin
admin_permissions.add("EXPORT_REPORTS")

# 2. Backup guest permissions
guest_backup = guest_permissions.copy()

# 3. Permissions only admin has
admin_exclusive = admin_permissions.difference(guest_permissions)
print("Admin-only permissions: ", admin_exclusive)

# 4. Remove common permissions from admin
admin_permissions.difference_update(guest_permissions)
print("Admin permissions after update: ", admin_permissions)

# 5. Clear the guest backup set
guest_backup.clear()
print("Guest backup after clear: ", guest_backup)