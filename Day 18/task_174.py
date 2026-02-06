"""
Merge Multiple Feature Flags from Teams into a Unified List

Requirements
You’re managing multiple product teams working on separate modules of a large SaaS platform. Each team defines its own
list of active feature flags. As the DevOps lead, you need to:
1. Simulate feature flag lists for three different teams.
2. Use the extend() method to merge all flags into a unified master list.
3. Remove any duplicates to get a clean, production-ready list.
4. Print both the raw merged list and the final deduplicated one.
"""
# Simulated feature flags from different teams
team_a_flags = ["login_v2", "dark_mode", "referral_program"]
team_b_flags = ["dark_mode", "beta_dashboard", "api_rate_limit"]
team_c_flags = ["referral_program", "chat_support", "analytics_v3"]

# Master feature flag list
master_flags = []

# Merge using extend()
master_flags.extend(team_a_flags)
master_flags.extend(team_b_flags)
master_flags.extend(team_c_flags)

print("Raw Merged Flags (With Duplicates):")
print(master_flags)

# Deduplicate while preserving order
abc = dict.fromkeys(master_flags)
final_flags = list(dict.fromkeys(master_flags))  # Python 3.7+ maintains order in dict

print("\nFinal Feature Flags (Deduplicated):")
print(final_flags)