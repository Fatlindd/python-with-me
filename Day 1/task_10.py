# Intentional Error

# Simple list of animals
animals = ["Cat", "Dog", "Elephant"]


# Intentional Index Error
print("This will cause an error:")
# print(animals[3])  # ❌ IndexError: list index out of range


# ✅ Corrected version
print("\nCorrected version:")
print(animals[2])  # "Elephant" is at index 2 (last valid index)
