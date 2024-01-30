"""
Write function which updates dictionary with defined values but only if new value more then in dict
Restriction: do not use .update() method of dictionary
Examples:
    >>> set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4)  # only b updated because new value for a less then original value
    {'a': 1, 'b': 4, 'c': 3}
    >>> set_to_dict({}, a=0)
    {a: 0}
    >>> set_to_dict({'a': 5})
    {'a': 5}
"""
#Dict allows to specify the types of keys and values in a dictionary
from typing import Dict

# dict_to_update: Dict[str, int] is the first parameter, it indicates that 
# dict_to_update should be a dictionary with keys of type str and int
# items_to_set is the second parameter the double asterisk means that this parameter
#will accept any number of keyword arguments.
# -> Dict[str,int] indicates that the function return a dictionary with the same type as dict_to_update
def set_to_dict(dict_to_update: Dict[str, int], **items_to_set) -> Dict[str,int]:
    # a for to iterate over the items_to_set
    # .items() method returns a view object displaying a dictionary's key value
    # key, value represents each key value pair in items_to_set
    for key, value in items_to_set.items():
        # dict-to_update set the value associated with the key to value
        # if the key already exists in dict_to_update, its value is replaced with value
        # if the key does not exist in dict-to_update, a new key value is added to the dictionary
        dict_to_update[key] = value
        
    return dict_to_update
        
print(set_to_dict({'a': 1, 'b': 2, 'c': 3}, a=0, b=4))  # only b updated because new value for a less then original value
print(set_to_dict({}, a=0))
print(set_to_dict({'a': 5}))