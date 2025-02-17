# Exercise 6-3: Glossary

# Glossary of programming terms
glossary: dict[str, str] = {
    "Function (def)": "A block of reusable code defined with 'def' followed by a function name and parentheses. It can accept parameters and return a value.",
    "For Loop": "A control structure used to iterate over a sequence (like a list, tuple, or string) or range of numbers.",
    "Dictionary": "A collection of key-value pairs, where keys are unique and used to store and retrieve data.",
    ".replace": "A string method used to replace occurrences of a specified substring with another string.",
    "If Not": "A conditional statement used to execute a block of code only if the given condition evaluates to False."
}

# Print each word and its meaning, formatted neatly
for word, meaning in glossary.items():
    print(f"{word}:\n{meaning}\n")
