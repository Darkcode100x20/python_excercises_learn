"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List

def calculate_power_with_difference(ints: List[int]) -> List[int]:
    # Initialize empty list to store the results.
    result = []
    
    # Iterate through the given list of integers.
    for i, num in enumerate(ints):
        # Calculate the square of the current number.
        square = num ** 2
        
        # If it's not the first number, subtract the difference.
        if i > 0:
            prev_num = ints[i - 1]
            difference = (prev_num ** 2) - prev_num
            square -= difference
        
        # Append the calculated value to the result list.
        result.append(square)
        
    # Return the result list.
    return result

# Test the function with the example input.
print(calculate_power_with_difference([1, 2, 3]))  # Output should be [1, 4, 7]

