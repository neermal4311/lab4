#!/usr/bin/env python3

# Dictionaries
dict_york = {
    'Address': '70 The Pond Rd',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M3J3M6',
    'Province': 'ON'
}

dict_newnham = {
    'Address': '1750 Finch Ave E',
    'City': 'Toronto',
    'Country': 'Canada',
    'Postal Code': 'M2J2X5',
    'Province': 'ON'
}

# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    """
    Combines two lists into a dictionary using a while loop.
    
    Args:
        keys (list): A list of keys for the dictionary.
        values (list): A list of values corresponding to the keys.
    
    Returns:
        dict: A dictionary created by pairing keys with their corresponding values.
    """
    dictionary = {}
    i = 0
    while i < len(keys) and i < len(values):
        dictionary[keys[i]] = values[i]
        i += 1
    return dictionary

def shared_values(dict1, dict2):
    """
    Finds all values that are shared between two dictionaries.
    
    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
    
    Returns:
        set: A set containing values found in both dictionaries.
    """
    set1 = set(dict1.values())
    set2 = set(dict2.values())
    shared = set1.intersection(set2)
    return shared

if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)
