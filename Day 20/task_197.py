"""
Analyze and Synchronize Team Tech Skills

Requirements
You are managing multiple developer teams in a large tech company. Each team has members with different tech skill sets.

Your task is to:
1. Identify the skills that are unique to either team_alpha or team_beta but not both (using symmetric_difference() and
^).
2. Update team_alpha’s skills to only reflect those unique differences using symmetric_difference_update() and ^=.
3. Compute the total combined skill set between team_alpha and team_gamma (use union() and |).
4. Permanently update team_beta’s skill set by merging in team_gamma's skills using update() and |=.
    - team_alpha = {"Python", "JavaScript", "SQL", "Docker"}
    - team_beta = {"Go", "Python", "SQL", "Kubernetes"}
    - team_gamma = {"Rust", "Docker", "Kubernetes"}
"""
team_alpha = {"Python", "JavaScript", "SQL", "Docker"}
team_beta = {"Go", "Python", "SQL", "Kubernetes"}
team_gamma = {"Rust", "Docker", "Kubernetes"}

# 1. Get symmetric difference: skills in either team_alpha or team_beta but not both
unique_skills = team_alpha.symmetric_difference(team_beta)
print("Unique skills between Alpha and Beta: ", unique_skills)

# Alternative using ^
print("Same thing (using ^): ", team_alpha ^ team_beta)

# 2. Update team_alpha with only the unique skills
team_alpha.symmetric_difference_update(team_beta)
print("Updated Alpha (only unique): ", team_alpha)

# Alternative using ^=
team_alpha = {"Python", "JavaScript", "SQL", "Docker"}
team_alpha ^= team_beta
print("Reset Alpha ^ Beta:", team_alpha)

# 3. Get union of Alpha and Gamma (all unique skills combined)
combined_skills = team_alpha.union(team_beta)
print("Combined skills (Alpha + Gamma): ", combined_skills)

# Alternative using |
print("Same (using |): ", team_alpha | team_beta)

# 4. Update team_beta by adding all skills from Gamma
team_beta.update(team_gamma)
print("Updated Beta (merged with Gamma): ", team_beta)

# Alternative using |=
team_beta = {"Go", "Python", "SQL", "Kubernetes"}
team_beta |= team_gamma
print("Reset Beta |= Gamma: ", team_beta)