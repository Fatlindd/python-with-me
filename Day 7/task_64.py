"""
User Albums: Start with your program from Exercise 65. Write a while loop that allows users to enter an album’s artist
and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s
created. Be sure to include a quit value in the while loop.
"""
def make_album(artist, title, number_of_songs=None):
   """Build a dictionary describing a music album."""
   album = {
       "artist": artist.title(),
       "title": title.title()
   }
   if number_of_songs:
       album["songs"] = number_of_songs
   return album


print("Enter 'quit' at any time to stop.\n")

while True:
   artist = input("Enter the artist name: ")
   if artist.lower() == 'quit':
       break

   title = input("Enter the album title: ")
   if title.lower() == 'quit':
       break

   song_count = input("Enter number of songs (optional, or press Enter to skip): ")
   if song_count.lower() == 'quit':
       break

   if song_count.strip():  # check if input is not empty
       album = make_album(artist, title, int(song_count))
   else:
       album = make_album(artist, title)

   print("\nCreated album dictionary:")
   print(album)
   print("-" * 40)