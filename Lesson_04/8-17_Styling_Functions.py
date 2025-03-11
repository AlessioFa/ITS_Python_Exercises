# Exercise 8-17: Styling Functions
# Frome exercise 8-7

def make_album(artist: str, title: str, songs_count: int = None) -> dict[str, str | int]:
    """Create a dictionary with album information."""

    album_info: dict[str, str | int] = {
        "artist_name": artist,
        "album_title": title,
    }

    # Add the song count if provided
    if songs_count:
        album_info["songs_count"] = songs_count

    return album_info


# Create an album and print its information
album1 = make_album("Post Malone", "Stoney", 14)
print(album1)

# Changes made:
# 1. Added a docstring to describe the function's purpose.
# 2. Used shorter variable names (artist, title) for clarity and simplicity.
# 3. Added a blank line after the function's docstring to improve readability.
# 4. Simplified and clarified comments.

# From exercise 8-2


def favorite_book(title: str) -> None:
    """Print the title of a favorite book."""
    print(f"My favorite book is: {title}.")


# Call the function with a specific book title
favorite_book("Cambia l'abitudine di essere te stesso")

# Changes made:
# 1. Added a docstring to describe the purpose of the function.
# 2. Clarified the function call with a comment.
# 3. Used appropriate spacing for better readability.


# From exercise 8-5

def describe_city(city: str, country: str = "Japan") -> str:
    """
    Prints a statement about the city and its country.
    """
    # Print a message about the city and its country
    print(f"{city} is in {country}")


# Call the function with the default country (Japan)
describe_city("Tokyo")

# Call the function with a custom country (France)
describe_city("Paris", country="France")

# Call the function with another custom country (Italy)
describe_city("Rome", country="Italy")

# Changes made:
# 1. Added a docstring to explain the function's purpose, parameters, and return value.
# 2. Improved comments for better readability and understanding.
