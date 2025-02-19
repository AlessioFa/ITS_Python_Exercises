# Exercise 8-8: User Album



def make_album(artist_name: str, album_title: str, songs_count=None):
    # Create a dictionary containing the artist's name and album title
    album_info: dict[str, str | int] = {
        "artist_name": artist_name,
        "album_title": album_title,
    }
    # If songs_count is provided, add it to the dictionary
    if songs_count:
        album_info["songs_count"] = songs_count
    return album_info

while True:
    # Ask the user to enter the name of an artist
    artist_name = input("Enter a name of an artist: ")
    # If the user enters "quit", exit the loop
    if artist_name == "quit":
        break

    # Ask the user to enter the title of an album
    album_title = input("Enter an album title of the artist you chose: ")
    # If the user enters "quit", exit the loop
    if album_title == "quit":
        break

    # Ask the user to enter the number of songs in the album
    songs_count = input("Enter the number of the songs: ")
    # If the user enters "quit", exit the loop
    if songs_count == "quit":
        break

    # Call the make_album function to create a dictionary with the album information
    album1 = make_album(artist_name, album_title, songs_count)
    
    # Print the album information to show the dictionary output
    print(album1)
