# Exercise 8-7: Album

def make_album(artist_name: str, album_title: str, songs_count=None) -> dict[str, str | int]:
    # Create a dictionary containing the artist's name and album title
    album_info: dict[str, str | int] = {
        "artist_name": artist_name,
        "album_title": album_title,
    }

    # If a song count is provided, add it to the dictionary
    if songs_count:
        album_info["songs_count"] = songs_count

    # Return the dictionary containing album information
    return album_info


album1 = make_album("Post Malone", "Stoney", 14)

# Print the album information to show the dictionary output
print(album1)
