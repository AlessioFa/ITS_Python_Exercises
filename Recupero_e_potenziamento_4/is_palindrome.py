def is_palindrome(word1: str, word2: str) -> None:

    if word1 == word2[::-1]:

        print("È palindroma!")
    
    else:
        print("Non è palindroma!")


is_palindrome("radar", "radar")


def is_palindrome_recursive(word: str) -> None:

    word = word.lower().replace(" ", "")

    if len(word) <= 1:

        return True
    
    if word[0] != word[-1]:

        return False
    
    else:

        return is_palindrome_recursive(word[1:-1])
    

is_palindrome_recursive("radar")

