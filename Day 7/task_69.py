"""
User Profile: Build a profile of yourself by calling build_profile(), using your first and last names and three other
key-value pairs that describe you.
"""
def build_profile(first, last, **user_info):
   """Build a dictionary containing everything we know about a user."""
   profile = {}
   profile['first_name'] = first
   profile['last_name'] = last
   for key, value in user_info.items():
       profile[key] = value
   return profile

# Example usage — building your own profile
my_profile = build_profile(
   'Fatlind',
   'Thaci',
   age=26,
   location='Kosovo',
   profession='Software Developer',
   favorite_language='Python'
)

print(my_profile)
