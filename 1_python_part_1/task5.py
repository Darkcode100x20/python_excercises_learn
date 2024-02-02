"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""
def remove_duplicated_words(line: str) -> str:
    # Split the input string into words.
    words = line.split()
    
    # Create an empty list to store words that have been seen.
    seen_words = []
    
    # Iterate through the list of words.
    for word in words:
        # Check if the word is already in the list of seen words.
        if word not in seen_words:
            # If it's not, append it to the list of seen words.
            seen_words.append(word)
    
    # Join the list of seen words back into a string, separated by spaces.
    result = ' '.join(seen_words)
    
    # Return the resulting string.
    return result

# Test the function with the example inputs.
print(remove_duplicated_words('cat cat dog 1 dog 2'))  # Output should be 'cat dog 1 2'
print(remove_duplicated_words('cat cat cat'))          # Output should be 'cat'
print(remove_duplicated_words('1 2 3'))                # Output should be '1 2 3'



    
