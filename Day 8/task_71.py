"""
Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py.
Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""

# printing_functions.py
def print_models(unprinted_designs, completed_models):
   """Simulate printing each design, until none are left."""
   while unprinted_designs:
       current_design = unprinted_designs.pop()
       print(f"Printing model: {current_design}")
       completed_models.append(current_design)


def show_completed_models(completed_models):
   """Show all the models that were printed."""
   print("\nThe following models have been printed:")
   for model in completed_models:
       print(f"- {model}")


# printing_models.py
# from printing_functions import print_models, show_completed_models
#
# unprinted_designs = ['phone case', 'robot pendant', 'drone frame']
# completed_models = []
#
#
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)
