"""
 Styling Functions: Choose any three programs you wrote for this chapter, and make sure they follow the styling
 guidelines described in this section.
"""
# Before styling
def display_message():
   print("i am learning python functions.")

# After styling
def display_message():
   """Display what this chapter is about."""
   print("I am learning Python functions.")

# Before styling
def make_shirt(size, message):
   print('shirt size is ' + size)
   print('message is ' + message)

# After styling
def make_shirt(size, message):
   """Print the size and message of a custom shirt."""
   print("Shirt size is: " + size.title())
   print("Message on the shirt: '" + message + "'")

# Before styling
def make_album(artist, title, tracks=None):
   album = {'artist': artist, 'title': title}
   if tracks:
       album['tracks'] = tracks
   return album

# After styling
def make_album(artist, title, tracks=None):
   """Build a dictionary describing a music album."""
   album = {
       'artist': artist.title(),
       'title': title.title()
   }
   if tracks:
       album['tracks'] = tracks
   return album
