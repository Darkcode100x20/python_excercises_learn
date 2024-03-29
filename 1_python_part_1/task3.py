"""
Write function which receives list of text lines (which is space separated words) and word number.
It should enumerate unique words from each line and then build string from all words of given number.
Restriction: word_number >= 0
Examples:
    >>> build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=1)
    'b 2 dog'
    >>> build_from_unique_words('a b c', '', 'cat dog milk', word_number=0)
    'a cat'
    >>> build_from_unique_words('1 2', '1 2 3', word_number=10)
    ''
    >>> build_from_unique_words(word_number=10)
    ''
"""
from typing import Iterable

# word_number represents the word index we are interested in
def build_from_unique_words(*lines: Iterable[str], word_number: int) -> str:
    if word_number < 0:
        return ' '
    
    result = []         # result, is a list thta stores words from 'word_number' from each line
    word_lists = []     # word_lists, a list to hold lists each containing unique words from the corresponding line
    
    # line.split() method is to get a list of words
    # .append method, is for adding the unique words founded
    for line in lines:
        # Check if the line is not empty
        if line.strip():
            # Split the line into words, remove duplicates and preserve order
            unique_words = list(set(line.split()))      # Remove duplicates and preserve order
            word_lists.append(unique_words)
        
    for unique_words in word_lists:
        if word_number - 1 < len(unique_words):
            result.append(unique_words[word_number - 1])
    
    # .join method, is used to join collected words into a single string
    return' '.join(result)

print(build_from_unique_words('a b c', '1 1 1 2 3', 'cat dog milk', word_number=0))
print(build_from_unique_words('a b c', '', 'cat dog milk', word_number=1))
print(build_from_unique_words('1 2', '1 2 3', word_number=10))
print(build_from_unique_words(word_number=10))   
