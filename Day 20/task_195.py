"""
Analyzing User Group Permissions with Advanced Set Logic

Requirements
You are maintaining a user access system for a large SaaS platform. Each user group (e.g., Editor, Viewer, Admin,
Auditor) has a set of permissions. Your goal is to:
1. Remove a deprecated permission from the editor_permissions using discard() (even if it may not exist).
2. Find common permissions between editor_permissions and auditor_permissions using intersection().
3. Update viewer_permissions to only keep permissions common with editor_permissions using intersection_update().
4. Check if admin_permissions and contractor_permissions have nothing in common using isdisjoint().
5. Check if viewer_permissions is a subset of editor_permissions using issubset().
6. Verify if auditor_permissions is a proper subset of admin_permissions using <.
    - admin_permissions = {"READ", "WRITE", "DELETE", "EXPORT", "SHARE"}
    - editor_permissions = {"READ", "WRITE", "SHARE", "COMMENT", "PUBLISH"}
    - viewer_permissions = {"READ", "COMMENT"}
    - auditor_permissions = {"READ", "EXPORT"}
    - contractor_permissions = {"DEPLOY", "BUILD"}
"""
admin_permissions = {"READ", "WRITE", "DELETE", "EXPORT", "SHARE"}
editor_permissions = {"READ", "WRITE", "SHARE", "COMMENT", "PUBLISH"}
viewer_permissions = {"READ", "COMMENT"}
auditor_permissions = {"READ", "EXPORT"}
contractor_permissions = {"DEPLOY", "BUILD"}

# 1. Remove a deprecated permission from the editor_permissions using discard() (even if it may not exist).
editor_permissions.discard("DEPRECATED")

# 2. Find common permissions between editor_permissions and auditor_permissions using intersection().
common_permissions = editor_permissions.intersection(auditor_permissions)
print("Common permissions (editor & auditor):", common_permissions)

# 3. Keep only common permissions in viewer that also exist in editor
viewer_permissions.intersection_update(editor_permissions)
print("Update viewer permissions:", viewer_permissions)

# 4. Check if admin and contractor have no permissions in common
print("Admin and contractor disjoint:", admin_permissions.isdisjoint(contractor_permissions))

# 5. Check if viewer permissions are subset of editor
print("Viewer ⊆ Editor:", viewer_permissions.issubset(editor_permissions))

# 6. Check if auditor is a proper subset of admin
print("Auditor < Admin: ", auditor_permissions < admin_permissions)