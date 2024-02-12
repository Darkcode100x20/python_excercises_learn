"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""


def write_word_files(words):
    # Write to file1.txt with UTF-8 encoding
    with open('file1.txt', 'w', encoding='utf-8') as file1:
        file1.write('\n'.join(words))

    # Write to file2.txt with CP1252 encoding, in reverse order
    with open('file2.txt', 'w', encoding='cp1252') as file2:
        file2.write(','.join(reversed(words)))

# Generate random words
words = generate_words()

# Write the generated words to files
write_word_files(words)

