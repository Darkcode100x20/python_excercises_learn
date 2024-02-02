"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple

def get_min_max(filename: str) -> Tuple[int, int]:
    min_val = None
    max_val = None
    
    with open(filename) as opened_file:
        for line in opened_file:
            # Attempt to convert the line to an integer.
            try:
                num = int(line.strip())
            except ValueError:
                # If the line cannot be converted to an integer, skip it.
                continue
            
            # If it's the first number, initialize min_val and max_val.
            if min_val is None or max_val is None:
                min_val = max_val = num
            else:
                # Update min_val and max_val if necessary.
                if num < min_val:
                    min_val = num
                if num > max_val:
                    max_val = num
    
    return (min_val, max_val)

# Example usage:
print(get_min_max('file_task6.txt'))  # Assuming the file contains integers and possibly non-integer lines.


