"""
Write function which deletes defined element from list.
Restriction: Use .pop method of list to remove item.
Examples:
    >>> delete_from_list([1, 2, 3, 4, 3], 3)
    [1, 2, 4]
    >>> delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b')
    ['a', 'c', 'd']
    >>> delete_from_list([1, 2, 3], 'b')
    [1, 2, 3]
    >>> delete_from_list([], 'b')
    []
"""
# from the typing module are imported List and Any
# this module is for type hinting 
#(helps to understand what type of arguments a function expects and what it returns)
from typing import List, Any

# This line defines the function named: delete_from_list
# delete_from_list, takes two parameters list_to_clean, a list from which you want to remove elements
# List, in the type hint signifies that this parameter should be a list
# item_to_delete: The item you want to remove from the list
# Any, in the type hint means this can be of any data type
# -> List, This indicates that the function will return a list
def delete_from_list(list_to_clean: List, item_to_delete: Any) -> List:
    # Iterate over the list in reverse order
    # len, gives the total number of elements in the list
    # Substracting 1 gices the index of th last element
    # the last -1 indicates the index decreases by 1 in each step 
    for i in range(len(list_to_clean) -1, -1, -1):
        # checks if the current item (accessed by list_to_clean[i])is the same as item to delete
        if list_to_clean [i] == item_to_delete:
            # if the item matches with the current index i from the list
            # then method .pop removes the item from the list and ensures is still proper structured
            list_to_clean.pop(i)
    
    return list_to_clean
            
            
#Test examples
print(delete_from_list([1, 2, 3, 4, 3], 3))
print(delete_from_list(['a', 'b', 'c', 'b', 'd'], 'b'))
print(delete_from_list([1, 2, 3], 'b'))
print(delete_from_list([], 'b'))